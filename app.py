import streamlit as st
import requests

st.set_page_config(page_title="Taha's Minehut Manager", page_icon="⛏️")

st.title("⛏️ Minehut Server Control")
st.info("No 503 Errors - Direct API Access")

# User Input
server_name = st.text_input("Enter your Minehut Server Name (e.g., TahaNodes)", "TahaNodes")

if server_name:
    # Minehut API call
    url = f"https://api.minehut.com/server/{server_name}?byName=true"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            server = data['server']
            
            # Status Metrics
            is_online = server['online']
            st.subheader(f"📍 {server['name'].upper()}")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Status", "🟢 Online" if is_online else "🔴 Offline")
            col2.metric("Players", f"{server['playerCount']}/{server['maxPlayers']}")
            col3.metric("MOTD", server['motd'])

            st.markdown("---")
            
            # Additional Info
            with st.expander("Detailed Server Info"):
                st.write(f"**IP Address:** {server['name']}.minehut.gg")
                st.write(f"**Platform:** {server['server_version_type']}")
                st.write(f"**Active Plugins:** {len(server['active_plugins'])}")

        else:
            st.error("Server not found! Make sure the name is correct.")
    except Exception as e:
        st.error(f"Connection Error: {e}")

st.caption("Note: Free servers hibernate when empty but auto-start on join.")
