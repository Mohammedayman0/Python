#!/usr/bin/env python
# coding: utf-8

# ETL & Data Analysis for Wine Data SET 

# In[5]:


# Required Libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[6]:


# Extraction
wine_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine_data = pd.read_csv(wine_url, header=None)

wine_quality_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_quality_data = pd.read_csv(wine_quality_url, sep=";")

# Initial look at the data
print(wine_data.head())
print(wine_quality_data.head())


# In[7]:


# Transformation
# Assigning  column names
wine_data.columns = ['class', 'alcohol', 'malic acid', 'ash',
                     'alcalinity of ash', 'magnesium', 'total phenols',
                     'flavonoids', 'nonflavonoid phenols', 'proanthocyanidins',
                     'color intensity', 'hue', 'OD280/OD315 of diluted wines',
                     'proline']

# Converting Class column into categorical datatype
wine_data['class'] = wine_data['class'].astype('category')

# Checking for any missing values in both datasets
print(wine_data.isnull().sum())
print(wine_quality_data.isnull().sum())



# In[34]:


# Normalizing 'alcohol' column in the wine_data using Min-Max normalization
wine_data['alcohol'] = (wine_data['alcohol'] - wine_data['alcohol'].min()) / (wine_data['alcohol'].max() - wine_data['alcohol'].min())

# Creating an average quality column in wine_quality_data
wine_quality_data['average_quality'] = wine_quality_data[['fixed acidity', 'volatile acidity', 'citric acid',
                                                          'residual sugar', 'chlorides', 'free sulfur dioxide',
                                                          'total sulfur dioxide', 'density', 'pH', 'sulphates',
                                                          'alcohol']].mean(axis = 1)

# Creating a 'quality_label' column based on 'average_quality'
wine_quality_data['quality_label'] = pd.cut(wine_quality_data['average_quality'], bins=[0, 5, 7, np.inf], 
                                            labels = ['low', 'medium', 'high'])


# In[35]:


wine_quality_data


# In[39]:


print (wine_quality_data.iloc[:,-2:])


# In[40]:


# Correlation Matrix
corr = wine_quality_data.corr(numeric_only = True)

# Plot heatmap
plt.figure(figsize = (12, 10))
sns.heatmap(corr, annot = True, cmap = 'coolwarm')
plt.title('Correlation Matrix of Wine Quality Data')

# Save the figure
plt.savefig('correlation_matrix.png', dpi = 300, bbox_inches = 'tight')

plt.show()


# columns have high effect in average quality : total sulfur dioxide , free sulfur dioxide 
# fixed acidity afffect density &

# In[46]:


# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Plot the pie chart
quality_counts = wine_quality_data['quality_label'].value_counts()
ax1.pie(quality_counts, labels=quality_counts.index, autopct='%1.1f%%')
ax1.set_title('Distribution of Wine Quality Ratings')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is circular.
ax1.set_xlabel('Quality Label')
ax1.set_ylabel('Count')

# Plot the histogram
ax2.hist(wine_quality_data['quality'], bins=np.arange(2.5, 9), rwidth=0.95)
ax2.set_title('Distribution of Wine Quality Ratings')
ax2.set_xlabel('Quality Ratings')
ax2.set_ylabel('Count')
ax2.set_xticks(np.arange(3, 9, step=1))

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.5)

# Save the figure
# plt.savefig('wine_quality_distributions.png', dpi=300, bbox_inches='tight')
plt.show()


# In[48]:


import matplotlib.pyplot as plt
import numpy as np

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

# Plot the scatter plot
ax1.scatter(wine_quality_data['average_quality'], wine_quality_data['total sulfur dioxide'])
ax1.set_title('Average Quality vs Total Sulfur Dioxide')
ax1.set_xlabel('Average Quality')
ax1.set_ylabel('Total Sulfur Dioxide')

# Plot the scatter plot
ax2.scatter(wine_quality_data['average_quality'], wine_quality_data['fixed acidity'])
ax2.set_title('Average Quality vs Fixed Acidity')
ax2.set_xlabel('Average Quality')
ax2.set_ylabel('Fixed Acidity')

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.5)

# Save the figure
plt.savefig('wine_quality_distributions.png', dpi=300, bbox_inches='tight')
plt.show()


# In[49]:


# Loading
# Saving the transformed data as a csv file
wine_data.to_csv('wine_dataset.csv', index = False)
wine_quality_data.to_csv('wine_quality_dataset.csv', index = False) 


# In[51]:


from sqlalchemy import create_engine
engine = create_engine('sqlite:///database.db', echo=False)


# In[53]:


wine_data.to_sql('wine_data', con=engine, if_exists='replace', index=False)
# print(wine_data.isnull().sum())
# print(wine_quality_data.isnull().sum())


# In[ ]:


# The last and critical step is encapsulating the entire ETL process into a function for reusability:
# def etl_pipeline(csv_file, db_file, table_name):
#     from sqlalchemy import create_engine
#     import pandas as pd


# In[ ]:


#    # Extract
#     data = pd.read_csv(csv_file)    # Transform
#     transformed_data = data.fillna(0)    # Load
#     engine = create_engine(f'sqlite:///{db_file}', echo=False)
#     transformed_data.to_sql(table_name, con=engine, if_exists='replace', index=False)    # Confirm successful load by querying data
#     db_df = pd.read_sql_query(f"SELECT * FROM {table_name}", con=engine)
#     print(db_df.head())

