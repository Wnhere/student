from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin, current_user
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # 设置一个密钥用于会话

# 假设这是我们的用户数据库
users = {
    'admin': generate_password_hash('password')
}

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
        if username in users and check_password_hash(users[username], password):
            user = User(username)
            login_user(user)
            flash('登录成功！', 'success')
            return redirect(url_for('admin'))
        else:
            flash('用户名或密码错误。', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已成功登出。', 'success')
    return redirect(url_for('login'))

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html', students=students)

@app.route('/add_student', methods=['GET', 'POST'])
@login_required
def add_student():
    global students  # 声明使用全局变量
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        new_id = max(student['id'] for student in students) + 1
        new_student = {'id': new_id, 'name': name, 'age': age}
        students.append(new_student)
        flash('学生添加成功', 'success')
        return redirect(url_for('admin'))
    
    # 处理 GET 请求
    return render_template('add.html')

@app.route('/edit_student/<int:student_id>', methods=['GET', 'POST'])
@login_required
def edit_student(student_id):
    global students
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        for student in students:
            if student['id'] == student_id:
                student['name'] = name
                student['age'] = age
                flash('学生信息更新成功', 'success')
                return redirect(url_for('admin'))
        flash('学生信息更新失败', 'danger')
        return redirect(url_for('admin'))
    
    # 处理 GET 请求     
    for student in students:
        if student['id'] == student_id:
            return render_template('edit.html', student=student)
    flash('学生信息获取失败', 'danger')
    return redirect(url_for('admin'))

@app.route('/delete_student/<int:student_id>')
@login_required
def delete_student(student_id):
    global students
    students = [student for student in students if student['id'] != student_id]
    flash('学生信息删除成功', 'success')
    return redirect(url_for('admin'))



if __name__ == '__main__':
    app.run(debug=True)