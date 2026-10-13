import os
import subprocess
import webbrowser

# 设置 Django 项目环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'file_manager.settings')

# 启动 Django 开发服务器
subprocess.Popen(['python3', 'manage.py', 'runserver', '127.0.0.1:8000'])

# 打开默认浏览器，访问本地服务器
webbrowser.open('http://127.0.0.1:8000')
