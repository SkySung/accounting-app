from flask import Flask, request, render_template, redirect, url_for
import sqlite3
import bcrypt

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 假設從表單獲取用戶名和電子郵件
        username = request.form['username']
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # 在這裡處理註冊邏輯，保存到數據庫
        try:
            conn = sqlite3.connect('mydatabase.db')
            cur = conn.cursor()
            # 确保在插入记录时为PasswordHash字段提供hashed_password
            cur.execute('INSERT INTO Users (Username, PasswordHash, Email) VALUES (?, ?, ?)',
                        (username, hashed_password, email))  # 假设email也是从表单获取的
            conn.commit()
        except sqlite3.IntegrityError as e:
            print(e)
            return "Registration failed due to database error."
        finally:
            conn.close()
        return redirect(url_for('registration_success', username=username))
    
    # 如果不是POST請求，顯示註冊表單
    return render_template('register.html')

@app.route('/registration_success/<username>')
def registration_success(username):
    # 顯示註冊成功頁面
    return render_template('registration_success.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)
