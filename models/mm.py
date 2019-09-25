from mongoengine import StringField
from db_create import db


class MM(db.Document):
    # 继承Document类,为普通文档
    uuid = StringField()
    name = StringField()
    remark = StringField()
    number = StringField()


