#!/usr/bin/env python
# coding: utf-8

# In[36]:


import math


# In[56]:


nums = [80,90,100,110,120,130,140,150,150]
size = len(nums)


# In[57]:


#mean
def Mean (nums):
    size = len(nums)
    sum = 0
    
    for i in nums:
          sum+=i
         
    Mean=sum/size
    return Mean
print(Mean(nums))


# In[58]:


#median
def Median(nums):
    size = len(nums)
     
    nums.sort()
    if size % 2 ==0:
        num1=nums[size//2]
        num2=nums[size//2]
        num=(num1+num2)/2
    else:
        num=(size+1)//2
    return num
print(Median(nums))


# In[59]:


#Mode
def Mode(nums):
    d = dict()
    
    for i in nums:
        d[i] = 0
        maxi = nums[0]
    for i in nums:
        d[i] += 1
    if d[i] > d[maxi]:
            maxi = i
    if d[maxi] == 1:
        print ("Mode is not available\n")
    else:
        print("The Mode is "+str(i)+" : "+str(d[maxi]))
        
Mode(nums)


# In[61]:


#Varience
lis=[1,2,3,4,5,6,7]
n=len(lis)
mean=sum(lis)//n
var=0
for i in lis:
    var=var+(i-mean)**2
    Varience=var//n
print(Varience)


# In[62]:


#Standard deviation
lis=[1,2,3,4,5,6,7]
n=len(lis)
mean=sum(lis)//n
var=0
for i in lis:
    var=var+(i-mean)**2
    sd=(var//n)++0.5
print (sd)


# In[65]:


#Normalization
def Normalization(nums):
    mini = min(nums)
    maxi = max(nums)  
    normalized_nums = []
    for item in nums:
        normalized_nums.append((item-mini)/(maxi-mini))
    return normalized_nums
print(Normalization(nums))


# In[77]:


#Standardization
def Standardization(nums):
    avg = mean(nums)
    std dev = std dev(nums)
    Standardization_nums = []
    for item in nums:
          Standardized_nums.append((item-avg)/std_dev)
    return Standarization_nums
print(Standarization(nums))

