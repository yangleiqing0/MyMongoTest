from flask.views import MethodView
from flask import Blueprint, render_template, redirect, url_for, session
from models import DG
from common import request_get_values, get_number, get_num
from views.com import str_num_dg, str_num_dg_list
from datetime import datetime


def _get_number(_str_num=str_num_dg):

    _num = get_number(next(_str_num))
    return _num


dg_blueprint = Blueprint('dg_blueprint', __name__)


class DGList(MethodView):

    def get(self):
        search = request_get_values('search')
        dg_list = DG.objects(number__contains=search).order_by('-number').all()
        return render_template('dg/list.html', items=dg_list, search=search)


class DGEdit(MethodView):

    def get(self):
        uuid = request_get_values('uuid')
        dg = None
        if uuid:
            dg = DG.objects(id=uuid).all().first()
        return render_template('dg/edit.html', dg=dg)

    def post(self):
        qx, dm, jy, uuid = request_get_values('qx', 'dm', 'jy', 'uuid')
        if uuid:
            dg = DG.objects(id=uuid).all().first()
            dg.update(qx=qx, dm=dm, jy=jy)
        else:
            if session.get('dg_data') and session.get('dg_data') != datetime.now().strftime('%Y%m%d'):
                print('!=')
                str_num_dg_list[0] = get_num()
            session['dg_data'] = datetime.now().strftime('%Y%m%d')
            DG(qx=qx, dm=dm, jy=jy, number=_get_number(str_num_dg_list[0])).save()

        return redirect(url_for('dg_blueprint.dg_list'))


class DGDel(MethodView):

    def get(self):
        uuid = request_get_values('uuid')
        DG.objects(id=uuid).delete()
        return redirect(url_for('dg_blueprint.dg_list'))


dg_blueprint.add_url_rule('/dg_list/', view_func=DGList.as_view('dg_list'))
dg_blueprint.add_url_rule('/dg_edit/', view_func=DGEdit.as_view('dg_edit'))
dg_blueprint.add_url_rule('/dg_del/', view_func=DGDel.as_view('dg_del'))