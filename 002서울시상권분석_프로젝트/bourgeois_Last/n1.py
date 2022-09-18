import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json



#-*- coding: utf-8 -*-
import os
import sys
import urllib.request

client_id = "ScaTb_f8PQ5GJteI95Kw"
client_secret = "xMj_ezOoXg"

url = "https://openapi.naver.com/v1/datalab/search"
body = "{\"startDate\":\"2021-01-01\",\
    \"endDate\":\"2021-12-31\",\
    \"timeUnit\":\"month\",\
    \"keywordGroups\":[{\"groupName\":\"구로구\",\"keywords\":[\"구로구 맛집\",\"구로구 까페\",\"구로구 술집\"]}],\
    \"device\":\"pc\",\
    \"ages\":[\"1\",\"2\"],\
    \"gender\":\"f\"}"

# body = "{\"startDate\":\"2021-01-01\",\
#     \"endDate\":\"2021-04-30\",\
#     \"timeUnit\":\"month\",\
#     \"keywordGroups\":[{\"groupName\":\"한글\",\"keywords\":[\"한글\",\"korean\"]},\
#                         {\"groupName\":\"영어\",\"keywords\":[\"영어\",\"english\"]}],\
#     \"device\":\"pc\",\
#     \"ages\":[\"1\",\"2\"],\
#     \"gender\":\"f\"}"

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")
response = urllib.request.urlopen(request, data=body.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))

else:
    print("Error Code:" + rescode)







