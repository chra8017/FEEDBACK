# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 14:56:05 2022

@author: chra8017
"""

import streamlit as st
import csv
import time
from datetime import datetime    
import pytz   
import pandas as pd 
tz_india = pytz.timezone('Asia/Kolkata')
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pathlib import Path

pkl_path = Path(__file__).parents[1] / 'hotel-pos-4301021f74a6.json'

def google_connect(mood_capture_lst):
    placeholder = st.empty()
    with placeholder.success(mood_capture_lst[0]):
        scope = ['https://www.googleapis.com/auth/drive']
        st.write(pkl_path)
        cred = ServiceAccountCredentials.from_json_keyfile_name(pkl_path,scope)
        gc = gspread.authorize(cred)
        wks = gc.open("Feedback - Streamlit").worksheet('log')
        wks.append_row(mood_capture_lst)
        time.sleep(2)
        placeholder.empty()
        
def capture_emotion(mood_capture_lst):
    with open('mood_data.csv','a', newline='') as f:
        placeholder = st.empty()
        st.write(" ")
        with placeholder.success(mood_capture_lst[0]):
            writer = csv.writer(f)
            writer.writerow(mood_capture_lst)
            time.sleep(2)
            placeholder.empty()
            
def capture_write_emotion(mood_capture_lst):
    placeholder = st.empty()
    with placeholder.success(mood_capture_lst[0]):
        log_df = pd.DataFrame(columns=['Mood','Timestamp'])
        log_df.loc[:,'Mood']=[mood_capture_lst[0]]
        log_df.loc[:,'Timestamp']=[mood_capture_lst[1]]
        st.write(log_df.head())
        log_df.to_csv(f'mood_data_{mood_capture_lst[1].replace(":","_")}.csv',index=False)
        time.sleep(2)
        placeholder.empty()
    
# st.set_page_config(layout="wide")

# hide_menu_style = """
#         <style>
#         #MainMenu {visibility: hidden;}
#         </style>
#         """
# st.markdown(hide_menu_style, unsafe_allow_html=True)

# # title_st_h2 ="""<div>
# #               <h1 style="color:#FF0000;font-size:80px;text-align:center;font-weight: bold;font-family:comic sans ms">Hi, there!​</h1>
# #               </div>"""

# # st.markdown(title_st_h2,unsafe_allow_html=True)

# title_st_h3 ="""<div>
#               <h3 style="color:#FF0000;font-size:80px;text-align:center;font-weight: bold;font-family:comic sans ms">In what mood were you in when you started work today?</h3>
#               </div>"""

# st.markdown(title_st_h3,unsafe_allow_html=True)

# sad_emoji,happy_emoji,super_start_emoji = st.columns(3)

# button_st ="""<style>
#     .stButton>button {
#     color: #FFFFFF;
#     border-radius: 80%;
#     border-color: #FFFFFF;
#     height: 0em;
#     width: 0em;
#     font-size: 290px;
#     margin-top:200px;
#     text-align:center;
#     padding-left:50px;
#     margin-left:150px;
# } </style>"""

# st.markdown(button_st,unsafe_allow_html=True)

# if sad_emoji.button("😩"):
#     datetime_IN = datetime.now(tz_india)
#     capture_emotion(["Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S")])
    
# if happy_emoji.button("🙂"):
#     datetime_IN = datetime.now(tz_india)
#     capture_emotion(["Ok",datetime_IN.strftime("%Y-%m-%d %H:%M:%S")])

# if super_start_emoji.button("🤩"):
#     datetime_IN = datetime.now(tz_india)
#     capture_emotion(["Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S")])
    
if __name__ == "__main__":
    
    st.set_page_config(layout="wide")

    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    
    title_st_h3 ="""<div>
              <h3 style="color:#FF0000;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">In what mood were you in when you started work today?</h3>
              </div>"""

    st.markdown(title_st_h3,unsafe_allow_html=True)
    
    sad_emoji,happy_emoji,super_start_emoji = st.columns(3)
    
    button_st ="""<style>
        .stButton>button {
        color: #FFFFFF;
        border-radius: 80%;
        border-color: #FFFFFF;
        height: 0em;
        width: 0em;
        font-size: 120px;
        margin-top:100px;
        text-align:center;
        padding-left:00px;
        margin-left:150px;
    } </style>"""
    
    st.markdown(button_st,unsafe_allow_html=True)
    
    if sad_emoji.button("😩"):
        datetime_IN = datetime.now(tz_india)
        #capture_write_emotion(["Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S")])
        google_connect(["Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S")])
        
    if happy_emoji.button("🙂"):
        datetime_IN = datetime.now(tz_india)
        #capture_write_emotion(["Ok",datetime_IN.strftime("%Y-%m-%d %H:%M:%S")])
        google_connect(["Ok",datetime_IN.strftime("%Y-%m-%d %H:%M:%S")])
    
    if super_start_emoji.button("🤩"):
        datetime_IN = datetime.now(tz_india)
        #capture_write_emotion(["Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S")])
        google_connect(["Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S")])
        
    
