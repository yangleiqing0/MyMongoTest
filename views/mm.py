from flask.views import MethodView
from flask import Blueprint, render_template, redirect, url_for, session
from models import MM
from common import request_get_values, get_number, get_num
from views.com import str_num_mm, str_num_mm_list
from datetime import datetime


def _get_number(_str_num=str_num_mm):

    _num = get_number(next(_str_num))
    return _num


mm_blueprint = Blueprint('mm_blueprint', __name__)


class MMList(MethodView):

    def get(self):
        search = request_get_values('search')
        mm_list = MM.objects(number__contains=search).order_by('-number').all()
        return render_template('mm/list.html', items=mm_list, search=search)


class MMEdit(MethodView):

    def get(self):
        uuid = request_get_values('uuid')
        mm = None
        if uuid:
            mm = MM.objects(id=uuid).all().first()
        return render_template('mm/edit.html', mm=mm)

    def post(self):
        name, remark, uuid = request_get_values('name', 'remark', 'uuid')
        if uuid:
            mm = MM.objects(id=uuid).all().first()
            mm.update(name=name, remark=remark)
        else:
            if session.get('mm_data') and session.get('mm_data') != datetime.now().strftime('%Y%m%d'):
                str_num_mm_list[0] = get_num()
            session['mm_data'] = datetime.now().strftime('%Y%m%d')
            MM(name=name, remark=remark, number=_get_number(str_num_mm_list[0])).save()
        return redirect(url_for('mm_blueprint.mm_list'))


class MMDel(MethodView):

    def get(self):
        uuid = request_get_values('uuid')
        MM.objects(id=uuid).delete()
        return redirect(url_for('mm_blueprint.mm_list'))


mm_blueprint.add_url_rule('/mm_list/', view_func=MMList.as_view('mm_list'))
mm_blueprint.add_url_rule('/mm_edit/', view_func=MMEdit.as_view('mm_edit'))
mm_blueprint.add_url_rule('/mm_del/', view_func=MMDel.as_view('mm_del'))