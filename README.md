<h2> 矿小助后端代码</h2>



本地启动方法：
      python manage.py runserver -r -d
      
      
Centos:

      Dcoker 一键部署:
           docker build -t cumt-kxz:1.0 .
           docker run -p 12001:12001 -d -it cumt-kxz:1.0  --restrat=always
      
      直接部署：
           pip insall -r requirements.txt
           gunicorn -w 4 -b 127.0.0.1:5000 manage:app
           
           
           
Apidoc生成：
       apidoc -i src/ -o apidoc/
