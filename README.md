<h2> 矿小助后端代码</h2>

矿小助单机多实例版(采用Flask实现)<br>
SpringColud版正在摸鱼开发中...<br>
具体实现及其原理解析[点此](https://www.yuque.com/boopo/pc)

使用到的技术：
- Nginx
- Redis
- MySQL
- Celery
- Flask

注意 ：请在校园内网环境下启动,否则无法正常运行

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
       
       目前在用
       需挂VPN(easyConnect)

       使用Tornado：
           pip insall -r requirements.txt
           python tornado_server_win.py
       在其他资源允许的情况下可以启动多个实例    
           
Apidoc生成：

       npm install apidoc
       apidoc -i src/ -o apidoc/
       


       
       
       

