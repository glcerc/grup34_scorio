import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

load_dotenv()

# Gemini API'yi yapılandır
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

def evaluate_essay(essay_text, rubrik):
    """Detaylı rubrik ile essay değerlendirme"""
    prompt = f"""
    Sen deneyimli bir öğretmensin. Aşağıdaki öğrenci yazısını verilen kriterlere göre objektif bir şekilde değerlendir.

    DEĞERLENDIRME KRİTERLERİ:
    {rubrik}

    ÖĞRENCİ METNİ:
    {essay_text}

    DEĞERLENDIRME FORMATI:
    Her kriter için:
    1. Verilen puanı belirt
    2. Bu puanın gerekçesini açıkla
    3. Gelişim önerileri sun

    Son olarak:
    - Toplam puanı hesapla
    - Genel değerlendirme yap
    - 3 ana gelişim önerisi ver

    Değerlendirmeni profesyonel ve yapıcı bir dilde yap.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Hata oluştu: {str(e)}"

def analyze_text_quality(essay_text):
    """Hızlı metin kalitesi analizi"""
    prompt = f"""
    Aşağıdaki metni hızlı bir şekilde analiz et ve genel kalitesini değerlendir:

    METİN:
    {essay_text}

    ANALIZ ET:
    1. Dil bilgisi ve yazım kalitesi (0-25 puan)
    2. Metin yapısı ve akış (0-25 puan)  
    3. İçerik zenginliği (0-25 puan)
    4. Genel okunabilirlik (0-25 puan)

    SONUÇ:
    - Toplam puan: X/100
    - 2 güçlü yön
    - 2 gelişim alanı
    - Kısa genel yorum

    Analizi özet halinde sun.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Hata oluştu: {str(e)}"

def get_essay_statistics(essay_text):
    """Metin istatistikleri hesapla"""
    if not essay_text:
        return {}
    
    words = essay_text.split()
    sentences = re.split(r'[.!?]+', essay_text)
    paragraphs = essay_text.split('\n\n')
    
    stats = {
        'word_count': len(words),
        'sentence_count': len([s for s in sentences if s.strip()]),
        'paragraph_count': len([p for p in paragraphs if p.strip()]),
        'char_count': len(essay_text),
        'avg_words_per_sentence': round(len(words) / max(len([s for s in sentences if s.strip()]), 1), 1)
    }
    
    return stats

def suggest_improvements(essay_text):
    """Gelişim önerileri üret"""
    prompt = f"""
    Bu metni analiz et ve öğrenciye 5 pratik gelişim önerisi ver:

    METİN:
    {essay_text}

    ÖNERİLER:
    1. Yapı ile ilgili
    2. İçerik ile ilgili  
    3. Dil kullanımı ile ilgili
    4. Yazım/dilbilgisi ile ilgili
    5. Genel yazma becerisi ile ilgili

    Her öneriyi kısa ve uygulanabilir şekilde yaz.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Hata oluştu: {str(e)}"

def grade_converter(score, total=100):
    """Puanı harf notuna çevir"""
    percentage = (score / total) * 100
    
    if percentage >= 90:
        return "AA", "Mükemmel"
    elif percentage >= 85:
        return "BA", "Çok İyi"
    elif percentage >= 75:
        return "BB", "İyi"
    elif percentage >= 65:
        return "CB", "Orta"
    elif percentage >= 55:
        return "CC", "Geçer"
    elif percentage >= 45:
        return "DC", "Şartlı Geçer"
    else:
        return "FF", "Başarısız"