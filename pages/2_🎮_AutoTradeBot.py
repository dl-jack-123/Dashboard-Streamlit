# -*- coding: utf-8 -*-
"""
@author: DL
Update Time: 2025-01-25
"""
import streamlit as st
from settings import LIGHT, DARK, DEFAULT

# if 'theme_mode' not in st.session_state:
#     shutil.copy2(DARK, DEFAULT)
#     st.session_state['theme_mode'] = True

if 'df_color' not in st.session_state:
    st.session_state['df_color'] = 'DarkRed'

st.set_page_config(
    page_title='Steam Discounts Items',
    page_icon='🎮',
    layout='wide',
    initial_sidebar_state='expanded'
)
st.sidebar.success('Select a demo above to get started.')

st.markdown(
    '''
    # :rainbow[*期選自動下單系統(Windows 10+)*]
    '''
)
col1, col2 = st.columns([1, 1]) # 寬度比例
with col1:
    st.image('./source/home_overview_2.png')

with col2:
    st.markdown(f'''
        - 運用元件: PyQT5 + 卷商 API 元件
        - 下單速率: 收到報價訊息到下單完成約 < 500ms.
        - 程式運行: 24 hr.
        - 計算與呈現: 選擇權剩餘換約天數, 期貨月/週的價格差異, ... etc.
        - 採報價元件與下單元件和策略邏輯分開實現, 可快速切換不同卷商之元件.
    ''', unsafe_allow_html=True)





st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)