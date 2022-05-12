import streamlit as st
import os
import numpy as np
import pandas as pd
import urllib.request
from PIL import Image
import glob

def update_params():
    st.experimental_set_query_params(challenge=st.session_state.day)

md_files = sorted([int(x.strip('Day').strip('.md')) for x in glob.glob1('content',"*.md") ])

# Logo and Navigation
col1, col2, col3 = st.columns((1,4,1))
with col2:
    st.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
st.markdown('# 30 วันแห่ง Streamlit')

days_list = [f'Day {x}' for x in md_files]

query_params = st.experimental_get_query_params()

if query_params and query_params["challenge"][0] in days_list:
    st.session_state.day = query_params["challenge"][0]

selected_day = st.selectbox('เริ่มต้นการเรียนรู้ 👇', days_list, key="day", on_change=update_params)

with st.expander("เกี่ยวกับ #30DaysOfStreamlit"):
    st.markdown('''
    **30 วันแห่ง Streamlit** (**30DaysOfStreamlit**) เป็นกิจกรรมการเรียนรู้ที่ออกแบบมาเพื่อช่วยให้คุณเรียนรู้และเริ่มต้นสร้างแอพด้วย Streamlit
    
    นี่คือสิ่งที่คุณจะได้เรียนรู้
    - Set up a coding environment for building Streamlit apps
    - Build your first Streamlit app
    - Learn about all the awesome input/output widgets to use for your Streamlit app
    ''')

# Sidebar
st.sidebar.header('เกี่ยวกับ')
st.sidebar.markdown('[Streamlit](https://streamlit.io) เป็นไพธอนไลบรารีสำหรับการเขียนเว็บแอปที่มีความสามารถในการขับเคลื่อนด้วยข้อมูลโดยไม่จำเป็นต้องมีความรู้เกี่ยวกับ HTML, CSS และ Javascript')

st.sidebar.header('แหล่งทรัพยากรการเรียนรู้')
st.sidebar.markdown('''
- [เอกสารอ้างอิงของ Streamlit](https://docs.streamlit.io/)
- [ใบสรุปคำสั่งทั้งหมดของ Streamlit](https://docs.streamlit.io/library/cheatsheet)
- [หนังสือ](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
- [บทความบล็อก](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
''')

st.sidebar.header('นำแอพลงเว็บ')
st.sidebar.markdown('คุณสามารถนำเว็บแอปที่เขียนด้วย Streamlit ไปแขวนบนเว็บโดยใช้ [Streamlit Cloud](https://streamlit.io/cloud) ในเพียงไม่กี่คลิก')

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f'# 🗓️ {i}')
        j = i.replace(' ', '')
        with open(f'content/{j}.md', 'r') as f:
            st.markdown(f.read())
        if os.path.isfile(f'content/figures/{j}.csv') == True:
            st.markdown('---')
            st.markdown('### รูปภาพ')
            df = pd.read_csv(f'content/figures/{j}.csv', engine='python')
            for i in range(len(df)):
                st.image(f'content/images/{df.img[i]}')
                st.info(f'{df.figure[i]}: {df.caption[i]}')
