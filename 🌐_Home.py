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
col1, col2 = st.columns([2, 0.75])  # 寬度比例
with col1:
    st.markdown(f'''
                [進行中]利用爬蟲去抓取所有人力職缺, 搭配 LLM 推薦最適合或最容易進入面試階段的工作職缺與連結
            ''', unsafe_allow_html=True)

with col2:
    st.image('./source/in_process.png', width=300)

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

st.markdown(f'''
        ##### :blue-background[4. 🎈️AI Role with Telegram]
        ''', unsafe_allow_html=True)
col1, col2 = st.columns([0.75, 2])  # 寬度比例
with col1:
    st.image('./source/home_overview_4.png')

with col2:
    st.markdown(f'''
            - 透過預訓練好的角色模型，可以透過 Telegram Bot 進行角色的設定、互動等
            - 了解 gemini API 基本串接
            - 簡易使用者操作介面(tg)來呈現互動
            
        ''', unsafe_allow_html=True)

st.markdown(f'''
        ##### :blue-background[5. 🎈️客服小幫手 with Line Bot]
        ''', unsafe_allow_html=True)
col1, col2 = st.columns([2, 0.75])  # 寬度比例
with col2:
    st.image('./source/home_overview_5.png')

with col1:
    st.markdown(f'''
            - 目的:利用已建立好的 Q&A 的方式，加上 RAG (增加檢索功能)，達成 AI 小幫手的功能
            1. 文檔知識庫建立：
                - 使用 TextLoader 載入文本文件（qa.txt 和 prompt.txt）
                - 通過 RecursiveCharacterTextSplitter 將文檔切分成較小的文本塊
                - 使用 HuggingFace 的 "all-MiniLM-L6-v2" 模型進行文本嵌入
                - 利用 FAISS 向量數據庫存儲文檔的向量表示
            2. 智能問答系統：
                - 整合了 Google 的 Gemini-2.0-pro-exp 大語言模型
                - 使用 RetrievalQA 鏈實現基於檢索的問答功能
                - 當用戶提問時，系統會：
                    - 從 FAISS 向量庫中檢索相關文檔片段
                    - 結合檢索到的上下文，使用 Gemini 生成答案
            3. Line Bot 整合：
                - 通過 Line Bot 介面接收用戶訊息
                - 將用戶問題傳遞給 RAG 系統處理
                - 將 RAG 系統生成的回答通過 Line Bot 發送給用戶
                - 同時記錄用戶資訊和對話歷史到數據庫中

        ''', unsafe_allow_html=True)

st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)
