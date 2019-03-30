# -*- coding: utf-8 -*-

from conf.default import cmdb_host, OWNER_ID
import requests
from common.mymako import render_json
from common.log import logger
import json
from home_application.examination import jobman
from home_application.examination.script_content import script
from conf.default import JOB_USER
from home_application.models import HostInfoMonitor, HostInfo


def test(request):
    return render_json({"result": "ok", "data": request.user.username})


def search_biz(request):
    try:
        url = cmdb_host + "/api/v3/biz/search/{}".format(OWNER_ID)
        condition = {
            "page": {
                "start": 0,
                "limit": 10,
                "sort": ""
            },
            "fields": [],
            "condition": {
            }
        }

        headers = {
            "Content-Type": "application/json",
            "HTTP_BlUEKING_SUPPLIER_ID": OWNER_ID,
            "BK_USER": "admin"
        }
        json_data = json.dumps(condition)
        res = requests.post(url=url, data=json_data, headers=headers, verify=False)

        data = []
        biz_info = json.loads(res.content)["data"]["info"]
        for info in biz_info:
            data.append({
                "value": info["bk_biz_id"],
                "label": info["bk_biz_name"]
            })

        return render_json({"result": True, "data": data})

    except Exception as e:
        return render_json({"result": False, "data": []})


def search_host(request):
    try:
        request_data = json.loads(request.body)
        condition = {
            "ip": {
                "flag": "bk_host_innerip|bk_host_outerip",
                "exact": 1,
                "data": [
                    request_data["bk_host_innerip"]
                ]
            },
            "condition": [
                {
                    "bk_obj_id": "biz",
                    "fields": [

                    ],
                    "condition": [
                        {
                            "field": "default",
                            "operator": "$ne",
                            "value": 1
                        }
                    ]
                }
            ]
        }
        if request_data["bk_biz_id"]:
            condition["bk_biz_id"] = request_data["bk_biz_id"]

        url = cmdb_host + "/api/v3/hosts/search"
        headers = {
            "Content-Type": "application/json",
            "HTTP_BlUEKING_SUPPLIER_ID": OWNER_ID,
            "BK_USER": "admin"
        }
        res = requests.post(url=url, data=json.dumps(condition), headers=headers, verify=False)

        res_info = json.loads(res.content)
        if not res_info["result"]:
            return render_json({"resutl": False, "message": res_info["bk_error_msg"]})

        data = []
        cloud_name = ""
        biz_id = 0
        cloud_id = ""
        host_info = res_info["data"]["info"]
        for info in host_info:
            for cloud in info["host"]["bk_cloud_id"]:
                cloud_name = cloud["bk_inst_name"]
                cloud_id = cloud["id"]
            for biz in info["biz"]:
                biz_id = biz["bk_biz_id"]
            data.append({
                "bk_host_innerip": info["host"]["bk_host_innerip"],
                "bk_os_name": info["host"]["bk_os_name"],
                "bk_host_name": info["host"]["bk_host_name"],
                "bk_cloud_name": cloud_name,
                "bk_biz_id": biz_id,
                "bk_host_id": info["host"]["bk_host_id"],
                "bk_cloud_id": cloud_id
            })
        HostInfo.objects.bulk_create(data)
        return render_json({"result": True, "data": data})

    except Exception as e:
        logger.exception("search host info fail, error: {}".format(e))
        return render_json({"result": False, "data": []})


def add_monitor(request):
    try:
        host_info = json.loads(request.body)
        host_name = host_info["bk_host_name"]
        innerip = host_info["bk_host_innerip"]
        host_id = host_info["bk_host_id"]
        biz_id = host_info["bk_biz_id"]
        cloud_id = host_info["bk_cloud_id"]
        HostInfoMonitor.objects.create(bk_host_name=host_name, bk_host_innerip=innerip,
                                       bk_host_id=host_id, bk_biz_id=biz_id,
                                       bk_cloud_id=cloud_id)

        return render_json({"result": True, "data": {}})

    except Exception as e:
        logger.exception("add monitor fail, err: {}".format(e))
        return render_json({"result": False, "data": {}})


def delete_monitor(request):
    try:
        host_info = json.loads(request.body)
        host_id = host_info["bk_host_id"]
        HostInfoMonitor.objects.filter(bk_host_id=host_id).delete()

        return render_json({"result": True, "data": {}})

    except Exception as e:
        logger.exception("delete monitor fail, err: {}".format(e))
        return render_json({"result": False, "data": {}})


def search_info(request):
    try:
        host_info = json.loads(request.body)
        biz_id = host_info["bk_biz_id"]
        ip_list = host_info["bk_host_innerip"]
        cloud_id = host_info["bk_cloud_id"]

        result = get_host_info(biz_id, ip_list, cloud_id)
        return result

    except Exception as e:
        logger.exception("search host info fail, error: {}".format(e))
        return render_json({"result": False, "data": {}})


def get_host_info(bk_biz_id, ip_list, cloud_id):
    try:
        # logs = jobman.job_result(script, JOB_USER, bk_biz_id, ip_list, cloud_id)
        logs = {"result": True, "data": [{"ip": "192.168.165.83", "log_content": "2019-10-1|10%|20%|30%"}]}
        data = logs["data"]
        mem_usage = ""
        disk_usage = ""
        cpu_usage = ""
        for i in data:
            usage_list = i["log_content"].split("|")
            mem_usage = usage_list[1]
            disk_usage = usage_list[2]
            cpu_usage = usage_list[3]
            HostInfo.objects.filter(bk_host_innerip=i["ip"]).update(bk_mem=mem_usage,
                                                                    bk_disk=disk_usage,
                                                                    bk_cpu=cpu_usage)

        return {"result": True, "data": {"bk_mem": mem_usage, "bk_disk": disk_usage, "bk_cpu": cpu_usage}}

    except Exception as e:
        logger.exception("get logs fail, error: {}".format(e))
        return {"result": True, "data": {}}
