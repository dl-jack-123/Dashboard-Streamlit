# -*- coding: utf-8 -*-
"""
@author: DL
Update Time: 2025-01-25
"""
import json
import numpy as np
import pandas as pd
import streamlit as st
from settings import LIGHT, DARK, DEFAULT


if 'df_color' not in st.session_state:
    st.session_state['df_color'] = 'DarkRed'

st.set_page_config(
    page_title='Stock Daily Info',
    page_icon='🎈️',
    layout='wide',
    initial_sidebar_state='expanded'
)
st.sidebar.success('Select a demo above to get started.')

st.markdown(
    '''
    # :rainbow[*Stock Daily Info*]
    '''
)

col1, col2 = st.columns([1, 1]) # 寬度比例
with col1:
    st.image('./source/home_overview_1.png')

with col2:
    st.markdown(f'''
        - 資料來源: 證交所/櫃買中心
        - 系統: 雲端虛擬主機(sugar) + nginx + Django + SQL Server
        - 內容: 依照 20 + 的不同選股條件所挑選出來股票，隔日漲的趨勢較為明顯
        - 廣告: 依照會員與非會員的權限, 呈現是否顯示廣告
    ''', unsafe_allow_html=True)


col1, col2 = st.columns([1, 1]) # 寬度比例
with col1:
    st.image('./source/page_charting.png')

with col2:
    st.markdown(f'''
        - 透過 tradingview 的 LightWeight Charts 套件，可以快速的繪製出股票的走勢圖
        - 自選功能: 可把關注股票加入群組, 供後續快速追蹤走勢
        - 不同週期的資料切換
    ''', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1]) # 寬度比例
with col1:
    st.image('./source/page_member_charting.png')

with col2:
    st.markdown(f'''
        - 透過會員瀏覽統計, 每天約 50-100 瀏覽次數
        
    ''', unsafe_allow_html=True)


st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)