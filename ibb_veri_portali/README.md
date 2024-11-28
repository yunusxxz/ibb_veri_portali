# İBB Veri Portalı  

**İBB Veri Portalı**, İstanbul Büyükşehir Belediyesi’nin (İBB) İSPARK verilerine kolayca erişmek ve bu verileri analiz etmek için geliştirilmiş bir Python kütüphanesidir. Kütüphane, İBB’nin sağladığı otopark API'sine bağlanmayı kolaylaştırır ve veri işleme araçlarıyla kullanıcı dostu bir deneyim sunar.  

---

## Özellikler  

- **Genel park bilgilerini çekme:** Tüm İSPARK verilerini tek bir API çağrısı ile elde edin.  
- **Belirli bir parkın detaylarına erişim:** İstediğiniz park ID'sini belirterek detaylı bilgilere ulaşın.  
- **Kolay veri analizi:** Verileri `pandas` DataFrame veya Series formatında işleyin.  

---

## Kurulum  

Kütüphaneyi PyPI üzerinden kolayca kurabilirsiniz:  
```bash
pip install ibb-veri-portali
```  

---

## Kullanım  

### 1. Genel Park Verilerini Çekme  
Tüm park bilgilerini JSON formatında almak için:  
```python
from ibb_veri_portali import json

veriler = json()
print(veriler)
```  

### 2. Belirli Bir Parkın Detaylarını Çekme  
Park ID'sine göre detaylı bilgi almak için:  
```
from ibb_veri_portali import series

park_bilgisi = series(882)  # Örnek: Park ID'si 882
print(park_bilgisi)
```  

### 3. Verileri DataFrame Formatında Kullanma  
Tüm park verilerini `pandas.DataFrame` olarak almak için:  
```
from ibb_veri_portali import dataframe

df = dataframe()
print(df.head())
```  

---

## Gereksinimler  

- Python 3.8 veya üstü  
- `requests` kütüphanesi  
- `pandas` kütüphanesi  

---

## Katkıda Bulunma  

Bu projeye katkıda bulunmak isterseniz, GitHub üzerinden bir **pull request** oluşturabilirsiniz. Hataları veya iyileştirme önerilerinizi **issues** bölümünde paylaşabilirsiniz.  

---

## Lisans  

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.  

---

