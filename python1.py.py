#!/usr/bin/env python
# coding: utf-8

# In[1]:


thriller=["prison break"," avengers end game"," infinity war","Inception"," men in black"," mission impossible","Money Heist","wanda vision"]
comedy=["bean","johhny english","johhny english reborn","johnny english strikes again","rambo 2"]
i=0
movie=input("Enter the movie:")
if movie==thriller[i]:
    print("It is a thriller")
elif movie==comedy[i]:
    print("It is a comedy")
else:
    print("It is not a thriller nor a comedy")


# In[ ]:


from collections import Counter

n = input("Enter total number of gloves")

print("Enter colors of array")
  
 
ar = list(map(int,input().split()))

pairs = 0

n = Counter(ar)
for i in n.values():
    
pairs += (i//2)
         

print(pairs)

