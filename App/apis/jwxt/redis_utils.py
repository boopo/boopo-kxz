from App.ext import redis_client


class CookieCache():
    def __init__(self, username):
        self.username = username

    def set(self, cook):
        l1 = [self.username, cook]
        redis_client.set(name=l1[0], value=l1[1], ex=43200)
        return True

    def get(self):
        data = redis_client.get(self.username)
        return str(data, encoding='utf-8')
