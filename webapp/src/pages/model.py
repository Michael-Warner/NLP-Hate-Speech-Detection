"""Page for Predictive Model"""

import streamlit as st
from PIL import Image
def write():
    site_header = st.beta_container()

    with site_header:
        st.title('Predictive Model')
        st.write("""
        Baseline models included Random Forest, Naive Bayes, Logistic Regression, Support Vector Machine (SVM) and Neural Network. The final model was a **SVM** model that used TFIDF Vectorization for feature engineering. It produced an F1 of 0.89 and Recall (TPR) of 0.92.  
        """)

    st.text('')
    st.image(Image.open('visualization/svm_model.png'), width = 400)