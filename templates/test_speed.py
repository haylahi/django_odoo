# author: Liberty
# date: 2019/4/28 19:02

import requests


for i in range(100):
    requests.get('http://127.0.0.1:8000/school/test/')
