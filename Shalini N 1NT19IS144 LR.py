#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("/home/ignis/Downloads/shalini.csv")
df


# In[4]:


df.plot(x="Hours", y="Scores", style="o")
plt.show()


# In[5]:


x_mean = df["Hours"].mean()
y_mean = df["Scores"].mean()
print(x_mean, y_mean)


# In[6]:


df["x"] = df["Hours"] - x_mean
df["y"] = df["Scores"] - y_mean
df["x*y"] = df["x"] * df["y"]
df["x^2"] = df["x"]**2
df["y^2"] = df["y"]**2
df


# In[7]:


summation_x_y = df["x*y"].sum()
summation_x_squared = df["x^2"].sum()
summation_y_squared = df["y^2"].sum()
print(summation_x_y, summation_x_squared, summation_y_squared)


# In[8]:


correlation = summation_x_y / (summation_x_squared *
summation_y_squared)**0.5
correlation


# In[10]:


def getMean(numbers):
    if len(numbers) == 0:
        return None
    else:
        current_sum = 0
        for i in numbers:
            current_sum += i
            current_avg = current_sum/len(numbers)
        return current_avg


# In[12]:


def getStandardDeviation(numbers):
    if len(numbers) == 0:
        return 0
    else:
        mean = getMean(numbers)
        std_deviation = 0
        for i in numbers:
            std_deviation += (i - mean)**2
        return (std_deviation/len(numbers))**0.5


# In[13]:


std_deviation_x = getStandardDeviation(df["x"].tolist())
std_deviation_y = getStandardDeviation(df["y"].tolist())
print(std_deviation_x, std_deviation_y)


# In[14]:


m = correlation * (std_deviation_y / std_deviation_x)
m


# In[15]:


c = df["Scores"].mean() - m * df["Hours"].mean()
c


# In[17]:


df["y_prediction"] = m * df["Hours"] + c
df


# In[18]:


plot1 = plt.scatter(df["Hours"], df["Scores"])
plot2 = plt.scatter(df["Hours"], df["y_prediction"])
plt.show()


# In[ ]:




