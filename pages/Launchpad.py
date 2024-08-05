import time
import streamlit as st

st.set_page_config(
    page_title="Launchpad",
    page_icon="🚀",
    layout="wide"
)

if 'history' not in st.session_state:
    st.session_state.history = []

if 'rerun_index' not in st.session_state:
    st.session_state.rerun_index = None

containerLaunchpad = st.container()

with containerLaunchpad:
    st.title("🚀 Launchpad")

    col1, col2, col3, col4 = st.columns(4)

    def update_history(button_text, command_text, is_rerun=False):
        if is_rerun:
            button_text = f"🔄 {button_text}"
        st.session_state.history.insert(0, (button_text, command_text))

    def run_seleniumbase_pass(is_rerun=False):
        command_text = "pytest fake_pass.py --headless"
        update_history("🐉 SeleniumBase | Run Pass", command_text, is_rerun)

    def run_seleniumbase_fail(is_rerun=False):
        command_text = "pytest fake_fail.py --headless"
        update_history("🐉 SeleniumBase | Run Fail", command_text, is_rerun)

    with col1:
        containerCypress = st.container(border=True)
        with containerCypress:
            st.subheader("🌴 Cypress")
            st.button("Coming soon", use_container_width=True, disabled=True, key="cypress_tba")

    with col2:
        containerPlaywright = st.container(border=True)
        with containerPlaywright:
            st.subheader("🎭 Playwright")
            st.button("Coming soon", use_container_width=True, disabled=True, key="playwright_tba")

    with col3:
        containerSelenium = st.container(border=True)
        with containerSelenium:
            st.subheader("🧪 Selenium")
            st.button("Coming soon", use_container_width=True, disabled=True, key="selenium_tba")

    with col4:
        containerSeleniumBase = st.container(border=True)
        with containerSeleniumBase:
            st.subheader("🐉 SeleniumBase")

            col1Cypress, col2Cypress = st.columns(2)
            with col1Cypress:
                if st.button("Run Pass", use_container_width=True, key="seleniumbase_pass"):
                    with st.spinner('Executing ...'):
                        time.sleep(2)
                    st.success("🟢 Executed")
                    run_seleniumbase_pass()
            with col2Cypress:
                if st.button("Run Fail", type="primary", use_container_width=True, key="seleniumbase_fail"):
                    with st.spinner('Executing ...'):
                        time.sleep(2)
                    st.error("🔴 Executed")
                    run_seleniumbase_fail()

containerCommand = st.container(border=True)
with containerCommand:
    st.subheader("✨ Result")
    st.text_area("Result", value="", label_visibility="collapsed", disabled=True, placeholder="Functionality coming soon")

containerHistory = st.container(border=True)
with containerHistory:
    st.subheader("🧠 History")

    if st.button("Clear", type="primary"):
        st.session_state.history = []

    col1History, col2History, col4History = st.columns([1, 2, 1])

    for index, (button_text, command_text) in enumerate(st.session_state.history):
        with col1History:
            button_type = "primary" if "Fail" in button_text else "secondary"
            st.button(button_text, use_container_width=True, key=f"col1HistoryResult_{index}", type=button_type)

        with col2History:
            st.text_input("command_text", command_text, key=f"col2HistoryResult_{index}", label_visibility="collapsed")

        with col4History:
            if st.button("Re-run", use_container_width=True, key=f"col4HistoryResult_run_{index}"):
                st.session_state.rerun_index = index

    if st.session_state.rerun_index is not None:
        index = st.session_state.rerun_index
        button_text, _ = st.session_state.history[index]
        if "SeleniumBase | Run Pass" in button_text:
            run_seleniumbase_pass(is_rerun=True)
        elif "SeleniumBase | Run Fail" in button_text:
            run_seleniumbase_fail(is_rerun=True)
        st.session_state.rerun_index = None
        st.rerun()

st.sidebar.markdown("© 2024 Christopher Zeuch. All rights reserved.")