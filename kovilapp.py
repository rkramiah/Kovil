import numpy as np
import pandas as pd
import openpyxl as xl

import streamlit as st
from PIL import Image

#st.sidebar.title("Side Bar")

col7,col8 = st.columns(2)

with col7:
    image = Image.open('MTNACafeLogo.png')
    st.image(image, caption='Om Muruga!!')


with col8:
    image = Image.open('Operation_banner.jpg')
    st.image(image, caption='Om Muruga!!')





df_as = pd.read_excel("appetizer.xlsx")
#df_as.set_index('appetizers_snacks')

df_md = pd.read_excel("main.xlsx")
#df_md = df_md.rename(columns={'main_dishes' : "Main Dish"})
df_md=df_md[:].round()

df_rd = pd.read_excel("rice.xlsx")
#df_rd.set_index('rice_dishes')



# display the checkbox in a column format    
col1, col2, col3 =st.columns(3)


#implement filters water_sources and water_tech
with col1:
    as_ = st.multiselect(label="Appetizer and Snacks",
                  options = df_as.appetizers_snacks.unique())
    checkbox_as =st.checkbox("Check box Appetizer")
    
with col2:
    md_ = st.multiselect(label="Main Dishes",
                  options = df_md.main_dishes.unique())
    checkbox_md =st.checkbox("Check box Main Dish")
    
with col3:
    rd_ = st.multiselect(label="Rice Dishes",
                  options = df_rd.rice_dishes.unique())
    checkbox_rd =st.checkbox("Check box Rice")    
    
    
    
    #filtering and connecting the checkbox to the data
if checkbox_as:
    filter_ = df_as.appetizers_snacks.apply(lambda x: x in as_)
    df_as = df_as[filter_].copy()
    
if checkbox_md:
    filter_ = df_md.main_dishes.apply(lambda x: x in md_)
    df_md = df_md[filter_].copy()
    
if checkbox_rd:
    filter_ = df_rd.rice_dishes.apply(lambda x: x in rd_)
    df_rd = df_rd[filter_].copy()
    


col4, col5, col6= st.columns(3)

with col4:
    st.table(df_as)
with col5:
    st.table(df_md)
with col6:
    st.table(df_rd)
      