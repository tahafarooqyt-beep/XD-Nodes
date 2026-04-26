import streamlit as st
from python_aternos import Client

st.set_page_config(page_title="Taha's Pro Panel", layout="wide")

# Session state to keep login active
if "at" not in st.session_state:
    st.session_state.at = None

with st.sidebar:
    st.title("Admin Login")
    u = st.text_input("Aternos User")
    p = st.text_input("Aternos Pass", type="password")
    if st.button("Connect"):
        try:
            st.session_state.at = Client.from_credentials(u, p)
            st.success("Connected!")
        except Exception as e:
            st.error(f"Failed: {e}")

if st.session_state.at:
    at = st.session_state.at
    # Pehla server select karein
    serv = at.list_servers()[0]

    tab1, tab2, tab3 = st.tabs(["🎮 Console & Control", "📁 File Browser", "⚙️ Server Settings"])

    # --- TAB 1: CONSOLE & CONTROL ---
    with tab1:
        col1, col2 = st.columns([1, 1])
        with col1:
            if st.button("🚀 Start Server", use_container_width=True):
                serv.start()
            if st.button("🛑 Stop Server", use_container_width=True):
                serv.stop()
        
        with col2:
            st.write(f"**Status:** {serv.status}")
            st.write(f"**IP:** {serv.address}")

        st.divider()
        st.subheader("Remote Console")
        cmd = st.text_input("Send Command to Server")
        if st.button("Send Command"):
            serv.send_command(cmd)
            st.success(f"Sent: {cmd}")
        
        if st.button("View Full Logs"):
            st.code(serv.get_log(), language="text")

    # --- TAB 2: FILES ---
    with tab2:
        st.subheader("Files List")
        path = st.text_input("Folder Path", value="/")
        try:
            files = serv.list_files(path)
            for f in files:
                type_icon = "📁" if f.is_dir else "📄"
                st.write(f"{type_icon} {f.name}")
        except:
            st.error("Cannot access files via API.")

    # --- TAB 3: SETTINGS (CRACKED) ---
    with tab3:
        st.subheader("Server Configuration")
        # Note: Ye features Aternos ke API version par depend karte hain
        st.info("To change Cracked/Online Mode, use the Aternos Website. This API currently supports Start/Stop/Console.")

else:
    st.info("Please login to see the dashboard.")