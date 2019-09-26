from _main import register_init
from flask import request, session, redirect, url_for
# from flask_mongoengine import MongoEngine

app = register_init()
app.secret_key = 'asldfwadadw@fwq@#!Eewew'
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'productDB',
#     'host': 'localhost',
#     'port': 27017
# }
# db = MongoEngine(app)


@app.before_request    # 在请求达到视图前执行
def login_required():

    # print('username: ', session.get('username'), request.path, type(session.get('username')))

    if request.path in ('/login/',):
        return
    elif session.get('username'):
        return
    else:
        return redirect(url_for('login_blueprint.login'))


if __name__ == '__main__':
    app.run()
