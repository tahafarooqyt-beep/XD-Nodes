import streamlit as st
import requests

st.set_page_config(page_title="Minefort Panel", page_icon="⛏️")

st.title("⛏️ Minefort Server Manager")
st.markdown("---")

# Sidebar for Credentials
with st.sidebar:
    st.header("🔑 Credentials")
    minefort_key = st.text_input("Minefort API Key", type="password")
    server_id = st.text_input("Server ID (e.g., srv-12345)")

# API Base URL (Minefort v1)
BASE_URL = "https://api.minefort.com/v1"

def manage_server(action):
    headers = {
        "Authorization": f"Bearer {minefort_key}",
        "Content-Type": "application/json"
    }
    # Minefort API endpoint for power actions
    url = f"{BASE_URL}/server/{server_id}/power/{action}"
    
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            return True, "Success!"
        else:
            return False, f"Error {response.status_code}: {response.text}"
    except Exception as e:
        return False, str(e)

if minefort_key and server_id:
    st.success(f"Connected to Server ID: {server_id}")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🚀 Start Minefort", use_container_width=True):
            success, msg = manage_server("start")
            if success: st.balloons()
            else: st.error(msg)
            
    with col2:
        if st.button("🛑 Stop Minefort", use_container_width=True):
            success, msg = manage_server("stop")
            if success: st.warning("Server Stopping...")
            else: st.error(msg)
            
    st.markdown("---")
    if st.button("🔄 Check Status"):
        # Status fetch logic
        status_url = f"{BASE_URL}/server/{server_id}"
        headers = {"Authorization": f"Bearer {minefort_key}"}
        res = requests.get(status_url, headers=headers)
        if res.status_code == 200:
            data = res.json()
            st.json(data) # Server ki details dikhayega
else:
    st.info("👈 Please enter your Minefort API Key and Server ID in the sidebar.")
