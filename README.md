<h2> 矿小助后端代码</h2>

矿小助单机版(采用Flask实现)

配置文件:
   
      App/_settings.py 


本地启动方法：

      python manage.py runserver -r -d
      
      
      
Centos:

      Dcoker 一键部署:
           docker build -t cumt-kxz:1.0 .
           docker run -p 12001:22222 -d -it cumt-kxz:1.0  --restrat=always
      
      直接部署：
           使用gunicorn
           pip insall -r requirements.txt
           gunicorn -w 4 -b 127.0.0.1:22222 manage:app    //w为线程数 b 指定端口
           
           使用Tornado
           pip insall -r requirements.txt
           python tornado_server.py
Windows-server：
       
       性能较差,仅做备用
       
       需挂VPN(奇安信)

       使用Tornado：
           pip insall -r requirements.txt
           python tornado_server_win.py
           
           
Apidoc生成：

       npm install apidoc
       apidoc -i src/ -o apidoc/
       


       
       
       

