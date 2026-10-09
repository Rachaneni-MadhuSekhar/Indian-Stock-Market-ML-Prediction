#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import warnings
warnings.filterwarnings("ignore",category=UserWarning)


# In[2]:


stock=['RELIANCE.NS','INFY.NS','HDFCBANK.NS','BHARTIARTL.NS','ASIANPAINT.NS']
IS=yf.download(stock,period='5d',interval='5m')
IS=IS.stack(level=1,future_stack=True).reset_index()
IS


# In[3]:


IS.rename(columns={'Datetime':'Date_time','Ticker':'Company','Close':'Closeing_time_price','Open':'Opening_time_price','Volume':'Total_stocks_sold'
                  ,'High':'High_price','Low':'Low_price'},inplace=True)


# In[4]:


IS.shape


# In[5]:


IS.columns


# In[6]:


IS.dtypes


# In[7]:


IS.isnull().sum()


# In[8]:


IS=IS.dropna()


# In[9]:


IS=IS.reset_index(drop=True)
IS


# In[10]:


IS.describe()


# In[11]:


import mysql.connector as mc
import pandas as pd


# In[12]:


#created conneaction between Jupyter notebook and MYSQl
DB=mc.connect(
    host='localhost',
    port=3306,
    user='root',
    password='423155',
    database='indian_stocks')
cursor = DB.cursor(buffered=True)


# In[13]:


query= """ 
INSERT INTO indian_stocks(Date_time,Company,Closeing_time_price,High_price,Low_price,Opening_time_price,Total_stocks_sold)
VALUES(%s,%s,%s,%s,%s,%s,%s) """


# In[14]:


cursor.execute('TRUNCATE TABLE indian_stocks')
for row in IS.itertuples(index=False,name=None):
    cursor.execute(query ,row)
DB.commit()
print("Data inserted successfully")


# In[15]:


Relaince="select Date_time, Company,Closeing_time_price, High_price,Low_price,Opening_time_price,Total_stocks_sold from indian_stocks WHERE company='RELIANCE.NS'"
Relaince=pd.read_sql(Relaince, DB)
Reliance=Relaince
Reliance  


# In[16]:


Asianpaint="select Date_time , Company,Closeing_time_price, High_price,Low_price,Opening_time_price,Total_stocks_sold from indian_stocks WHERE company='ASIANPAINT.NS'"
Asianpaint=pd.read_sql(Asianpaint, DB)
Asianpaint


# In[17]:


Bhartiartl="select Date_time , Company,Closeing_time_price, High_price,Low_price,Opening_time_price,Total_stocks_sold from indian_stocks WHERE company='BHARTIARTL.NS'"
Bhartiartl=pd.read_sql(Bhartiartl, DB)
Bhartiartl


# In[18]:


Hdfc="select Date_time , Company,Closeing_time_price, High_price,Low_price,Opening_time_price,Total_stocks_sold from indian_stocks WHERE company='HDFCBANK.NS'"
Hdfc=pd.read_sql(Hdfc, DB)
Hdfc


# In[19]:


Infy="select Date_time , Company,Closeing_time_price, High_price,Low_price,Opening_time_price,Total_stocks_sold from indian_stocks where company = 'INFY.NS'"
Infy=pd.read_sql(Infy , DB)
Infy


# In[20]:


#creating target column for every comapny
Asianpaint['Target_Price'] =  Asianpaint['Closeing_time_price'].shift(-1)
Infy['Target_Price']=Infy['Closeing_time_price'].shift(-1)
Reliance['Target_Price']=Reliance['Closeing_time_price'].shift(-1)
Hdfc['Target_Price']=Hdfc['Closeing_time_price'].shift(-1)
Bhartiartl['Target_Price']=Bhartiartl['Closeing_time_price'].shift(-1)


# In[21]:


Asianpaint


# In[22]:


Asianpaint=Asianpaint.dropna()
Bhartiartl=Bhartiartl.dropna()
Hdfc=Hdfc.dropna()
Infy=Infy.dropna()
Reliance=Reliance.dropna()


# In[23]:


#Training the Asianpaint Model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,root_mean_squared_error
import joblib as jl


