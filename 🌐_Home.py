# -*- coding: utf-8 -*-
"""
@author: DL
Update Time: 2025-01-24
"""
import time
import numpy as np
import pandas as pd
import streamlit as st
from settings import LIGHT, DARK, DEFAULT

def stream_data(stream_strings):
    for i in stream_strings.split(' '):
        yield i + ' '
        time.sleep(0.1)

# if 'theme_mode' not in st.session_state:
#     shutil.copy2(DARK, DEFAULT)
#     st.session_state['theme_mode'] = True

if 'df_color' not in st.session_state:
    st.session_state['df_color'] = 'DarkRed'

st.set_page_config(
    page_title='DL Workspace',
    page_icon='🚀️',
    layout='wide',
    initial_sidebar_state='expanded'
)

st.sidebar.success('Select a demo above to get started.')


st.write('# :+1: :rainbow[ & _技術為工具，創造為目標_ &] :+1:')

col1, col2, col3 = st.columns([0.75, 2, 0.8]) # 寬度比例
with col1:
    st.image('./source/pic1.jpg')
with col2:
    st.markdown(f'''
    # Jack Chiu
    - Experienced to Django, FastAPI, Django Rest Framework, ... etc.
    - Experienced to Docker, Docker Swarm, ... etc.
    - Experienced to Linux, Windows, MacOS.
    - Experienced to SQL Server, MySQL, SQLite.
    - Experienced to Charting component, like echart, tradingview chart ... etc.
    - Experienced to Message Broker, like MQTT, Websocket.
    - Proficient in using Git for version control and familiar with the GitFlow workflow.
    - Baseic to PostgreSQL, MongoDB, K8S, Gitlab CI/CD, Airflow, ... etc.
    ''', unsafe_allow_html=True)

with col3:
    pass


st.markdown('### 🔎 Overview', unsafe_allow_html=True)
col1, col2 = st.columns([2, 0.75]) # 寬度比例
with col1:
    st.markdown(f'''
    ##### :blue-background[1. 🎈️Stock Daily Info]
    
        - 透過股市老師提出的邏輯，抓取上市上櫃的每日行情資料，可以選出隔日較具潛力的商品組合，減少每日花費大量時間在觀察行情走勢上
    ''', unsafe_allow_html=True)
with col2:
    st.image('./source/home_overview_1.png')

st.markdown(f'''
        ##### :blue-background[2. 🎮Auto TradeBot for Future/Option Strategy]
        ''', unsafe_allow_html=True)
col1, col2 = st.columns([0.75, 2])  # 寬度比例
with col1:
    st.image('./source/home_overview_2.png')

with col2:
    st.markdown(f'''
            - 串接及時成交明細
            - 實現期貨與選擇權的策略交易
            - 周選換倉邏輯實現
            - 斷線偵測
            - 基本帳戶資訊偵測 ... etc.
        ''', unsafe_allow_html=True)

st.markdown(f'''
        ##### :blue-background[3. 🎎Job Recommendation AI System]
        ''', unsafe_allow_html=True)

st.markdown(f'''
            利用爬蟲去抓取所有人力職缺, 搭配 LLM 推薦最適合或最容易進入面試階段的工作職缺與連結
        ''', unsafe_allow_html=True)
st.markdown("""
<style>
.rainbow-animation {
  font-size: 32px;
  font-weight: bold;
  background: linear-gradient(90deg, red, orange, yellow, green, indigo, violet);
  background-size: 400%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: rainbow 5s linear infinite;
}
@keyframes rainbow {
  100% { background-position: 100%; }
  100% { background-position: -200%; }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)
