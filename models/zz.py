from mongoengine import StringField
from db_create import db


class ZZ(db.Document):
    # 继承Document类,为普通文档
    uuid = StringField()
    dj = StringField()
    sj = StringField()
    dm = StringField()
    jy = StringField()
    number = StringField()
