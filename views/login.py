from flask.views import MethodView
from flask import render_template, Blueprint, redirect, url_for, session, flash
from common.request_get_more_values import request_get_values
from common.connect_mongo import db


login_blueprint = Blueprint('login_blueprint', __name__)


class Login(MethodView):

    def get(self):

        return render_template('login/login.html')

    def post(self):
        username, password = request_get_values('username', 'password')
        print('username:', username, password)
        pwd = db['user'].find_one({'username': 'moadmin'}).get('password')
        print('pwd:', pwd)
        if username == 'moadmin' and password == pwd:
            session['username'] = 'moadmin'
            return redirect(url_for('zz_blueprint.zz_list'))
        else:
            flash('账号密码错误')
            return redirect(url_for('login_blueprint.login'))


class LoginOut(MethodView):

    def get(self):
        session['username'] = None
        session['user_id'] = None
        flash('登出成功')
        return redirect(url_for('login_blueprint.login'))


login_blueprint.add_url_rule('/login/', view_func=Login.as_view('login'))
login_blueprint.add_url_rule('/logout/', view_func=LoginOut.as_view('logout'))
