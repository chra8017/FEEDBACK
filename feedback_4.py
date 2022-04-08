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
#import pyautogui
import random
#from streamlit import caching
# from streamlit.ScriptRunner import RerunException

pkl_path = 'hotel-pos-4301021f74a6.json'

def google_connect(mood_capture_lst):
    scope = ['https://www.googleapis.com/auth/drive']
    cred = ServiceAccountCredentials.from_json_keyfile_name(pkl_path,scope)
    gc = gspread.authorize(cred)
    wks = gc.open("Feedback - Streamlit").worksheet('log')
    wks.append_row(mood_capture_lst)
        
############################# The App starts from here ########################

if __name__ == "__main__":
    
    st.set_page_config(layout="wide")

    hide_menu_style = """
         <style>
         #MainMenu {visibility: hidden;}
         </style>
         """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    
    # st.write('<style>div.Widget.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    # st_autorefresh(interval=2000,key="fizzbuzzcounter")
    
    title_st_h4 ="""<div>
              <h4 style="color:#FF0000;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">In what mood were you in when you started work today?</h4>
              </div>"""

    st.markdown(title_st_h4,unsafe_allow_html=True)
    
    sad_emoji,happy_emoji,super_star_emoji = st.columns(3)
    
    button_st ="""<style>
        .stButton>button {
        color: #FFFFFF;
        border-radius: 80%;
        border-color: #FFFFFF;
        height: 0em;
        width: 0em;
        font-size: 100px;
        margin-top:60px;
        text-align:center;
        padding-left:00px;
        margin-left:150px;
    } </style>"""
    
    st.markdown(button_st,unsafe_allow_html=True)

############################# session state for sad emoji #############    
    if "sad_button_clicked_level_1" not in st.session_state:
        st.session_state.sad_button_clicked_level_1 = False
    
    if "sad_button_clicked_level_2" not in st.session_state:
        st.session_state.sad_button_clicked_level_2 = False
    
    def callback_sad_level_1():
        st.session_state.sad_button_clicked_level_1=True
    
    def callback_sad_level_2():    
        st.session_state.sad_button_clicked_level_2 = True
############################### session state for happy emoji ############    
    if "happy_button_clicked_level_1" not in st.session_state:
        st.session_state.happy_button_clicked_level_1 = False
    
    if "happy_button_clicked_level_2" not in st.session_state:
        st.session_state.happy_button_clicked_level_2 = False
    
    def callback_happy_level_1():
        st.session_state.happy_button_clicked_level_1=True
    
    def callback_happy_level_2():    
        st.session_state.happy_button_clicked_level_2 = True
        
############################### session state for excited emoji ############    
    if "excited_button_clicked_level_1" not in st.session_state:
        st.session_state.excited_button_clicked_level_1 = False
    
    if "excited_button_clicked_level_2" not in st.session_state:
        st.session_state.excited_button_clicked_level_2 = False
    
    
    def callback_excited_level_1():
        st.session_state.excited_button_clicked_level_1=True
    
    def callback_excited_level_2():    
        st.session_state.excited_button_clicked_level_2 = True

############################# Session State for Radio Buttons ##############
    if "radio_select" not in st.session_state:
        st.session_state.radio_select = False
    
    def callback_radio_select():
        st.session_state.radio_select = True
    
    sad_button = sad_emoji.button("😩",key="12",on_click=callback_sad_level_1)
    happy_button = happy_emoji.button("🙂",key="13",on_click=callback_happy_level_1)
    super_star_button = super_star_emoji.button("🤩",key='14',on_click=callback_excited_level_1)

