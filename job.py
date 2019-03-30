# -*- coding: utf-8 -*-
import base64
import json

import requests

from common.mymako import render_mako_context, render_json
import sys

from conf.default import BK_PAAS_HOST, APP_ID, APP_TOKEN

reload(sys)
sys.setdefaultencoding('utf-8')


def home(request):
    """
    首页
    """
    return render_mako_context(request, '/home_application/js_factory.html')


def get_business_list(request):
    url = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_business/"
    headers = {"Accept": "application/json"}
    params = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": request.user.username,
    }
    res = requests.post(url, data=json.dumps(params), headers=headers, verify=False)
    result = json.loads(res.content)
    if result["result"]:
        business_data = result["data"]["info"]
        business_list = [{"bk_biz_id": i["bk_biz_id"], "bk_biz_name": i["bk_biz_name"]} for i in business_data]
    else:
        return render_json({"result": False, "message": u"获取业务失败，请联系管理员。"})
    return render_json({"result": True, "data": business_list})


def get_iplist(request):
    bk_biz_id = json.loads(request.body)["bk_biz_id"]
    url = BK_PAAS_HOST + "/api/c/compapi/v2/cc/search_host/"
    headers = {"Accept": "application/json"}
    params = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": request.user.username,
        "ip": {
            "data": ["192.168.165.83"],
            "exact": 1,
            "flag": "bk_host_innerip|bk_host_outerip"
        },
        "condition": [
            {
                "bk_obj_id": "biz",
                "fields": [],
                "condition": [
                    {
                        "field": "bk_biz_id",
                        "operator": "$eq",
                        "value": int(bk_biz_id)
                    }
                ]
            }
        ]
    }
    res = requests.post(url, data=json.dumps(params), headers=headers, verify=False)
    result = json.loads(res.content)
    if result["result"]:
        data = result["data"]["info"]
        host_list = [{"bk_cloud_id": str(i["host"]["bk_cloud_id"][0]["bk_inst_id"]),
                   "bk_host_innerip": str(i["host"]["bk_host_innerip"]),
                   "bk_os_name": str(i["host"]["bk_os_name"]),
                   "bk_host_name": str(i["host"]["bk_host_name"]),
                   } for i in data]
        return render_json({"result": True, "data": host_list})
    else:
        return render_json({"result": False, "message": u"获取IP列表错误"})


def search_host(request):
    up = json.loads(request.body)
    host_id = up["id"]
    bk_biz_id = up["bk_biz_id"]
    script_content = """"""
    username = request.user.username
    return True


# 快速执行作业
def get_fast_execute_script(script_content,username,bk_biz_id,ip_list):
    # 脚本内容/当前用户/业务ID/云区域ID/IP地址
    url = BK_PAAS_HOST + "/api/c/compapi/v2/job/fast_execute_script/"
    headers = {"Accept": "application/json"}
    params = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
        "bk_biz_id": bk_biz_id,
        "script_content": base64.b64encode(script_content),
        "account": "root",
        "script_type": 1,
        "ip_list": [
            {"bk_cloud_id": ip_list.bk_cloud_id, "ip": ip_list.ip},
            {"bk_cloud_id": ip_list.bk_cloud_id, "ip": ip_list.ip}
        ]
    }
    res = requests.post(url, data=json.dumps(params), headers=headers, verify=False)
    result = json.loads(res.content)
    if result["result"]:
        job_instance_id = result["data"]["job_instance_id"]
    else:
        return False
    return ({"result": True, "data": job_instance_id})


# 根据作业实例 ID 查询作业执行状态
def get_job_instance_status(job_id,username,bk_biz_id):
    # 作业ID/当前用户/业务ID/
    url = BK_PAAS_HOST + "/api/c/compapi/v2/job/get_job_instance_status/"
    headers = {"Accept": "application/json"}
    params = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
        "bk_biz_id": bk_biz_id,
        "job_instance_id": job_id,
    }
    res = requests.post(url, data=json.dumps(params), headers=headers, verify=False)
    result = json.loads(res.content)
    if result["result"]:
        status = result["data"]["status"]
    else:
        return False
    return ({"result": True, "data": status})


# 根据作业实例ID查询作业执行日志
def get_job_instance_log(job_id,username,bk_biz_id):
    # 作业ID/当前用户/业务ID/
    url = BK_PAAS_HOST + "/api/c/compapi/v2/job/get_job_instance_log/"
    headers = {"Accept": "application/json"}
    params = {
        "bk_app_code": APP_ID,
        "bk_app_secret": APP_TOKEN,
        "bk_username": username,
        "bk_biz_id": bk_biz_id,
        "job_instance_id": job_id,
    }
    res = requests.post(url, data=json.dumps(params), headers=headers, verify=False)
    result = json.loads(res.content)
    if result["result"]:
        ip_logs = result["data"]["step_results"]["ip_logs"]
        ip_logs_list = [{"ip": i["ip"], "log_content": i["log_content"]} for i in ip_logs]
    else:
        return False
    return ({"result": True, "data": ip_logs_list})
