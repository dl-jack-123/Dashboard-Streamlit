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
    page_title='Side Project',
    page_icon='📋',
    layout='wide',
    initial_sidebar_state='expanded'
)
st.sidebar.success('Select a demo above to get started.')

st.markdown(
    '''
    # :rainbow[*Coming Soon ...*]
    '''
)

st.markdown('<br><br><br>', unsafe_allow_html=True)
st.caption('<div style="text-align: center"> Streamlit is simply an artifact for Data Scientist.</div>', unsafe_allow_html=True)