############################## Sad Button #####################################
    
    rand_num = random.randint(1,100000)
    
    datetime_IN = datetime.now(tz_india)
    
    if (sad_button or st.session_state.sad_button_clicked_level_1):
        
        #google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
        
        title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">What mood are you in leaving work today?</h4>
              </div>"""

        st.markdown(title_st_h4,unsafe_allow_html=True)
        
        sad_emoji_inner,happy_emoji_inner,super_star_emoji_inner = st.columns(3)
        inner_sad = sad_emoji_inner.button("😩",key="+100",on_click=callback_sad_level_2)
        happy_inner = happy_emoji_inner.button("🙂",key="++100",on_click=callback_happy_level_2) 
        excited_inner = super_star_emoji_inner.button("🤩",key="+++100",on_click=callback_excited_level_2)
        
        if (inner_sad or st.session_state.sad_button_clicked_level_2):
            
            #google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
            
            title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">From 1 to 4, how much did you enjoy what you did today?</h4>
              </div>"""
            
            st.markdown(title_st_h4,unsafe_allow_html=True)
            col1, col2, col3 , col4 = st.columns(4)
            
            option_1 = col1.button("1️⃣",on_click=callback_radio_select)
            option_2 = col2.button("2️⃣",on_click=callback_radio_select)
            option_3 = col3.button("3️⃣",on_click=callback_radio_select)
            option_4 = col4.button("4️⃣",on_click=callback_radio_select)
            
            if option_1:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",1,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_2:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",2,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_3:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",3,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_4:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",4,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
                
        elif (happy_inner or st.session_state.happy_button_clicked_level_2):
            
            title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">From 1 to 4, how much did you enjoy what you did today?</h3>
              </div>"""
            
            st.markdown(title_st_h4,unsafe_allow_html=True)
            
            col1, col2, col3 , col4 = st.columns(4)
            
            option_1 = col1.button("1️⃣",on_click=callback_radio_select)
            option_2 = col2.button("2️⃣",on_click=callback_radio_select)
            option_3 = col3.button("3️⃣",on_click=callback_radio_select)
            option_4 = col4.button("4️⃣",on_click=callback_radio_select)
            
            if option_1:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",1,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_2:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",2,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_3:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",3,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_4:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",4,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
        
        elif (excited_inner or st.session_state.excited_button_clicked_level_2):
            
            title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">From 1 to 4, how much did you enjoy what you did today?</h3>
              </div>"""
            
            st.markdown(title_st_h4,unsafe_allow_html=True)
            
            col1, col2, col3 , col4 = st.columns(4)
            
            option_1 = col1.button("1️⃣",on_click=callback_radio_select)
            option_2 = col2.button("2️⃣",on_click=callback_radio_select)
            option_3 = col3.button("3️⃣",on_click=callback_radio_select)
            option_4 = col4.button("4️⃣",on_click=callback_radio_select)
            
            if option_1:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",1,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_2:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",2,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_3:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",3,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_4:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",4,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
    
############################## Happy Button ###################################
    
    elif (happy_button or st.session_state.happy_button_clicked_level_1):
        
        title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">What mood are you in leaving work today?</h3>
              </div>"""

        st.markdown(title_st_h4,unsafe_allow_html=True)
        
        sad_emoji_inner,happy_emoji_inner,super_star_emoji_inner = st.columns(3)
        inner_sad = sad_emoji_inner.button("😩",key="+100",on_click=callback_sad_level_2)
        happy_inner = happy_emoji_inner.button("🙂",key="++100",on_click=callback_happy_level_2) 
        excited_inner = super_star_emoji_inner.button("🤩",key="+++100",on_click=callback_excited_level_2)
        
        if (inner_sad or st.session_state.sad_button_clicked_level_2):
            
            title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">From 1 to 4, how much did you enjoy what you did today?</h3>
              </div>"""
            
            st.markdown(title_st_h4,unsafe_allow_html=True)
            
            col1, col2, col3 , col4 = st.columns(4)
            
            option_1 = col1.button("1️⃣",on_click=callback_radio_select)
            option_2 = col2.button("2️⃣",on_click=callback_radio_select)
            option_3 = col3.button("3️⃣",on_click=callback_radio_select)
            option_4 = col4.button("4️⃣",on_click=callback_radio_select)
            
            if option_1:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",1,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_2:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",2,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_3:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",3,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_4:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",4,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
                
        elif (happy_inner or st.session_state.happy_button_clicked_level_2):
            
            title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">From 1 to 4, how much did you enjoy what you did today?</h3>
              </div>"""
            
            st.markdown(title_st_h4,unsafe_allow_html=True)
            col1, col2, col3 , col4 = st.columns(4)
            
            option_1 = col1.button("1️⃣",on_click=callback_radio_select)
            option_2 = col2.button("2️⃣",on_click=callback_radio_select)
            option_3 = col3.button("3️⃣",on_click=callback_radio_select)
            option_4 = col4.button("4️⃣",on_click=callback_radio_select)
            
            if option_1:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",1,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
                
            
            elif option_2:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",2,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_3:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",3,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_4:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",4,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
        
        elif (excited_inner or st.session_state.excited_button_clicked_level_2):
            
            title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">From 1 to 4, how much did you enjoy what you did today?</h3>
              </div>"""
            
            st.markdown(title_st_h4,unsafe_allow_html=True)
            col1, col2, col3 , col4 = st.columns(4)
            
            option_1 = col1.button("1️⃣",on_click=callback_radio_select)
            option_2 = col2.button("2️⃣",on_click=callback_radio_select)
            option_3 = col3.button("3️⃣",on_click=callback_radio_select)
            option_4 = col4.button("4️⃣",on_click=callback_radio_select)
            
            if option_1:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",1,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_2:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",2,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_3:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",3,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_4:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",4,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
    
