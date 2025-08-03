import os
import subprocess
import threading
import time
from dotenv import load_dotenv
import streamlit as st

# Çevre değişkenlerini yükle
load_dotenv()

def start_streamlit():
    """Streamlit uygulamasını başlat"""
    print("🚀 Streamlit uygulaması başlatılıyor...")
    # Ana uygulama dosyanızın adını buraya yazın
    subprocess.run(["streamlit", "run", "app.py", "--server.port=8501"])

def start_ngrok():
    """ngrok tunnel'ını başlat"""
    # ngrok auth token'ı al
    ngrok_token = os.getenv('NGROK_AUTHTOKEN')
    
    if not ngrok_token:
        print("❌ NGROK_AUTHTOKEN çevresel değişkeni bulunamadı!")
        print("💡 .env dosyanıza NGROK_AUTHTOKEN=your_token_here ekleyin")
        return
    
    print("🔑 ngrok auth token ayarlanıyor...")
    
    # ngrok auth token'ı ayarla
    subprocess.run(["ngrok", "config", "add-authtoken", ngrok_token])
    
    # Streamlit'in başlaması için bekle
    print("⏳ Streamlit'in başlaması bekleniyor...")
    time.sleep(5)
    
    print("🌐 ngrok tunnel oluşturuluyor...")
    # ngrok tunnel başlat
    subprocess.run(["ngrok", "http", "8501"])

if __name__ == "__main__":
    print("=" * 50)
    print("🎯 Essay Grader AI - Public Link Oluşturucu")
    print("=" * 50)
    
    # Streamlit'i arka planda başlat
    streamlit_thread = threading.Thread(target=start_streamlit)
    streamlit_thread.daemon = True
    streamlit_thread.start()
    
    # ngrok'u başlat
    start_ngrok()