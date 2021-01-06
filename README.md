<h2> 矿小助后端代码</h2>

本项目为中国矿业大学 校园App 矿小助的后端代码，除内网敏感数据外，其余服务均迁移至腾讯云，可实现多台实例运行

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
       


       
       
       

