from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
from urllib.parse import urlparse, urljoin

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置一个密钥用于会话
# 数据传入 可从数据库中获取
students = [
    {'id': 1, 'name': '张三', 'age': 20},
    {'id': 2, 'name': '李四', 'age': 21},
    {'id': 3, 'name': '王五', 'age': 22},
    {'id': 4, 'name': '赵六', 'age': 23},
    {'id': 5, 'name': '钱七', 'age': 24}
]
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# 这只是一个示例用户类，实际应用中您应该连接到数据库
class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        remember = 'rememberMe' in request.form
        # 验证用户名和密码
        return redirect('/admin')
    return render_template('login.html')


@app.route('/admin')
def admin():
    return render_template('admin.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)