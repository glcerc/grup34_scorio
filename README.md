# <h1 align="center">✏️ Scorio</h1>
<p align="center">
  Yapay zekâ destekli ödev değerlendirme ve kişisel geri bildirim sistemi
</p>



## 👥 Takımımız

|                                   Fotoğraf                                   | İsim                   | Rol           | Sosyal Medya                                                                                |
| :--------------------------------------------------------------------------: | ---------------------- | ------------- | ------------------------------------------------------------------------------------------- |
| <img src="" width="100"/> | **Behiye Bedir** | Scrum Master | [GitHub](https://github.com/) \| [LinkedIn](https://linkedin.com/in/) |
| <img src="" width="100"/> | **Gülce Berfin Ercan**       | Product Owner  | [GitHub](https://github.com/glcerc) \| [LinkedIn](https://linkedin.com/in/) |
| <img src="" width="100"/> | **Şadi Gökdeniz Akbayır**         | Developer     | [GitHub](https://github.com/) \| [LinkedIn](https://linkedin.com/in/)     |
| <img src="" width="100"/> | **Arda Gonca**         | Developer     | [GitHub](https://github.com/) \| [LinkedIn](https://linkedin.com/in/)     |
| <img src="" width="100"/> | **Elif Nur**        | Developer     | [GitHub](https://github.com/) \| [LinkedIn](https://linkedin.com/in/)   |



## 🎯 Vizyonumuz

Geleneksel değerlendirme yöntemleri hem zaman alıcı hem de subjektif olabiliyor. **Scorio**, öğretmenlerin yazılı ödevleri ve sınavları objektif, hızlı ve kişiselleştirilmiş şekilde değerlendirmesini sağlar.  
Rubrik tabanlı puanlama + GPT destekli açıklayıcı geri bildirim = Gerçek bir eğitim teknolojisi çözümü.

---

## 🧠 Proje Özeti

> **Scorio**, öğretmenlerin sisteme yükledikleri rubrikleri kullanarak, öğrencilerin yazılarını GPT-4 destekli yapay zekâ modeli ile otomatik puanlayan ve yorumlayan bir web uygulamasıdır.

---

## 🚀 Ürün Özellikleri

- 🧾 JSON formatında dinamik rubrik yükleme
- ✍️ Öğrenci yazısı girişi (text/file)
- 🧠 GPT-4 destekli puanlama ve yorum üretimi
- 🧮 Kriter bazlı puanlama + toplam skor
- 🗣️ Öğrenciye özel geri bildirim
- 📤 Geri bildirim çıktısını kopyalama ve PDF olarak indirme
- 👥 Çoklu öğrenci değerlendirme (v3.0 planı)

---
##  🗂️ Product Backlog – Scorio
| #  | User Story                                                             | Açıklama                                                                                  | SP | Sprint   |
| -- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | -- | -------- |
| 1  | Vizyon ve hedef kitleyi tanımlamak                                     | Projenin amacını ve kime hitap ettiğini netleştirir                                       | 3  | Sprint 1 |
| 2  | Ürün ismi, logo ve marka dili oluşturmak                               | Scorio ismini seçme, görsel kimlik belirleme                                              | 2  | Sprint 1 |
| 3  | Takım yapısını ve klasör sistemini kurmak                              | Takım rolleri, görev paylaşımı ve proje klasörleme yapılır                                | 3  | Sprint 1 |
| 4  | Rubrik formatını belirleyip JSON şablonu oluşturmak                    | Öğretmenlerin değerlendirme kriterlerini tanımlayacağı yapı                               | 4  | Sprint 1 |
| 5  | README dosyasını hazırlamak                                            | Projenin tanıtımı, kurulumu ve sprint planları dahil edilir                               | 3  | Sprint 1 |
| 6  | Kullanıcı persona ve senaryo oluşturmak                                | Hedef kullanıcıları anlamak için 5 farklı persona ve akış hazırlığı                       | 5  | Sprint 1 |
| 7  | Streamlit UI ile temel arayüz oluşturmak                               | Giriş ekranı, yazı alanı, düğmeler                                                        | 5  | Sprint 2 |
| 8  | Rubrik yükleme özelliği eklemek (form girişi ve/veya dosya yükleme)    | Kullanıcılar rubriklerini dışarıdan veya manuel olarak girebilir                          | 5  | Sprint 2 |
| 9  | Öğrenci yazısını girme/yükleme modülü geliştirmek                      | Öğretmen, yazıyı ya yapıştırır ya da dosya olarak yükler                                  | 4  | Sprint 2 |
| 10 | OpenAI API (GPT-4) entegrasyonunu kurmak                               | GPT-4 ile yazı değerlendirme bağlantısını sağlamak                                        | 3  | Sprint 2 |
| 11 | GPT’ye prompt gönderip rubrik bazlı puanlama ve açıklama alma          | Yapay zekâdan her kriter için skor ve neden açıklaması alınır                             | 7  | Sprint 2 |
| 12 | Değerlendirme sonuçlarını görselleştirmek                              | Kriter bazlı skorlar + açıklamalar kullanıcıya sade şekilde sunulur                       | 5  | Sprint 2 |
| 13 | Geri bildirimi kopyalama ve dışa aktarma özelliği eklemek              | Sistem tarafından üretilen geri bildirim kopyalanabilir veya indirilebilir hâle getirilir | 3  | Sprint 2 |
| 14 | PDF çıktısı alma özelliği geliştirmek                                  | Öğretmen geri bildirimi PDF olarak alabilir                                               | 6  | Sprint 3 |
| 15 | Yapay zekâdan rubrik önerisi almayı mümkün kılmak                      | Öğretmen kriterleri girmekte zorlanırsa, GPT'den öneri alabilir                           | 6  | Sprint 3 |
| 16 | Aynı rubrikle çoklu öğrenci değerlendirme modülü geliştirmek           | Tek bir rubrikle birden fazla yazı arka arkaya değerlendirilebilir                        | 7  | Sprint 3 |
| 17 | Gelişim takibi için öğrenciye özel geri bildirim geçmişi oluşturmak    | Öğrencinin geçmiş değerlendirmeleri bir araya getirilebilir                               | 5  | Sprint 3 |
| 18 | Demo video ve jüri sunum materyallerini hazırlamak                     | Scorio tanıtım videosu ve jüri sunumu                                                     | 5  | Sprint 3 |
| 19 | Proje posteri, sunum görselleri ve simgeler oluşturmak                 | Görsel sunum materyalleri                                                                 | 3  | Sprint 3 |
| 20 | GitHub cleanup, açıklayıcı yorumlar ve örnek veri dosyalarını yüklemek | Proje finalde açık ve anlaşılır dokümantasyona sahip olmalı                               | 5  | Sprint 3 |


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 🌀 Sprint Süreci

## 🧮 Puan Tamamlama ve Sprint Dağılımı Mantığı

Projemiz toplam 100 Story Point (SP) üzerinden planlanmıştır. Bu puanlar, her özelliğin karmaşıklığı, iş yükü ve geliştirme süresine göre tahmini olarak belirlenmiştir. Puanlamalar sprint başına eşit değil; işin doğasına uygun şekilde artan zorluk ve geliştirme yoğunluğuna göre dağıtılmıştır:

Sprint Başına Dağılım
| Sprint     | Toplam Puan |
| ---------- | ----------- |
| Sprint 1   | **20 SP**   |
| Sprint 2   | **32 SP**   |
| Sprint 3   | **48 SP**   |
| **TOPLAM** | **100 SP**  |

🎯 Sprint 1, proje planlaması, rubrik yapısının belirlenmesi ve temel yapı taşlarının hazırlanmasına odaklanır (düşük teknik yük).
⚙️ Sprint 2, GPT entegrasyonu, arayüz geliştirme ve temel değerlendirme motorunun tamamlanmasını kapsar.
🚀 Sprint 3, ürün çıktılarının sunulabilir hâle getirilmesi, PDF oluşturma ve çoklu kullanıcı desteği gibi ileri seviye özelliklerle en yüksek teknik yükü barındırır.

Bu dağılım sayesinde, projenin aşamalı gelişimi hem sürdürülebilir hem de değerlendirilebilir hâle gelmiştir.

## 🚀 Sprint 1 (20 Haziran – 6 Temmuz)  
**Amaç:** Proje vizyonu, backlog, rubrik modeli, kullanıcı analizi  

• **Sprint 1 Notları**  :Proje adı Scorio olarak belirlendi. Takım organizasyonu oluşturuldu. Ürün açıklaması, hedef kitle, kullanıcı beklentileri ve çözüm önerileri açıklandı. Product Backlog temel hatlarıyla çıkarıldı.

• **Sprint içinde tamamlanması tahmin edilen puan**  : 20 SP


• **Puan tamamlama mantığı**  :3 sprint üzerinden, görev bazlı toplam 100 SP’lik yapı oluşturulmuştur. Sprint 1; analiz, kullanıcı belirleme ve planlama gibi başlangıç safhalarını içerdiğinden 20 SP olarak belirlenmiştir.


• **Daily Scrum**  : Toplantılar Google Meet üzerinden gerçekleştirilmiştir. Sürekli iletişim için WhatsApp grubu aktif olarak kullanılmıştır.

• **Sprint Board Update**  
Sprint panosu Miro üzerinden oluşturulmuştur. Görevler Trello'da “To Do / In Progress / Done” şeklinde kategorilendirilmiş ve sorumlular belirlenmiştir.


• **Sprint Review**  
Scorio’nun temel yönleri, kullanıcı ihtiyaçları ve çözüm stratejisi başarıyla tanımlandı. Proje vizyonu kullanıcı kitlesiyle net biçimde eşleşti. Persona çalışmaları farklı yaş ve meslek gruplarını kapsayacak şekilde çeşitlendirildi. Ürün özellikleri öğretmenlerin iş yükünü azaltma, öğrencilere kişiselleştirilmiş geribildirim sunma üzerine şekillendirildi. Rubrik + LLM tabanlı yapı sayesinde Scorio’nun diğer sistemlerden ayrıştığı gösterildi. Renk, logo ve marka kimliği çalışmaları tamamlandı.


• **Sprint Retrospective**  
Takım içi iletişim ve görev paylaşımı güçlüydü. Ürün fikrine olan inanç ve sahiplenme motivasyonu yükseltti. Kullanıcı analizi başarılıydı ve doğru hedef kitlenin tespiti sağlandı. Zaman planlaması ve dokümantasyon disiplini noktasında bazı iyileştirmeler yapılması gerektiği belirlendi. Development ekibinin iletişiminin güçlenmesi adına ek toplantılar alınması kararlaştırıldı.

# Sprint 2
