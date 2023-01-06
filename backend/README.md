## 準備

```
 $ cd react-flask-template-app/backend
 
 $ pip install -r requirements.txt
```

## 実行方法

### Flask起動

```sh
 $ cd react-flask-template-app/backend
 
 $ flask run
    * Serving Flask app 'apps.run:create_app('local')'
    * Debug mode: on
   WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
    * Running on http://127.0.0.1:5000
   Press CTRL+C to quit
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 151-350-782
```

### Pytest実行

Pytestは起動方法が複数あるが、以下はフォルダをまとめて実行するやり方。

```sh
 $ cd react-flask-template-app/backend/apps/tests
 
 $ pytest .
```

## Docker起動方法

```sh
 $ docker build -t sample-app ./
 
 $ docker images
   REPOSITORY   TAG         IMAGE ID       CREATED          SIZE
   sample-app   latest      fb6a957542a9   8 minutes ago    971MB
 
 $ docker run --name sample-app -d -p 8080:5000 sample-app
 
 $ docker ps
 
 $ docker stop sample-app
 
 $ docker ps
```