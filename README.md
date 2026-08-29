# AgroGen AI — Streamlit MVP

AgroGen AI — chorvachilik uchun raqamli hayvon pasporti, mahsuldorlik monitoringi va naslchilik qarorlarini qo‘llab-quvvatlashga mo‘ljallangan tanlov MVP.

## Funksiyalar
- Dashboard
- 100 ta demo hayvon
- Hayvon qidirish va qo‘shish
- Raqamli pasport
- Sut/vazn monitoringi
- Naslchilik AI demo
- AI Farm Assistant

## Local ishga tushirish

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Streamlit Community Cloud
GitHub repository root qismiga `app.py`, `requirements.txt` va `data/animals.json` joylashtiriladi. Streamlit Community Cloud'da repository va `app.py` entrypoint tanlanadi.

## Muhim
Demo ma’lumotlari sun’iy yaratilgan. AI tavsiyasi hozircha qoidaviy decision-support prototipidir; veterinariya yoki genetik tashxis emas.
---

## 🧠 Alohida ma'lumotlar: AgroGen AI qanday ishlaydi?

Quyida platformaning ishlash mantig'i bosqichma-bosqich ifodalangan:
   🐄 HAYVON
       │
       ▼
📋 MA'LUMOTLAR
       │
       ▼
🗄️ RAQAMLI BAZA
       │
       ▼
  📊 TAHLIL
       │
       ▼
  🧠 AI MODEL
       │
       ▼
💡 TAVSIYA / SIGNAL
       │
       ▼
  👨‍🌾 FERMER
  
Bu sxema quyidagi jarayonni aks ettiradi:

1. **🐄 HAYVON**: Har bir hayvon (sigir, qo'y, echki va boshqalar) tizimga kiritiladi.
2. **📋 MA'LUMOTLAR**: Uning zoti, yoshi, vazni, sog'lig'i va naslchilik ma'lumotlari platformaga yoziladi.
3. **🗄️ RAQAMLI BAZA**: Barcha ma'lumotlar xavfsiz va tizimli ravishda raqamli bazada saqlanadi.
4. **📊 TAHLIL**: Sun'iy intellekt va statistika modellari ushbu ma'lumotlarni qayta ishlaydi va tahlil qiladi.
5. **🧠 AI MODEL**: Tahlil natijalariga asoslanib, AI modeli kelajakdagi mahsuldorlik va naslchilik potentsialini baholaydi.
6. **💡 TAVSIYA / SIGNAL**: Tizim fermerga aniq tavsiyalar (qaysi hayvonni qachon naslchilikka qo'yish) yoki xavf signalini (kasallik belgilari) beradi.
7. **👨‍🌾 FERMER**: Fermer bu ma'lumotlarni qabul qiladi va xo'jalikda amaliy qarorlar qabul qilishda foydalanadi.
