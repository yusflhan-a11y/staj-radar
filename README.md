# 🚀 Staj Radar - İş ve Staj İlanı Veri Toplama Motoru

**Staj Radar**, Youthall, Kariyer.net ve LinkedIn gibi popüler platformlardaki iş ve staj ilanlarını otomatik olarak toplayan, verileri temizleyip üniversite bölümlerine göre kategorize eden ve mobil/masaüstü uygulamalara veri sağlayan **modüler Python arka plan (backend) sistemidir**.

---

## 🎯 Projenin Amacı

Öğrencilerin ve yeni mezunların kendilerine en uygun staj ve iş fırsatlarını tek bir platform üzerinden, kendi bölümlerine ve ilgi alanlarına göre ayrıştırılmış olarak bulabilmelerini sağlamak amacıyla kararlı, hataya dayanıklı ve ölçeklenebilir bir veri altyapısı sunar.

---

## 🛠️ Mimari ve Öne Çıkan Özellikler

* **Modüler Scraper Mimarisi (`BaseScraper`)**: Yeni platformların (Toptalent vb.) sisteme kolayca entegre edilmesini sağlayan genişletilebilir yapı.
* **Tip Güvenliği ve Doğrulama (`Pydantic v2`)**: Sitelere erişilerek çekilen verilerin standart kalıplardan geçirilerek doğrulanması.
* **Dinamik İçerik ve Anti-Bot Desteği (`Playwright` & `Stealth`)**: Sonsuz kaydırma (infinite scroll) ve bot koruma sistemlerine takılmayan tarayıcı otomasyonu.
* **ETL Pipeline (Temizleme & Tekilleştirme)**:
  * HTML etiketlerini ve gereksiz karakterleri temizleme.
  * Mükerrer (duplicate) ilanları otomatik engelleme.
  * İlan açıklamalarından ilgili üniversite bölümünü (Bilgisayar Müh., Endüstri Müh., Pazarlama vb.) otomatik tespit etme.
* **Kalıcı Depolama (`PostgreSQL` & `SQLAlchemy 2.0 ORM`)**: Güvenli `UPSERT` işlemleriyle güncel tutulan veri havuzu.

---

## 📂 Proje Klasör Anatomisi

```text
staj_radar/
├── .env                # Ortam değişkenleri ve gizli konfigürasyonlar
├── .env.example        # Örnek ortam değişkenleri kılavuzu
├── .gitignore          # Git tarafından takip edilmeyecek dosyalar
├── requirements.txt    # Projenin bağımlı olduğu kütüphaneler listesi
├── README.md           # Proje tanıtım ve kullanım kılavuzu
└── src/                # Ana kaynak kod dizini
    ├── config.py       # Uygulama ve ortam ayarları yönetimi
    ├── models/         # Pydantic veri kalıpları (job.py vb.)
    ├── scrapers/       # Platform scraper modülleri (youthall_scraper.py vb.)
    ├── pipeline/       # Metin temizleme, tekilleştirme ve kategorizasyon
    └── db/             # Veritabanı bağlantı ve kayıt katmanı
```

---

## 💻 Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın
```bash
git clone https://github.com/KULLANICI_ADIN/staj-radar.git
cd staj-radar
```

### 2. Sanal Ortamı Oluşturun ve Aktif Edin
```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS / Linux
# .venv\Scripts\activate   # Windows
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Ortam Değişkenlerini Hazırlayın
```bash
cp .env.example .env
```

### 5. Sistemi Test Edin
```bash
python3 test_step1.py
```

---

## 📄 Lisans
Bu proje geliştirme aşamasındadır. Tüm hakları saklıdır.
