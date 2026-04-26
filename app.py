import streamlit as st
import os
import subprocess
import requests

st.title("🚀 Taha Pro Cloud Monitor")

# File Names
JAR_FILE = "server.jar"
# Minecraft 1.21.1 official jar
DOWNLOAD_URL = "https://piston-data.mojang.com/v1/objects/45035533e69f3503c6d0358e60144f2396244c46/server.jar"

if st.button("📥 Step 1: Download Server"):
    if not os.path.exists(JAR_FILE):
        with st.spinner("Downloading..."):
            r = requests.get(DOWNLOAD_URL)
            with open(JAR_FILE, "wb") as f:
                f.write(r.content)
        st.success("Download Ho Gayi!")
    else:
        st.info("File pehle se maujood hai.")

if st.button("▶️ Step 2: Start & See Logs"):
    if os.path.exists(JAR_FILE):
        # EULA auto-accept
        with open("eula.txt", "w") as f:
            f.write("eula=true")
        
        # Server start command
        cmd = ["java", "-Xmx800M", "-Xms512M", "-jar", JAR_FILE, "nogui"]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        
        st.warning("Server start ho raha hai... Niche logs dekhein:")
        
        # Live Logs Console
        log_placeholder = st.empty()
        full_log = ""
        
        # Sirf pehli 20 lines dikhayega taake crash na ho
        for _ in range(20):
            line = process.stdout.readline()
            if not line: break
            full_log += line
            log_placeholder.code(full_log)
    else:
        st.error("Pehle Step 1 wala button dabayein!")
