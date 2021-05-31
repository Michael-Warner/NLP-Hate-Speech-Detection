"""Main module for the streamlit app"""

import streamlit as st
import src.pages.eda
import src.pages.app
import src.pages.intro
import src.pages.model


PAGES = {
    "App": src.pages.app,
    "Business Problem": src.pages.intro,
    "EDA": src.pages.eda,
    "Model": src.pages.model,
}


def main():
    """Main function of the App"""
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.write()
   
    with st.spinner(f"Loading {selection} ..."):
        st.sidebar.title("About")
        st.sidebar.info(
            "This app is maintained by **MSc Artificial Intelligence and Business Analytics students** from Toulouse Business School, France. \n\n"
            "Check out the project repository [here](https://github.com/jingfei-x/AI-and-Big-Data-Project-Hate-Speech-)"
    )
    st.error("**WARNING:** *The data, lexicons, and notebooks all contain content that is racist, sexist, homophobic, and offensive in many other ways.*") 


if __name__ == "__main__":
    main()