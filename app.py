import streamlit as st
import os
import subprocess
import requests

st.set_page_config(page_title="Taha Cloud Host", page_icon="🎮")
st.title("🚀 Taha Pro Cloud Hosting")

# Server files ke naam
JAR_FILE = "server.jar"
# Minecraft 1.21.1 ka official download link
DOWNLOAD_URL = "https://piston-data.mojang.com/v1/objects/45035533e69f3503c6d0358e60144f2396244c46/server.jar"

# 1. Automatic Download Function
def setup_files():
    if not os.path.exists(JAR_FILE):
        with st.spinner("Downloading Minecraft Engine (1.21.1)..."):
            response = requests.get(DOWNLOAD_URL)
            with open(JAR_FILE, "wb") as f:
                f.write(response.content)
        st.success("Download Complete!")
    
    # EULA Accept karna
    if not os.path.exists("eula.txt"):
        with open("eula.txt", "w") as f:
            f.write("eula=true")
        st.info("EULA Accepted.")

# 2. Start Server Function
def start_mc():
    # Streamlit ki RAM (1GB) ke mutabiq settings
    cmd = ["java", "-Xmx800M", "-Xms512M", "-jar", JAR_FILE, "nogui"]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return process

# --- Dashboard UI ---
if st.button("🛠️ Setup & Install"):
    setup_files()

if st.button("▶️ Start Server"):
    if os.path.exists(JAR_FILE):
        proc = start_mc()
        st.success("Server Online! Aap laptop band kar sakte hain.")
        st.warning("Note: IP dhoondne ke liye 'Manage App' ke Logs check karein.")
    else:
        st.error("Pehle Setup wala button dabayein!")

st.sidebar.markdown("---")
st.sidebar.write("Owner: **Taha Farooq**")
st.sidebar.write("Status: **Free VPS Mode**")
