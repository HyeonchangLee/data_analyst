
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

crm_dataset = pd.read_csv('/Users/hyeonchanglee/Documents/data_analyst/004마케팅_퍼널/CRM_dataset/CRM_dataset.csv', encoding = 'unicode_escape')

print(crm_dataset)
print(crm_dataset.info())

crm_dataset['InvoiceDate'] = pd.to_datetime(crm_dataset['InvoiceDate'] )
print(crm_dataset.info())


df = crm_dataset

#  #   Column       Non-Null Count   Dtype  
# ---  ------       --------------   -----  
#  0   InvoiceNo    541909 non-null  object 
#  1   StockCode    541909 non-null  object 
#  2   Description  540455 non-null  object 
#  3   Quantity     541909 non-null  int64  
#  4   InvoiceDate  541909 non-null  object 
#  5   UnitPrice    541909 non-null  float64
#  6   CustomerID   406829 non-null  float64
#  7   Country      541909 non-null  object 

#  InvoiceNo StockCode                           Description  Quantity      InvoiceDate  UnitPrice  CustomerID         Country
#  0  536365    85123A   WHITE HANGING HEART T-LIGHT HOLDER         6   12/1/2010 8:26       2.55     17850.0  United Kingdom


# # to_mysql 

# SQL
# CREATE TABLE sales_table (
#  seq        INT NOT NULL ,
#  invoice_no     VARCHAR(30),
#  stock_code    VARCHAR(30),
#  description   VARCHAR(500),
#  quantity    INT,  
#  invoice_date    DATETIME,  
#  unit_price    FLOAT,  
#  custome_id    VARCHAR(20),  
#  country   VARCHAR(50),
#   PRIMARY KEY(seq)
# ) ENGINE=MYISAM ;

# numpy의 nan을 None으로 변경
df = df.replace({np.nan: None})

df['seq'] = np.arange(0, len(df), 1)

seq = list(df['seq'] )
invoice_no = list(df['InvoiceNo'] )
stock_code = list(df['StockCode'] )
description = list(df['Description'] )
quantity = list(df['Quantity'] )
invoice_date = list(df['InvoiceDate'] )
unit_price = list(df['UnitPrice'] )
custome_id = list(df['CustomerID'] )
country = list(df['Country'] )


import pymysql
conn = pymysql.connect(host='localhost', user='root', password='1234', db='crm')
# conn = pymysql.connect(host='localhost', user='root', password='1234', db='crm', charset='utf8')
cur = conn.cursor()
# cur.execute("INSERT INTO sales_table VALUES('create_date','15:00','남성패션',31,'    뮤니드 8mm RULED 노트 8종 세트, WHITE, DARK NAVY, MONOGREY, SWEET ORANGE, LEMON, AQUAMINT, VIOLET, LOVELY PINK, 1세트', 14868675097,11900,4.5,22852,'https://www.coupang.com/vp/products/340621082?itemId=1084367415&vendorItemId=5589631461&sourceType=CATEGORY&categoryId=186969')")

sql = "INSERT INTO sales_table VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
# val = seq,invoice_no,stock_code,description,quantity,invoice_date,unit_price,custome_id,country
# cur.execute(sql,val)


for i in tqdm(range(len(df))):
    
# # sql구문 실행
    cur.execute(sql,(seq[i],invoice_no[i],stock_code[i],description[i],quantity[i],invoice_date[i],unit_price[i],custome_id[i],country[i]))



conn.commit()
conn.close()

