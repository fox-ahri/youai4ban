# youaisiban

## siban/manager/views_upload.py
```python
auth = oss2.Auth('<AK>', '<SK>')
bucket = oss2.Bucket(auth, '<地域名>', '<Bucket Name>')
s = '<域名>' + file_name
```

## siban/siban/settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '<数据库主机名/IP>',
        'PORT': '3306',
        'NAME': '<数据库名>',
        'USER': '<数据库用户名>',
        'PASSWORD': '<数据库密码>',
    },
}
```

## youai/sec/main.js
```js
Vue.prototype.url = "后端地址(末尾不能有 '/')"
```
