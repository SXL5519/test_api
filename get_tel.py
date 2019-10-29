import ast
import csv

import pandas as pd

from db_file import DB
from read_data_file import Readfile

a= DB()
b=Readfile()

list=b.read()

print(list)

def get_sql(i):
    n={"_id" :i}
    return n
qq=0
for i in list:
    # print(type(i))
    c=i.strip()
    tel=''
    list=[]
    list.append(c)
    value=a.connect_mongodb_all('tb_user',n=get_sql(c))
    # print(type(value))
    # for j in value:
        # print(type(j))
    tel=value.get('telephone')
    list.append(tel)
    # print(tel)
    # data=pd.DataFrame(tel,columns=['tel'])
    # data.to_csv("G:/yali/order.csv")
    with open("G:/yali/order1.csv", 'a+', newline='') as f:
        csv_write = csv.writer(f)
        csv_write.writerow(list)
    print(qq)
    qq=qq+1
    if qq>30000:
        break
