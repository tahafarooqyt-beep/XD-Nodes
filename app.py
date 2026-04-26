import streamlit as st
import os
import subprocess
import requests

st.title("🚀 Taha Cloud - Playit Linker")

# Paste your claim code here
claim_code = "fdfce59474c24e2e4a30f5d1c4fc4cb5"

if st.button("🔗 Link Playit & Start"):
    # 1. Download Playit if not exists
    if not os.path.exists("playit"):
        r = requests.get("https://github.com/playit-cloud/playit-agent/releases/latest/download/playit-linux-amd64")
        with open("playit", "wb") as f:
            f.write(r.content)
        os.chmod("playit", 0o755)

    # 2. Run Playit with Claim Code
    # Is command se aapka Streamlit Playit account se link ho jayega
    st.info("Linking account... Please wait.")
    link_cmd = ["./playit", "setup", "--code", claim_code]
    subprocess.Popen(link_cmd)

    # 3. Start Minecraft Server in background
    if os.path.exists("server.jar"):
        # EULA cleanup and accept
        if os.path.exists("world/session.lock"):
            os.remove("world/session.lock")
        with open("eula.txt", "w") as f:
            f.write("eula=true")
            
        mc_cmd = ["java", "-Xmx800M", "-Xms512M", "-jar", "server.jar", "nogui"]
        subprocess.Popen(mc_cmd)
        st.success("Server and Playit are running!")
    else:
        st.error("server.jar nahi mili! Pehle setup karein.")

st.warning("Logs mein check karein, jab link ho jaye toh Playit website par 'Agent' green ho jayega.")