############################ super excited ####################################
    
    elif (super_star_button or st.session_state.excited_button_clicked_level_1):
        
        title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">What mood are you in leaving work today?</h3>
              </div>"""

        st.markdown(title_st_h4,unsafe_allow_html=True)
        
        sad_emoji_inner,happy_emoji_inner,super_star_emoji_inner = st.columns(3)
        inner_sad = sad_emoji_inner.button("😩",key="+100",on_click=callback_sad_level_2)
        happy_inner = happy_emoji_inner.button("🙂",key="++100",on_click=callback_happy_level_2) 
        excited_inner = super_star_emoji_inner.button("🤩",key="+++100",on_click=callback_excited_level_2)
        
        if (inner_sad or st.session_state.sad_button_clicked_level_2):
            
            title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">From 1 to 4, how much did you enjoy what you did today?</h3>
              </div>"""
            
            st.markdown(title_st_h4,unsafe_allow_html=True)
            col1, col2, col3 , col4 = st.columns(4)
            
            option_1 = col1.button("1️⃣",on_click=callback_radio_select)
            option_2 = col2.button("2️⃣",on_click=callback_radio_select)
            option_3 = col3.button("3️⃣",on_click=callback_radio_select)
            option_4 = col4.button("4️⃣",on_click=callback_radio_select)
            
            if option_1:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",1,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_2:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",2,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_3:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",3,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_4:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Bad",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",4,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
                
        
        elif (happy_inner or st.session_state.happy_button_clicked_level_2):
            
            title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">From 1 to 4, how much did you enjoy what you did today?</h3>
              </div>"""
            
            st.markdown(title_st_h4,unsafe_allow_html=True)
            col1, col2, col3 , col4 = st.columns(4)
            
            option_1 = col1.button("1️⃣",on_click=callback_radio_select)
            option_2 = col2.button("2️⃣",on_click=callback_radio_select)
            option_3 = col3.button("3️⃣",on_click=callback_radio_select)
            option_4 = col4.button("4️⃣",on_click=callback_radio_select)
            
            if option_1:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",1,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_2:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",2,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_3:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",3,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_4:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Happy",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",4,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
        
        elif (excited_inner or st.session_state.excited_button_clicked_level_2):
            
            title_st_h4 ="""<div>
              <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">From 1 to 4, how much did you enjoy what you did today?</h3>
              </div>"""
            
            st.markdown(title_st_h4,unsafe_allow_html=True)
            col1, col2, col3 , col4 = st.columns(4)
            
            option_1 = col1.button("1️⃣",on_click=callback_radio_select)
            option_2 = col2.button("2️⃣",on_click=callback_radio_select)
            option_3 = col3.button("3️⃣",on_click=callback_radio_select)
            option_4 = col4.button("4️⃣",on_click=callback_radio_select)
            
            if option_1:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",1,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_2:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",2,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_3:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",3,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])

                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
            
            elif option_4:
                title_st_h4 ="""<div>
                  <h4 style="color:#FF0000;margin-top:60px;font-size:40px;text-align:center;font-weight: bold;font-family:comic sans ms">Thank you🙂</h3>
                  </div>"""
                st.markdown(title_st_h4,unsafe_allow_html=True)
                google_connect(["Q1","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q2","Excited",datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                google_connect(["Q3",4,datetime_IN.strftime("%Y-%m-%d %H:%M:%S"),rand_num])
                
                for key in st.session_state.keys():
                    del st.session_state[key]
                raise st.experimental_rerun()
    
