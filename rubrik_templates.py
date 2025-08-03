from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB Atlas bağlantısı
MONGO_URI = os.getenv('MONGO_URI')

if not MONGO_URI:
    raise Exception("⚠️ .env dosyasında MONGO_URI değişkeni tanımlı değil!")

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=5000,
    connectTimeoutMS=5000,
    socketTimeoutMS=5000,
    maxPoolSize=1
)

db = client['essay_grader']  # Veritabanı adı

def create_template_rubrics():
    """Hazır rubrik şablonlarını MongoDB Atlas’a ekler"""

    templates = [
        {
            "name": "Kompozisyon Rubriği",
            "description": "Genel kompozisyon değerlendirmesi için standart rubrik",
            "grade_levels": [9, 10, 11, 12],
            "subject": "Türk Dili ve Edebiyatı",
            "criteria": [
                {
                    "name": "İçerik ve Konu İşleme",
                    "description": "Konuya uygunluk, bilgi doğruluğu ve derinlik",
                    "weight": 30,
                    "max_points": 30,
                    "levels": {
                        "mükemmel": "26-30: Konu tam anlaşılmış, detaylı işlenmiş",
                        "iyi": "21-25: Konu anlaşılmış, yeterli detay var",
                        "orta": "16-20: Konu kısmen anlaşılmış",
                        "zayıf": "0-15: Konu yanlış anlaşılmış veya eksik"
                    }
                },
                {
                    "name": "Yapı ve Düzen",
                    "description": "Giriş-gelişme-sonuç yapısı, paragraf düzeni",
                    "weight": 25,
                    "max_points": 25,
                    "levels": {
                        "mükemmel": "22-25: Mükemmel yapı, akıcı geçişler",
                        "iyi": "18-21: İyi yapı, çoğu geçiş başarılı",
                        "orta": "14-17: Temel yapı var, bazı sorunlar",
                        "zayıf": "0-13: Yapı bozuk veya eksik"
                    }
                },
                {
                    "name": "Dil ve Anlatım",
                    "description": "Dilbilgisi, yazım kuralları, kelime seçimi",
                    "weight": 25,
                    "max_points": 25,
                    "levels": {
                        "mükemmel": "22-25: Hatasız dil kullanımı",
                        "iyi": "18-21: Az sayıda küçük hata",
                        "orta": "14-17: Orta düzeyde hatalar",
                        "zayıf": "0-13: Çok sayıda dil hatası"
                    }
                },
                {
                    "name": "Yaratıcılık ve Özgünlük",
                    "description": "Orijinal düşünce, farklı bakış açıları",
                    "weight": 20,
                    "max_points": 20,
                    "levels": {
                        "mükemmel": "18-20: Çok yaratıcı ve özgün",
                        "iyi": "14-17: Yaratıcı unsurlar var",
                        "orta": "11-13: Kısmen özgün",
                        "zayıf": "0-10: Klişe ve sıradan"
                    }
                }
            ],
            "total_points": 100,
            "is_template": True,
            "teacher_id": None,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "name": "Deneme Rubriği",
            "description": "Düşünce yazısı ve deneme değerlendirmesi",
            "grade_levels": [10, 11, 12],
            "subject": "Türk Dili ve Edebiyatı",
            "criteria": [
                {"name": "Tez ve Argüman", "description": "Ana tezin netliği ve destekleyici argümanlar", "weight": 35, "max_points": 35},
                {"name": "Eleştirel Düşünme", "description": "Analiz yetisi, farklı görüşleri değerlendirme", "weight": 25, "max_points": 25},
                {"name": "Örnekleme ve Kanıtlama", "description": "Uygun örnekler, kaynak kullanımı", "weight": 20, "max_points": 20},
                {"name": "Dil ve Üslup", "description": "Deneme türüne uygun dil kullanımı", "weight": 20, "max_points": 20}
            ],
            "total_points": 100,
            "is_template": True,
            "teacher_id": None,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        },
        {
            "name": "Proje Raporu Rubriği",
            "description": "Araştırma projesi ve rapor değerlendirmesi",
            "grade_levels": [9, 10, 11, 12],
            "subject": "Genel",
            "criteria": [
                {"name": "Araştırma Kalitesi", "description": "Kaynak kullanımı, bilgi toplama", "weight": 30, "max_points": 30},
                {"name": "İçerik Organizasyonu", "description": "Bilgilerin düzenli sunumu", "weight": 25, "max_points": 25},
                {"name": "Analiz ve Yorum", "description": "Verileri analiz etme ve yorumlama", "weight": 25, "max_points": 25},
                {"name": "Sunum ve Format", "description": "Rapor formatı, grafik/tablo kullanımı", "weight": 20, "max_points": 20}
            ],
            "total_points": 100,
            "is_template": True,
            "teacher_id": None,
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
    ]

    try:
        # Önce şablonları temizle
        db.rubrics.delete_many({"is_template": True})

        # Yeni şablonları ekle
        result = db.rubrics.insert_many(templates)
        print(f"✅ {len(result.inserted_ids)} rubrik şablonu başarıyla eklendi!")

        # Eklenen şablonları listele
        for template in templates:
            print(f"📋 {template['name']} - {len(template['criteria'])} kriter")

    except Exception as e:
        print(f"❌ Veri ekleme hatası: {e}")

def get_template_rubrics():
    """Tüm şablon rubrikleri getirir"""
    return list(db.rubrics.find({"is_template": True}))

def get_rubric_by_id(rubric_id):
    """ID'ye göre rubrik getirir"""
    from bson import ObjectId
    return db.rubrics.find_one({"_id": ObjectId(rubric_id)})

if __name__ == "__main__":
    print("🚀 Rubrik şablonları oluşturuluyor...")
    create_template_rubrics()

    print("\n📊 Mevcut şablonlar:")
    templates = get_template_rubrics()
    for i, template in enumerate(templates, 1):
        criteria_count = len(template['criteria'])
        print(f"{i}. {template['name']} ({criteria_count} kriter)")
