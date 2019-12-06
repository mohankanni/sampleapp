# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 11:23:11 2019

@author: saivalini
"""
import streamlit as st
import pandas as pd
import os
import numpy as np
from main import department,frequency_generator

# Data Viz Pkgs
import matplotlib
matplotlib.use('Agg')# To Prevent Errors
import matplotlib.pyplot as plt
# import seaborn as sns
from matplotlib.pyplot import figure

# st.title("Grievances Text Analytics")

html_temp = """
	<div style="background-color:;"><p style="color:tomato;font-size:30px;font-weight: bolder;">Grievances Text Analytics</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)

data = pd.DataFrame(pd.read_csv('data.csv'))

duration_data=data[(data['CUST_FEEDBACK'].str.contains('one month','1 month')) | (data['CUST_FEEDBACK'].str.contains('2 month','two month')) |(data['CUST_FEEDBACK'].str.contains('week')) | (data['CUST_FEEDBACK'].str.contains('10 days','15 days'))]                                  
filtermaster = pd.DataFrame(data[['COM_ID','DEPT_ID','SECTION_ID']].groupby(['DEPT_ID','SECTION_ID'],as_index=False).count())

# Drop Down Select Box
departmentfilter = st.sidebar.selectbox('Department',list(["ALL"]) + list(department(filtermaster['DEPT_ID'])))

if departmentfilter != 'ALL':
	sectiondata = list(["ALL"]) + list(department(filtermaster['SECTION_ID'][(filtermaster.DEPT_ID == departmentfilter)]))
	sectionfilter = st.sidebar.selectbox('Section',sectiondata)

#Data Filter
if departmentfilter != 'ALL':
 	if sectionfilter != 'ALL':
 		filtereddata = duration_data[(duration_data.DEPT_ID == departmentfilter) & (duration_data.SECTION_ID == sectionfilter)]
 	else:
 		filtereddata = duration_data[(duration_data.DEPT_ID == departmentfilter)]
else:
 	filtereddata = duration_data

# duration_data

st.subheader("Title: Frequency Distribution of Trigrams for Delayed Grievances")
wordfrequency = frequency_generator(filtereddata['CUST_FEEDBACK'])
duration_ngrams= wordfrequency[:30]
duration_freq=pd.DataFrame(duration_ngrams[0:14],columns=["Trigram","Frequency"]).sort_values(by='Frequency',ascending=True)
# duration_freq
fig = plt.figure()
fig.set_size_inches(15, 7) 
# plt.subplots_adjust(left=0.60)  # adjust plot area
plt.barh(duration_freq["Trigram"],duration_freq["Frequency"], color = "red",align='center', alpha=0.5)
plt.ylabel('Frequency of Complaints')
plt.xlabel('No of Complaints')
st.pyplot()


st.subheader("Title: Repeated complaints on same Pole Number")
# @st.cache
pole_freq=pd.DataFrame(pd.read_csv("Pole_Freq.csv"))
fig = plt.figure()
fig.set_size_inches(15, 7)
plt.barh(pole_freq["Pole_No"], pole_freq["Freq"],color="Grey")
st.pyplot()
