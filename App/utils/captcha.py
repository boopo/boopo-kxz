import requests
from App.ext import db
from App.models import Ocr


class Captcha:
    def __init__(self, client_key, client_id, base64):
        self.client_key = client_key
        self.client_id = client_id
        self.grant_type = "client_credentials"
        self.base64_body = {
            'image': base64
        }
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    def refresh_key(self):
        url = "https://aip.baidubce.com/oauth/2.0/token?grant_type="+self.grant_type+"&client_id="+self.client_id+"&client_secret"+self.client_key
        r = requests.post(url=url)
        if r.status_code == 200:
            session_key = r.json()['access_token']
            ocr = Ocr().query.get(1)
            ocr.access_token = session_key
            db.session.add(ocr)
            db.session.commit()
            return True
        else:
            return False

    def get_result(self):
        access_token = Ocr.query.get("1").access_token
        url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic?access_token="+access_token
        ocr_data = requests.post(url=url, data=self.base64_body, headers=self.headers)
        if ocr_data.status_code == 200 :
            if "error_msg" in ocr_data.text:
                print("error_msg")
                url_res = "https://aip.baidubce.com/oauth/2.0/token?grant_type=" + self.grant_type + "&client_id=" + self.client_id + "&client_secret=" + self.client_key
                r = requests.post(url=url_res)
                if r.status_code == 200:
                    a_token = r.json()['access_token']
                    ocr = Ocr().query.get("1")
                    ocr.access_token = a_token
                    db.session.add(ocr)
                    db.session.commit()
                    return False
            if "words_result" in ocr_data.text:
                return ocr_data.json()['words_result'][0]['words'].replace(" ", "")
        else:
            return False



