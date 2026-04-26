import streamlit as st
import os
import subprocess
import requests

st.title("🖥️ Taha Personal Cloud Hosting")

# 1. Badi files download karne ka function
def download_file(url, filename):
    if not os.path.exists(filename):
        with st.spinner(f"Downloading {filename}..."):
            r = requests.get(url)
            with open(filename, 'wb') as f:
                f.write(r.content)
        st.success(f"{filename} Downloaded!")

# 2. Server Start Function
def start_server():
    # Streamlit ke RAM ke mutabiq 800MB allot karenge
    cmd = "java -Xmx800M -Xms512M -jar server.jar nogui"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return process

# --- Setup ---
# Agar aapka server.jar GitHub par nahi hai, toh hum yahan link de sakte hain
# Example: Purpur ya Spigot ka download link
jar_url = "https://api.purpurmc.org/v2/purpur/1.21.1/latest/download" 

if st.button("🚀 Start My Hosting"):
    download_file(jar_url, "server.jar")
    
    # EULA accept karna zaroori hai
    with open("eula.txt", "w") as f:
        f.write("eula=true")
        
    proc = start_server()
    st.success("Taha OG SMP is now LIVE on Cloud!")
    st.info("Laptop band kar dein, ye chalta rahega.")

st.sidebar.warning("Note: Streamlit 1GB RAM limit rakhta hai.")
