#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


files = ["gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/BR_youtube_trending_data.csv",
         "gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/CA_youtube_trending_data.csv", 
         "gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/DE_youtube_trending_data.csv",
         "gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/FR_youtube_trending_data.csv",
         "gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/GB_youtube_trending_data.csv",
         "gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/IN_youtube_trending_data.csv",
         "gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/JP_youtube_trending_data.csv",
         "gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/KR_youtube_trending_data.csv",
         "gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/MX_youtube_trending_data.csv",
         "gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/RU_youtube_trending_data.csv",
         "gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/US_youtube_trending_data.csv"]


# In[3]:


df_list=[]
for filename in sorted(files):
    data = pd.read_csv(filename)
    data = data.drop(["description","tags"],axis=1)
    
    if "BR_youtube_trending_data" in filename:
        data["region"] = "Brazil"
    elif 'CA_youtube_trending_data' in filename:
        data["region"] = "Canada"
    elif 'DE_youtube_trending_data' in filename:
        data["region"] = "Germany"
    elif 'FR_youtube_trending_data' in filename:
        data["region"] = "France"
    elif 'GB_youtube_trending_data' in filename:
        data["region"] = "Great Britain"
    elif 'IN_youtube_trending_data' in filename:
        data["region"] = "India"
    elif 'JP_youtube_trending_data' in filename:
        data["region"] = "Japan"
    elif 'KR_youtube_trending_data' in filename:
        data["region"] = "Korea"
    elif 'MX_youtube_trending_data' in filename:
        data["region"] = 'Mexico'
    elif 'RU_youtube_trending_data' in filename:
        data["region"] = "Russia"
    elif 'US_youtube_trending_data' in filename:
        data["region"] = "USA"    
    df_list.append(data)


# In[4]:


full_df = pd.concat(df_list)


# In[5]:


full_df.info()


# In[6]:


full_df["video_url"]= "https://www.youtube.com/watch?v="+full_df.video_id
full_df["channel_url"] = "https://www.youtube.com/channel/"+full_df.channelId


# In[7]:


cat_df = pd.read_csv("gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Source/br_catagory.csv")


# In[8]:


full_df.to_csv("gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Destination/Cleaned_YTtest_stats.csv",index=False)


# In[9]:


final_df = pd.read_csv("gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Destination/Cleaned_YTtest_stats.csv")


# In[10]:


#final_df["categoryName"] = cat_df[str(cat_df.categoryId) == str(final_df.categoryId)].categoryName


# In[11]:


#cat_dict = cat_df.values.todict()
cat_dict = cat_df.set_index('categoryId')['categoryName'].to_dict()


cat_dict
#dfmi.loc[:, ('one', 'second')] = value


# In[12]:


final_df["category_name"] = final_df.categoryId
final_df = final_df.replace({"category_name":cat_dict})

#df2=df.replace({"Courses": dict})


# In[13]:


final_df.to_csv("gs://dataproc-staging-europe-west3-434500979019-9r1d6ed2/Dataset/Destination/Cleaned_YTfinal_stats.csv",index=False)


# In[14]:


final_df.tail()


# In[15]:


final_df.columns


# In[16]:


final_df.info()


# In[ ]:




