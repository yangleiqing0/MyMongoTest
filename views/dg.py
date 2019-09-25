from flask.views import MethodView
from flask import Blueprint, render_template, redirect, url_for
from models import DG
from common import request_get_values, get_number
from views.com import str_num_dg


def _get_number():

    _num = get_number(next(str_num_dg))
    return _num


dg_blueprint = Blueprint('dg_blueprint', __name__)


class DGList(MethodView):

    def get(self):
        search = request_get_values('search')
        dg_list = DG.objects(number__contains=search).all()
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
            DG(qx=qx, dm=dm, jy=jy, number=_get_number()).save()
        return redirect(url_for('dg_blueprint.dg_list'))


class DGDel(MethodView):

    def get(self):
        uuid = request_get_values('uuid')
        DG.objects(id=uuid).delete()
        return redirect(url_for('dg_blueprint.dg_list'))


dg_blueprint.add_url_rule('/dg_list/', view_func=DGList.as_view('dg_list'))
dg_blueprint.add_url_rule('/dg_edit/', view_func=DGEdit.as_view('dg_edit'))
dg_blueprint.add_url_rule('/dg_del/', view_func=DGDel.as_view('dg_del'))