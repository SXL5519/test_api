import csv

import pandas as pd

from db_file import DB
from read_data_file import Readfile
from configHttp import ConfigHttp


a=Readfile()
b=ConfigHttp()

tel=a.read_tel()
print(tel)

for i in tel:
    data={}
    url='http:192.168.1.72:8080/ajgsapp/user/login'
    data['telephone']=i
    data['password']=111111
    data['loginType']='ios'

    print(b.post())
