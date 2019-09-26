from flask.views import MethodView
from flask import Blueprint, render_template, redirect, url_for, session
from models import ZZ
from common import request_get_values, get_number, get_num
from views.com import str_num_zz, str_num_zz_list
from datetime import datetime


def _get_number(_str_num=str_num_zz):

    _num = get_number(next(_str_num))
    return _num


zz_blueprint = Blueprint('zz_blueprint', __name__)


class ZZList(MethodView):

    def get(self):
        search = request_get_values('search')
        zz_list = ZZ.objects(number__contains=search).order_by('-number').all()
        return render_template('zz/list.html', items=zz_list, search=search)


class ZZEdit(MethodView):

    def get(self):
        uuid = request_get_values('uuid')
        zz = None
        if uuid:
            zz = ZZ.objects(id=uuid).all().first()
        return render_template('zz/edit.html', zz=zz)

    def post(self):
        dj, sj, dm, jy, uuid = request_get_values('dj', 'sj', 'dm', 'jy', 'uuid')
        if uuid:
            zz = ZZ.objects(id=uuid).all().first()
            zz.update(dj=dj, sj=sj, dm=dm, jy=jy)
        else:
            if session.get('zz_data') and session.get('zz_data') != datetime.now().strftime('%Y%m%d'):
                str_num_zz_list[0] = get_num()
            session['zz_data'] = datetime.now().strftime('%Y%m%d')
            ZZ(dj=dj, sj=sj, dm=dm, jy=jy, number=_get_number(str_num_zz_list[0])).save()
        return redirect(url_for('zz_blueprint.zz_list'))


class ZZDel(MethodView):

    def get(self):
        uuid = request_get_values('uuid')
        ZZ.objects(id=uuid).delete()
        return redirect(url_for('zz_blueprint.zz_list'))


zz_blueprint.add_url_rule('/zz_list/', view_func=ZZList.as_view('zz_list'))
zz_blueprint.add_url_rule('/zz_edit/', view_func=ZZEdit.as_view('zz_edit'))
zz_blueprint.add_url_rule('/zz_del/', view_func=ZZDel.as_view('zz_del'))