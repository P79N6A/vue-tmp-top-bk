# -*- coding: utf-8 -*-

from conf.default import APP_ID, APP_TOKEN, BK_PAAS_HOST
import requests
import base64
import json
from home_application.models import HostInfo
from time import sleep


# 快速执行作业
def get_fast_execute_script(script_content, username, bk_biz_id, ip_list, cloud_id):
    # 脚本内容/当前用户/业务ID/云区域ID/IP地址
    url = BK_PAAS_HOST + "/api/c/compapi/v2/job/fast_execute_script/"
    # url = 'http://paas.cwbke.com' + "/api/c/compapi/v3/job/fast_execute_script/"
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
            {"bk_cloud_id": cloud_id, "ip": ip_list},
            # {"bk_cloud_id": cloud_id, "ip": ip_list}
        ]
    }
    res = requests.post(url=url, data=json.dumps(params), headers=headers, verify=False)
    result = json.loads(res.content)
    if result["result"]:
        job_instance_id = result["data"]["job_instance_id"]
    else:
        return {"result": False, "job_id": 0}

    return {"result": True, "job_id": job_instance_id}


# 根据作业实例 ID 查询作业执行状态
def get_job_instance_status(job_id, username, bk_biz_id):
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
        status = result["data"]["job_instance"]["status"]
    else:
        return {"result": False, "data": 0}

    return {"result": True, "data": status}


# 根据作业实例ID查询作业执行日志
def get_log(job_id, username, bk_biz_id):
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
    ip_logs = []
    if result["result"]:
        for i in result["data"]:
            for j in i["step_results"]:
                ip_logs = j["ip_logs"]
        ip_logs_list = [{"ip": x["ip"], "log_content": x["log_content"]} for x in ip_logs]
    else:
        return {"result": False, "data": []}

    return {"result": True, "data": ip_logs_list}


def job_result(script_content, username, bk_biz_id, ip_list, cloud_id):
    try:
        exe_result = get_fast_execute_script(script_content, username, bk_biz_id, ip_list, cloud_id)
        if not exe_result["result"]:
            return {"result": False, "data": []}

        job_id = exe_result["job_id"]
        success = False
        i = 0
        status = dict()
        while i < 12 and not success:
            status = get_job_instance_status(job_id, username, bk_biz_id)
            if status["data"] == 3:
                success = True
            sleep(5)
            i += 1

        if not status["result"]:
            return {"result": False, "data": []}

        logs = get_log(job_id, username, bk_biz_id)
        return logs

    except Exception as e:
        return {"result": False, "data": []}





