from mongoengine import StringField
from db_create import db


class DG(db.Document):
    # 继承Document类,为普通文档
    uuid = StringField()
    qx = StringField()
    dm = StringField()
    jy = StringField()
    number = StringField()


