import streamlit as st
from python_aternos import Client
import time

st.set_page_config(page_title="Taha's MC Panel", page_icon="🎮")

st.title("🎮 Aternos Control Panel")
st.write("Manual Login Mode")

# Login UI in Sidebar or Main Page
with st.sidebar:
    st.header("🔑 Aternos Login")
    user_input = st.text_input("Username", placeholder="Taha_123")
    pass_input = st.text_input("Password", type="password")
    login_btn = st.button("Connect to Aternos")

if login_btn:
    if user_input and pass_input:
        try:
            # Login process
            at = Client.from_credentials(user_input, pass_input)
            st.session_state.at = at
            st.success("✅ Connected Successfully!")
        except Exception as e:
            st.error(f"❌ Login Failed: {e}")
            if "503" in str(e):
                st.info("Aternos is blocking the script. Try logging into Aternos.org on your phone first.")
    else:
        st.warning("Please enter both Username and Password.")

# Dashboard Logic
if "at" in st.session_state:
    at = st.session_state.at
    try:
        serv = at.list_servers()[0]
        
        st.divider()
        st.subheader(f"📍 Server: {serv.address}")
        st.write(f"**Status:** {serv.status.upper()}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🚀 Start Server", use_container_width=True):
                serv.start()
                st.toast("Starting...")
                time.sleep(2)
                st.rerun()
        
        with col2:
            if st.button("🛑 Stop Server", use_container_width=True):
                serv.stop()
                st.toast("Stopping...")
                time.sleep(2)
                st.rerun()

        with st.expander("📝 Server Logs"):
            if st.button("Fetch Logs"):
                st.code(serv.get_log())

    except Exception as e:
        st.error(f"Could not fetch server: {e}")

else:
    st.info("👈 Please enter your credentials in the sidebar to start.")
