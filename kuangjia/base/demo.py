# -*- coding: utf-8 -*-
import requests
import json

class Runmain:
    def set_get(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url,data=data,header=header)
        else:
            res = requests.get(url=url, data=data)
        return res

    def set_post(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,header=header)
        else:
            res = requests.get(url=url, data=data)
        return res

    def run_set(self,url,method,data,header=None):
        res = None
        if method == "get":
            res = self.set_get(url,data.encode("utf-8"),header)
        else:
            res = self.set_post(url,data.encode("utf-8"),header)
        # return json.dumps(res,indent=2,sort_keys=True)
        # return res
        print(res.status_code)
        print(res.text)
        print(res.json)