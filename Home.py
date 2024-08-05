import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Home")

st.markdown("""
Welcome to Launchpad!

This application was built so that I can showcase my experience with :red[Streamlit] and various :rainbow[Automation Frameworks].
""")

col1, col2 = st.columns(2)

with col1:
    containerLaunchpad = st.container(border=True)
    containerLaunchpad.page_link("pages/Launchpad.py", label="Launchpad", icon="🚀")

with col2:
    containerPlayground = st.container(border=True)
    containerPlayground.page_link("pages/Playground.py", label="Playground", icon="🧱")

st.sidebar.markdown("© 2024 Christopher Zeuch. All rights reserved.")