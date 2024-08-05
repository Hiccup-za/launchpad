import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(
    page_title="Playground",
    page_icon="🧱",
    layout="wide"
)

st.title("🧱 Playground")

containerRadio = st.container(border=True)
with containerRadio:

    st.header("💬 Text elements")
    col1, col2 = st.columns(2)
    with col1:
        
        if st.button("Clear", type="primary", key="clear_text"):
            st.session_state.text_element = None

        text_element = st.radio("Select text element:", [
            "Display :red[Title]",
            "Display :orange[Header]",
            "Display :violet[Subheader]",
            "Display :rainbow[Markdown]",
            "Display :blue[Caption]",
            "Display :green[LaTeX]",
            "Display :grey[Code Block]"
        ], label_visibility="collapsed", index=None, key="text_element")

    with col2:
        if text_element == "Display :red[Title]":
            st.title(":red[This is a red Title]")
        elif text_element == "Display :orange[Header]":
            st.header(":orange[This is an orange Header]")
        elif text_element == "Display :violet[Subheader]":
            st.subheader(":violet[This is a violet Subheader]")
        elif text_element == "Display :rainbow[Markdown]":
            st.markdown(":rainbow[This is Markdown text with rainbow colors]")
        elif text_element == "Display :blue[Caption]":
            st.caption(":blue[This is a blue Caption]")
        elif text_element == "Display :green[LaTeX]":
            st.latex(r'''
                a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
                \sum_{k=0}^{n-1} ar^k =
                a \left(\frac{1-r^{n}}{1-r}\right)
                ''')
        elif text_element == "Display :grey[Code Block]":
            st.code("This is a Code Block", language="markdown")

containerStatus = st.container(border=True)
with containerStatus:
    st.header("🚦 Status elements")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Clear", type="primary", key="clear_status"):
            st.session_state.status_element = None

        status_element = st.radio("Select status element:", [
            "📊 Progress bar ",
            "🔄 Spinner ",
            "📦 Status container ",
            "🍞 Toast ",
            "📢 Callouts ",
            "🎈 Balloons ",
            "❄️ Snowflakes "
        ], label_visibility="collapsed", index=None, key="status_element")

    with col2:
        if status_element == "📊 Progress bar ":
            progress_text = "Operation in progress. Please wait ..."
            my_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.03)
                my_bar.progress(percent_complete + 1, text=progress_text)
            time.sleep(1)
            my_bar.empty()
            st.button("Rerun")
        elif status_element == "🔄 Spinner ":
            with st.spinner('Wait for it...'):
                time.sleep(3)
            st.success("Success!")
        elif status_element == "📦 Status container ":
            with st.status("Downloading data..."):
                st.write("Searching for data...")
                time.sleep(2)
                st.write("Found URL.")
                time.sleep(1)
                st.write("Downloading data...")
                time.sleep(1)
            st.button("Rerun")
        elif status_element == "🍞 Toast ":
            def cook_breakfast():
                msg = st.toast('Gathering ingredients...', icon='🥚')
                time.sleep(1)
                msg.toast('Cooking...', icon='🍳')
                time.sleep(1)
                msg.toast('Ready!', icon='🥞')

            def celebrate():
                st.toast('Hip!', icon='🎉')
                time.sleep(0.5)
                st.toast('Hip!', icon='🎂')
                time.sleep(0.5)
                st.toast('Hooray!', icon='🥳')

            col1, col2 = st.columns(2)
            if col1.button('Cook breakfast'):
                cook_breakfast()
            if col2.button('Three cheers'):
                celebrate()

        elif status_element == "📢 Callouts ":
            st.info("This is an informational callout")
            time.sleep(1)
            st.warning("This is a warning callout")
            time.sleep(1)
            st.error("This is an error callout")
            time.sleep(1)
            st.success("This is a success callout")
        elif status_element == "🎈 Balloons ":
            st.balloons()
        elif status_element == "❄️ Snowflakes ":
            st.snow()

containerCharts = st.container(border=True)
with containerCharts:

    containerChartsButtons = st.container()
    with containerChartsButtons:

        st.header("📊 Chart elements")
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            clear_button = st.button("Clear", type="primary", key="clear_charts")
        with col2:
            area_button = st.button("Display Area chart")
        with col3:
            bar_button = st.button("Display Bar chart")
        with col4:
            line_button = st.button("Display Line chart")
        with col5:
            scatter_button = st.button("Display Scatter chart")
    
    containerChartsOutput = st.container()
    with containerChartsOutput:
        chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
        if clear_button:
            st.empty()
        elif area_button:
            st.subheader("Area chart")
            st.area_chart(chart_data)
        elif bar_button:
            st.subheader("Bar chart")
            st.bar_chart(chart_data)
        elif line_button:
            st.subheader("Line chart")
            st.line_chart(chart_data)
        elif scatter_button:
            st.subheader("Scatter chart")
            st.scatter_chart(chart_data)
        else:
            st.empty()

containerData = st.container(border=True)
with containerData:
    
    containerDataButtons = st.container()
    with containerDataButtons:
        st.header("💽 Data elements")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            clear_button = st.button("Clear", type="primary", key="clear_data")
        with col2:
            dataframe_button = st.button("Display Dataframe")
        with col3:
            static_table_button = st.button("Display Static table")
        with col4:
            metrics_button = st.button("Display Metrics")

    containerDataOutput = st.container()
    with containerDataOutput:
        df = pd.DataFrame(np.random.randn(10, 10), columns=("col %d" % i for i in range(10)))
        if clear_button:
            st.empty()
        elif dataframe_button:
            st.subheader("Dataframe")
            st.dataframe(df)
        elif static_table_button:
            st.subheader("Static table")
            st.table(df)
        elif metrics_button:
            st.subheader("Metrics")
            col1, col2, col3 = st.columns(3)
            col1.metric("Temperature", "70 °F", "1.2 °F")
            col2.metric("Wind", "9 mph", "-8%")
            col3.metric("Humidity", "86%", "4%")
        else:
            st.empty()