# In[24]:


#Training the Asianpaint Mode
AX=Asianpaint[['Closeing_time_price','High_price','Low_price','Opening_time_price','Total_stocks_sold']] #input features
AY=Asianpaint['Target_Price'] #target features
X_Asianpaint_train,X_Asianpaint_test,Y_Asianpaint_train,Y_Asianpaint_test=train_test_split(AX,AY,test_size=0.2,random_state=42)
AL=LinearRegression() #Model creation
AL.fit(X_Asianpaint_train,Y_Asianpaint_train) #model train
Y_Asianpaint_test_pred=AL.predict(X_Asianpaint_test) #predicting the test data
print('R2score:',r2_score(Y_Asianpaint_test,Y_Asianpaint_test_pred))
print('MAE:',mean_absolute_error(Y_Asianpaint_test,Y_Asianpaint_test_pred))
Asianpaint['Predicted_Value']=AL.predict(AX)
jl.dump(AL , 'Asianpaint.pkl')


# In[25]:


#Training the Bharatiartl Model
BX=Bhartiartl[['Closeing_time_price','High_price','Low_price','Opening_time_price','Total_stocks_sold']]  #input features
BY=Bhartiartl['Target_Price'] #target features
X_Bhartiartl_train,X_Bhartiartl_test,Y_Bhartiartl_train,Y_Bhartiartl_test=train_test_split(BX,BY,test_size=0.2,random_state=42)
BL=LinearRegression() #Model creation
BL.fit(X_Bhartiartl_train,Y_Bhartiartl_train) #model train
Y_Bhartiartl_test_pred=BL.predict(X_Bhartiartl_test) #predicting the test data
print('R2score:',r2_score(Y_Bhartiartl_test,Y_Bhartiartl_test_pred))
print('MAE:',mean_absolute_error(Y_Bhartiartl_test,Y_Bhartiartl_test_pred))
Bhartiartl['Predicted_Value']=BL.predict(BX) 
jl.dump(BL , 'Bhartiartl.pkl')


# In[26]:


#Training the Hdfc model
HX=Hdfc[['Closeing_time_price','High_price','Low_price','Opening_time_price','Total_stocks_sold']] #input featured
HY=Hdfc['Target_Price']                                      #Target value
X_Hdfc_train,X_Hdfc_test,Y_Hdfc_train,Y_Hdfc_test=train_test_split(HX,HY,test_size=0.2,random_state=42) 
HL=LinearRegression() #model creation
HL.fit(X_Hdfc_train,Y_Hdfc_train)    #model training
Y_Hdfc_test_pred = HL.predict(X_Hdfc_test) #predicting the test data
print('R2score:',r2_score(Y_Hdfc_test,Y_Hdfc_test_pred))
print('MAE:',mean_absolute_error(Y_Hdfc_test,Y_Hdfc_test_pred))
Hdfc['Predicted_Value']=HL.predict(HX)
Hdfc
jl.dump(HL , 'Hdfc.pkl')


# In[27]:


IX=Infy[['Closeing_time_price','High_price','Low_price','Opening_time_price','Total_stocks_sold']]  #input features
IY=Infy['Target_Price']                                       #Target value
X_Infy_train,X_Infy_test,Y_Infy_train,Y_Infy_test=train_test_split(IX,IY,test_size=0.2,random_state=42)
IL=LinearRegression()                                     #model creation
IL.fit(X_Infy_train,Y_Infy_train)               #model training
Y_Infy_test_pred=IL.predict(X_Infy_test)
print('R2score:',r2_score(Y_Infy_test,Y_Infy_test_pred))
print('MAE:',mean_absolute_error(Y_Infy_test,Y_Infy_test_pred))
Infy['Predicted_Value']=IL.predict(IX)
Infy
jl.dump(IL , 'Infy.pkl')


# In[28]:


