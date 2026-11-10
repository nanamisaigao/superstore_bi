import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/orders')

df=pd.read_csv("data/Sample - Superstore.csv",encoding="latin1")
df.to_sql("orders",engine,if_exists='replace',chunksize=1000,index=False)
print("数据导入成功")
