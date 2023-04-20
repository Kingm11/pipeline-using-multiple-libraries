#!/usr/bin/env python
# coding: utf-8

# ## First, let's start by importing the necessary libraries and loading the iris dataset:
# 

# In[1]:


import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from yellowbrick.classifier import ConfusionMatrix

# load iris dataset
iris = load_iris()
X = iris.data
y = iris.target


# ## Let's split the dataset into training and testing sets:

# In[2]:


# split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# ## Now, let's create a pipeline to preprocess the data and train a logistic regression model:
# 

# In[3]:


# create pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(random_state=42))
])

# train model
pipeline.fit(X_train, y_train)


# ## We can use Yellowbrick to visualize the confusion matrix:

# In[4]:


# predict labels for test set
y_pred = pipeline.predict(X_test)

# plot confusion matrix
cm = ConfusionMatrix(pipeline, classes=iris.target_names)
cm.score(X_test, y_test)
cm.show()


# ## Finally, we can use Seaborn to visualize the relationship between the features and the target:

# In[5]:


# create dataframe with features and target
df = pd.DataFrame(data=X, columns=iris.feature_names)
df['target'] = y

# plot pairplot
sns.pairplot(data=df, hue='target', palette='colorblind')


# In[ ]:




