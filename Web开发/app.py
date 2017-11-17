#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  PythonRepository
#  Created by xingl on 2017/11/10.
#  Filename: app


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/sigin', methods=['GET'])
def sigin_form():
    print('login')
    return render_template('form.html')

@app.route('/sigin', methods=['POST'])
def sigin():
    username = request.form['username']
    password = request.form['password']
    print(username,'-->', password)
    if username=='admin' and password=='password':
        # 在Jinja2模板中，我们用{{ name }}表示一个需要替换的变量。
        # 很多时候，还需要循环、条件判断等指令语句，在Jinja2中，用{% ... %}表示指令。
        return render_template('sigin-ok.html', username=username, page_list = [1,2,3])
    return render_template('form.html', message='Bad username or password', username=username)

if __name__ == '__main__':
    app.run()