#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[19]:


customers = pd.read_csv(r"E:\Python\P\Ecommerce.csv")



# In[20]:


customers.head()


# In[21]:


customers.describe()


# In[22]:


customers.columns


# In[23]:


customers.info()


# In[24]:


sns.jointplot(x='Time on Website',y ='Yearly Amount Spent', data = customers)


# In[26]:


sns.jointplot(x='Time on App',y ='Yearly Amount Spent', data = customers)


# In[27]:


sns.jointplot(x='Time on App',y ='Length of Membership', data = customers, kind='hex')


# In[49]:


sns.pairplot(customers)


# In[32]:


print("Length of Membership")



# In[33]:


sns.set(color_codes=True)
sns.lmplot(x='Length of Membership', y='Yearly Amount Spent',data=customers)



# In[35]:


X = customers[['Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership']]

y= customers['Yearly Amount Spent']


# In[36]:


from sklearn.model_selection import train_test_split


# In[37]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)


# In[38]:


from sklearn.linear_model import LinearRegression


# In[41]:


lm = LinearRegression()


# In[42]:


lm.fit(X_train, y_train )


# In[43]:


print(lm.coef_)



# In[44]:


predictions = lm.predict(X_test)


# In[45]:


plt.pyplot.scatter(y_test, predictions)
plt.pyplot.ylabel('Predicted')
plt.pyplot.xlabel('Y test')


# In[46]:


import sklearn.metrics as metrics
print('MAE: {}'.format(metrics.mean_absolute_error(y_test, predictions)))
print('MSE: {}'.format(metrics.mean_squared_error(y_test, predictions)))
print('RMSE: {}'.format(np.sqrt(metrics.mean_squared_error(y_test, predictions))))


# In[47]:


sns.distplot((y_test-predictions))


# In[48]:


pd.DataFrame(lm.coef_ , X.columns, columns=['Coeffecient'])


# In[ ]:


# How can you interpret these coefficients?

# The greater the value the more related it is to the target, in this case yearly amount spent

# Do you think the company should focus more on their mobile app or on their website?

# The company should focus on the mobile app