RX=Reliance[['Closeing_time_price','High_price','Low_price','Opening_time_price','Total_stocks_sold']]
RY=Reliance['Target_Price']
X_Reliance_train,X_Reliance_test,Y_Reliance_train,Y_Reliance_test=train_test_split(RX,RY,test_size=0.2,random_state=42)
RL=LinearRegression()
RL.fit(X_Reliance_train,Y_Reliance_train)
Y_Reliance_test_pred=RL.predict(X_Reliance_test)
print('R2score:',r2_score(Y_Reliance_test,Y_Reliance_test_pred))
print('MAE:',mean_absolute_error(Y_Reliance_test,Y_Reliance_test_pred))
Reliance['Predicted_Value']=RL.predict(RX)
jl.dump(RL , 'Reliance.pkl')


# In[29]:


Amodel = jl.load('Asianpaint.pkl') # import model for prepartion
Asianpaint=pd.read_sql("select * from indian_stocks where Company = 'ASIANPAINT.NS' order by Date_time desc limit 1" , DB) # importlast row
AX_latest=Asianpaint[['Closeing_time_price','High_price','Low_price','Opening_time_price','Total_stocks_sold']]
Predicted_Value=Amodel.predict(AX_latest)
Predicted_Value

#adding predicted value to mysql table 
Predicted_Value=float(Predicted_Value[0])
cursor.execute("""update indian_stocks set Predicted_Value = %s WHERE Company = %s order by Date_time DESC limit 1 """,(Predicted_Value,"ASIANPAINT.NS"))
DB.commit()
print("updated successfully")


# In[30]:


Bmodel = jl.load('Bhartiartl.pkl')
Bhartiartl=pd.read_sql("select * from indian_stocks where Company = 'BHARTIARTL.NS' order by Date_time desc limit 1",DB)
BX_latest=Bhartiartl[['Closeing_time_price','High_price','Low_price','Opening_time_price','Total_stocks_sold']]
Predicted_Value=Bmodel.predict(BX_latest)
Predicted_Value

#import predicted value into Mysql tabel
Predicted_Value=float(Predicted_Value)
cursor.execute(""" update indian_stocks set Predicted_Value = %s where Company = %s order by Date_time desc limit 1 """,(Predicted_Value,"BHARTIARTL.NS"))
DB.commit()


# In[31]:


Hmodel = jl.load('Hdfc.pkl')
Hdfc=pd.read_sql("select * from indian_stocks where Company = 'HDFCBANK.NS' order by Date_time desc limit 1",DB)
HX_latest=Hdfc[['Closeing_time_price','High_price','Low_price','Opening_time_price','Total_stocks_sold']]
Predicted_Value=Hmodel.predict(HX_latest)
Predicted_Value

#import predicted value into Mysql tabel
Predicted_Value=float(Predicted_Value)
cursor.execute(""" update indian_stocks set Predicted_Value = %s where Company = %s order by Date_time desc limit 1 """,(Predicted_Value,"HDFCBANK.NS"))
DB.commit()


# In[32]:


Imodel = jl.load('Infy.pkl')
Infy=pd.read_sql("select * from indian_stocks where Company = 'INFY.NS' order by Date_time desc limit 1",DB)
IX_latest=Infy[['Closeing_time_price','High_price','Low_price','Opening_time_price','Total_stocks_sold']]
Predicted_Value=Imodel.predict(IX_latest)
Predicted_Value

#import predicted value into Mysql tabel
Predicted_Value=float(Predicted_Value)
cursor.execute(""" update indian_stocks set Predicted_Value = %s where Company = %s order by Date_time desc limit 1 """,(Predicted_Value,"INFY.NS"))
DB.commit()


# In[87]:


Rmodel = jl.load('Reliance.pkl')
Reliance=pd.read_sql("select * from indian_stocks where Company = 'RELIANCE.NS' order by Date_time desc limit 1",DB)
RX_latest=Reliance[['Closeing_time_price','High_price','Low_price','Opening_time_price','Total_stocks_sold']]
Predicted_Value=Rmodel.predict(RX_latest)
Predicted_Value

#import predicted value into Mysql tabel
Predicted_Value=float(Predicted_Value)
cursor.execute(""" update indian_stocks set Predicted_Value = %s where Company = %s order by Date_time desc limit 1 """,(Predicted_Value,"RELIANCE.NS"))
DB.commit()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




