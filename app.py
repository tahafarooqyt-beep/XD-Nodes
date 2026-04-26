import streamlit as st
from python_aternos import Client
import time

# Page Configuration
st.set_page_config(page_title="XD-Nodes Control", page_icon="🎮", layout="centered")

st.title("🎮 XD-Nodes Aternos Panel")
st.markdown("---")

# 1. Secure Login using Streamlit Secrets
try:
    USER = st.secrets["AT_USER"]
    PASS = st.secrets["AT_PASS"]
except KeyError:
    st.error("❌ Secrets not found! Go to Advanced Settings > Secrets and add AT_USER and AT_PASS.")
    st.stop()

# 2. Initialize Connection
if "at" not in st.session_state:
    try:
        at = Client.from_credentials(USER, PASS)
        st.session_state.at = at
        st.success("✅ Connected to Aternos!")
    except Exception as e:
        st.error(f"❌ Login Failed: {e}")
        st.stop()

at = st.session_state.at

# 3. Server Selection
try:
    servers = at.list_servers()
    # Select the first server by default
    serv = servers[0]
except Exception as e:
    st.error("❌ No servers found in this account.")
    st.stop()

# 4. Dashboard UI
st.subheader(f"📍 Server: {serv.address}")
status_color = "🟢" if serv.status == "online" else "🔴"
st.write(f"**Current Status:** {status_color} {serv.status.upper()}")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🚀 Start Server", use_container_width=True):
        try:
            serv.start()
            st.toast("Starting server...")
            time.sleep(2)
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")

with col2:
    if st.button("🛑 Stop Server", use_container_width=True):
        try:
            serv.stop()
            st.toast("Stopping server...")
            time.sleep(2)
            st.rerun()
        except Exception as e:
            st.error(f"Error: {e}")

with col3:
    if st.button("🔄 Refresh Status", use_container_width=True):
        st.rerun()

st.markdown("---")

# 5. Console & Logs
with st.expander("📝 View Server Logs"):
    if st.button("Fetch Latest Logs"):
        log = serv.get_log()
        if log:
            st.code(log, language="text")
        else:
            st.info("No logs available right now.")

with st.expander("💻 Send Command"):
    cmd = st.text_input("Enter command (e.g. /op Taha)")
    if st.button("Send"):
        if cmd:
            serv.send_command(cmd)
            st.success(f"Command '{cmd}' sent!")
        else:
            st.warning("Please enter a command first.")

# Footer
st.caption("Powered by XD-Nodes | 24/7 Streamlit Hosting")
