# -*- coding: utf-8 -*-
from common.mymako import render_json
from common.log import logger
from home_application.bkcommon import utilities as util
from home_application.models import User
import json


def search_user(request):
    try:
        c = json.loads(request.body)
        user = list(User.objects.filter(name__icontains=c['value']).all().values())
        return render_json({'result': True, 'data': user})
    except Exception as e:
        logger.exception('search_user error')
        return render_json({'result': False, 'message': e.message})


def create_user(request):
    try:
        dict_data = json.loads(request.body)
        dict_data['when_created'] = util.get_time_now_str()
        dict_data['when_modified'] = util.get_time_now_str()
        res = User.objects.create(**dict_data)
        return render_json({'result': True, 'data': res.id})
    except Exception as e:
        logger.exception('create_user error')
        return render_json({'result': False, 'message': e.message})


def update_user(request):
    try:
        dict_data = json.loads(request.body)
        dict_data['when_modified'] = util.get_time_now_str()
        User.objects.filter(id=dict_data['id']).update(**dict_data)
        return render_json({'result': True, 'data': None})
    except Exception as e:
        logger.exception('update_user error')
        return render_json({'result': False, 'message': e.message})


def delete_user(request):
    try:
        id = request.GET.get('id', None)
        User.objects.filter(id=id).delete()
        return render_json({'result': True, 'data': None})
    except Exception as e:
        logger.exception('delete_user error')
        return render_json({'result': False, 'message': e.message})
