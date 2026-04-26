import streamlit as st
import os
import subprocess
import requests

st.title("🖥️ Taha Pro Nodes")

# 1. Server Download Function (Direct from Internet)
def download_server():
    jar_url = "https://api.purpurmc.org/v2/purpur/1.21.1/latest/download" 
    if not os.path.exists("server.jar"):
        with st.spinner("Downloading Minecraft Server Engine... Please wait."):
            r = requests.get(jar_url)
            with open("server.jar", "wb") as f:
                f.write(r.content)
        st.success("Download Complete!")

# 2. Start Server Function
def start_server():
    if not os.path.exists("eula.txt"):
        with open("eula.txt", "w") as f:
            f.write("eula=true")

    # Command to run server
    cmd = ["java", "-Xmx800M", "-Xms512M", "-jar", "server.jar", "nogui"]
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        return process
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# --- UI Buttons ---
if st.button("📥 Download & Setup"):
    download_server()

if st.button("🚀 Start Hosting"):
    proc = start_server()
    if proc:
        st.success("Server is booting up! Laptop band kar sakte hain.")
        st.info("Check 'Manage App' logs to see the server console.")
