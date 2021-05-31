"""Page for Business Problem"""

import streamlit as st
from PIL import Image
def write():
    # creating page sections
    site_header = st.beta_container()

    with site_header:
        st.title('Twitter Hate Speech Detection')
        st.write("""
        This project aims to analyze how could AI **optimize the content moderation processes** for business and **reduce harmful effects** on human moderators [(reference)](https://imagga.com/blog/how-to-handle-content-moderation-with-the-human-factor-in-mind/)
        \n\n By using this detection app, the workload of human moderats would be reduced, so as the Negative Psychological Effects.
        Moreover, it could help the company to fulfill the requirements/ laws in different countries.
        """)
        st.image(Image.open('visualization/hatespeech.jpeg'), width = 600)
        st.image(Image.open('visualization/business_problem_1.png'), width = 600)
        st.image(Image.open('visualization/business_problem_2.png'), width = 600)
        st.image(Image.open('visualization/business_problem_3.png'), width = 600)
        st.image(Image.open('visualization/business_problem_4.png'), width = 600)
