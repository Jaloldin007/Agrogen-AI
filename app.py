import pandas as pd
import streamlit as st
import json
from pathlib import Path
from PIL import Image
import plotly.express as px
from datetime import date
import numpy as np

st.set_page_config(
    page_title="AgroGen AI",
    page_icon="🐄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main { background: linear-gradient(135deg, #0a1620, #142830); }
    .block-container { padding-top: 1.5rem; max-width: 1300px; }
    .hero {
        padding: 2rem 2.5rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #0d2818, #1a4a2e);
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
        border: 1px solid rgba(255,255,255,0.05);
    }
    .hero h1 {
        margin: 0;
        font-size: 2.8rem;
        background: linear-gradient(90deg, #8cffc3, #4ecdc4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero p { color: #b8cfc3; font-size: 1.1rem; margin-top: 0.5rem; }
    .kpi {
        padding: 1.2rem 1.5rem;
        border-radius: 16px;
        background: rgba(13, 28, 21, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(37, 69, 54, 0.5);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        text-align: center;
    }
    .kpi:hover { transform: translateY(-5px); box-shadow: 0 10px 30px rgba(0,255,150,0.1); }
    .kpi small { color: #89a195; font-size: 0.9rem; display: block; }
    .kpi b { font-size: 2.2rem; color: #8cffc3; display: block; margin-top: 0.3rem; }
    .ai-box {
        padding: 1.5rem;
        border-radius: 16px;
        background: linear-gradient(135deg, #0d2818, #1a4a2e);
        border: 1px solid rgba(78, 205, 196, 0.2);
        box-shadow: 0 5px 25px rgba(78, 205, 196, 0.05);
    }
    .testimonial {
        padding: 1.2rem;
        border-radius: 14px;
        background: rgba(13, 28, 21, 0.6);
        border-left: 4px solid #4ecdc4;
        margin: 0.5rem 0;
    }
    .testimonial .name { color: #8cffc3; font-weight: bold; }
    .testimonial .stars { color: #f4c430; }
    .footer {
        text-align: center;
        color: #4a6a5a;
        font-size: 0.85rem;
        padding: 1.5rem 0;
        border-top: 1px solid rgba(37, 69, 54, 0.3);
        margin-top: 2rem;
    }
    .section-desc {
        color: #b8cfc3;
        background: rgba(13, 28, 21, 0.4);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        border-left: 3px solid #4ecdc4;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

try:
    image = Image.open('logo.jpg')
    st.image(image, use_container_width=True)
except:
    st.warning("⚠️ Rasm (logo.jpg) topilmadi.")

st.markdown("""
<div class="hero">
    <h1>🐄 AgroGen AI</h1>
    <p>Chorvachilikni raqamli boshqarish, mahsuldorlik monitoringi va naslchilik qarorlarini maʼlumotlar asosida qoʻllab-quvvatlash.</p>
    <p style="font-size: 0.9rem; color: #4ecdc4; margin-top: 0.5rem;">🚀 2026 yilgi AgriTech startaplari orasida yetakchi</p>
</div>
""", unsafe_allow_html=True)

DATA_FILE = Path("data/animals.json")

@st.cache_data
def load_animals():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return pd.DataFrame(json.load(f))

df = load_animals()

if "animals" not in st.session_state:
    st.session_state.animals = df.copy()

animals = st.session_state.animals
breeds = animals['breed'].unique().tolist()

st.sidebar.title("🐄 AgroGen AI")
st.sidebar.caption("Livestock Intelligence — tanlov MVP")

page = st.sidebar.radio(
    "Boʻlim",
    ["Dashboard", "Hayvonlar", "Hayvon pasporti", "Sut & vazn", "Naslchilik AI", "AI Assistant"],
    index=0
)

st.sidebar.divider()
lang = st.sidebar.selectbox("🌐 Til / Language", ["O'zbek", "Русский", "English"])
st.sidebar.divider()
st.sidebar.info("MVP: 100 ta demo hayvon. Keyingi bosqichda real ferma maʼlumotlari va ML modeli ulanadi.")

# ======================== DASHBOARD ========================
if page == "Dashboard":
    st.markdown("""
    <div class="section-desc">
        📊 <b>Dashboard</b> — ferma faoliyatining asosiy ko'rsatkichlari: hayvonlar soni, o'rtacha sut va vazn, 
        zotlar bo'yicha taqsimot va eng mahsuldor hayvonlar reytingi.
    </div>
    """, unsafe_allow_html=True)

    females = animals[animals["sex"] == "Urgʻochi"]
    avg_milk = females["milk"].mean() if not females.empty else 0
    avg_weight = animals["weight"].mean() if not animals.empty else 0
    high = len(females[females["milk"] >= 30])

    cols = st.columns(4)
    kpi_data = [
        ("Jami hayvon", len(animals)),
        ("Urgʻochi", len(females)),
        ("Oʻrtacha sut", f"{avg_milk:.1f} L/kun"),
        ("Oʻrtacha vazn", f"{avg_weight:.0f} kg")
    ]
    for col, (title, value) in zip(cols, kpi_data):
        col.markdown(f'<div class="kpi"><small>{title}</small><b>{value}</b></div>', unsafe_allow_html=True)

    st.subheader("📊 Ferma koʻrsatkichlari")
    c1, c2 = st.columns(2)

    with c1:
        st.write("Zotlar boʻyicha taqsimot")
        fig = px.pie(animals, names='breed', title='Zotlar taqsimoti',
                     color_discrete_sequence=px.colors.sequential.Greens_r)
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                          font=dict(color='#b8cfc3'))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.write("Sut mahsuldorligi")
        if not females.empty:
            fig = px.bar(females.head(25), x='id', y='milk', color='breed',
                         title='Sut mahsuldorligi',
                         color_discrete_sequence=px.colors.sequential.Greens_r)
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                              font=dict(color='#b8cfc3'))
            st.plotly_chart(fig, use_container_width=True)

    st.subheader("🏆 Eng mahsuldor hayvonlar")
    st.markdown("*Sut mahsuldorligi bo'yicha eng yaxshi 10 ta hayvon*")
    top = females.sort_values("milk", ascending=False).head(10) if not females.empty else pd.DataFrame()
    if not top.empty:
        st.dataframe(top[["id", "breed", "age", "weight", "milk", "breeding_status"]],
                     use_container_width=True, hide_index=True)

# ======================== HAYVONLAR ========================
elif page == "Hayvonlar":
    st.markdown("""
    <div class="section-desc">
        🐄 <b>Hayvonlar bazasi</b> — barcha hayvonlar haqidagi ma'lumotlar: ID, zoti, jinsi, yoshi, vazni, 
        sut mahsuldorligi va nasl ma'lumotlari. Qidiruv, filtr va CSV yuklab olish imkoniyatlari mavjud.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        breed_filter = st.multiselect("Zot", breeds, default=[])
    with col2:
        sex_filter = st.selectbox("Jins", ["Hammasi", "Urgʻochi", "Erkak"])
    with col3:
        min_milk = st.slider("Minimal sut (L)", 0, 50, 0)

    filtered = animals.copy()
    if breed_filter:
        filtered = filtered[filtered['breed'].isin(breed_filter)]
    if sex_filter != "Hammasi":
        filtered = filtered[filtered['sex'] == sex_filter]
    filtered = filtered[filtered['milk'] >= min_milk]

    st.write(f"Topildi: {len(filtered)} ta")

    csv = filtered.to_csv(index=False)
    st.download_button(
        label="📥 CSV yuklab olish",
        data=csv,
        file_name='hayvonlar.csv',
        mime='text/csv',
        use_container_width=True
    )

    st.dataframe(filtered, use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("➕ Yangi hayvon qoʻshish")
    st.markdown("*Yangi hayvon ma'lumotlarini kiritib, bazaga qo'shing*")
    with st.form("add_animal"):
        c1, c2, c3 = st.columns(3)
        new_id = c1.text_input("ID", value=f"UZ-{len(animals)+1:04d}")
        new_breed = c2.selectbox("Zot", breeds)
        new_sex = c3.selectbox("Jins", ["Urgʻochi", "Erkak"])

        c4, c5, c6 = st.columns(3)
        new_age = c4.number_input("Yosh", 0, 20, 2)
        new_weight = c5.number_input("Vazn (kg)", 0, 1500, 450)
        new_milk = c6.number_input("Sut (L/kun)", 0.0, 100.0, 25.0)
        submitted = st.form_submit_button("➕ Hayvonni qoʻshish")
        if submitted:
            row = {
                "id": new_id,
                "name": f"Yangi hayvon",
                "breed": new_breed,
                "sex": new_sex,
                "age": new_age,
                "weight": new_weight,
                "milk": new_milk if new_sex == "Urgʻochi" else 0,
                "father": "Nomaʼlum",
                "mother": "Nomaʼlum",
                "vaccination": str(date.today()),
                "breeding_status": "Kuzatuvda",
                "health_status": "Sogʻlom",
                "pregnancy": "Yoʻq"
            }
            st.session_state.animals = pd.concat([animals, pd.DataFrame([row])], ignore_index=True)
            st.success(f"✅ {new_id} muvaffaqiyatli qoʻshildi!")
            st.rerun()

# ======================== HAYVON PASPORTI ========================
elif page == "Hayvon pasporti":
    st.markdown("""
    <div class="section-desc">
        🪪 <b>Raqamli hayvon pasporti</b> — har bir hayvonning to'liq ma'lumotlari: ID, zoti, jinsi, yoshi, 
        vazni, sut mahsuldorligi, ota-ona ma'lumotlari, emlash va naslchilik holati.
    </div>
    """, unsafe_allow_html=True)

    selected = st.selectbox("Hayvonni tanlang", animals["id"].tolist())
    a = animals[animals["id"] == selected].iloc[0]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("ID", a["id"])
    c2.metric("Zot", a["breed"])
    c3.metric("Vazn", f'{a["weight"]} kg')
    c4.metric("Sut", f'{a["milk"]} L/kun')

    st.divider()
    left, right = st.columns(2)
    with left:
        st.write("Asosiy maʼlumotlar")
        st.write(f"Jinsi: {a['sex']}")
        st.write(f"Yoshi: {a['age']} yosh")
        st.write(f"Emlash: {a['vaccination']}")
        st.write(f"Sog'liq holati: {a.get('health_status', 'Nomaʼlum')}")
    with right:
        st.write("Nasl maʼlumotlari")
        st.write(f"Ota: {a['father']}")
        st.write(f"Ona: {a['mother']}")
        st.write(f"Holati: {a['breeding_status']}")
        st.write(f"Boʻgʻozlik: {a.get('pregnancy', 'Nomaʼlum')}")

    st.info("📌 QR-kod moduli keyingi versiyada ulanadi.")

# ======================== SUT & VAZN ========================
elif page == "Sut & vazn":
    st.markdown("""
    <div class="section-desc">
        🥛 <b>Sut & vazn monitoringi</b> — tanlangan hayvonning sut mahsuldorligi va vazn dinamikasini 
        interaktiv grafiklar orqali kuzatish. 14 kunlik demo tarix asosida tahlil.
    </div>
    """, unsafe_allow_html=True)

    female_ids = animals[animals["sex"] == "Urgʻochi"]["id"].tolist()
    if not female_ids:
        st.warning("Urgʻochi hayvonlar mavjud emas.")
    else:
        selected = st.selectbox("Hayvon", female_ids)
        a = animals[animals["id"] == selected].iloc[0]

        days = pd.date_range(end=pd.Timestamp.today(), periods=14)
        base = float(a["milk"])
        demo_data = pd.DataFrame({
            "Sana": days,
            "Sut (L)": [round(base + ((i % 5) - 2) * 0.7, 1) for i in range(14)],
            "Vazn (kg)": [int(a["weight"] - 5 + i * 0.4) for i in range(14)]
        }).set_index("Sana")

        st.write(f"{a['id']} — {a['breed']} hayvoni uchun ma'lumotlar")

        c1, c2 = st.columns(2)
        with c1:
            st.write("Sut dinamikasi")
            fig = px.line(demo_data, y='Sut (L)', title='Sut dinamikasi',
                          color_discrete_sequence=['#4ecdc4'])
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                              font=dict(color='#b8cfc3'))
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            st.write("Vazn dinamikasi")
            fig = px.line(demo_data, y='Vazn (kg)', title='Vazn dinamikasi',
                          color_discrete_sequence=['#8cffc3'])
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                              font=dict(color='#b8cfc3'))
            st.plotly_chart(fig, use_container_width=True)

        st.caption("📌 Grafiklar MVP namoyishi uchun generatsiya qilingan demo tarixidir.")

# ======================== NASLCHILIK AI ========================
elif page == "Naslchilik AI":
    st.markdown("""
    <div class="section-desc">
        🧬 <b>Naslchilik AI</b> — tanlangan sigir uchun eng mos naslchilik nomzodlarini aniqlash. 
        Zot, mahsuldorlik, vazn va yosh asosida hisoblangan moslik skori.
    </div>
    """, unsafe_allow_html=True)

    females = animals[animals["sex"] == "Urgʻochi"]
    if females.empty:
        st.warning("Urgʻochi hayvonlar mavjud emas.")
    else:
        selected = st.selectbox("Sigirni tanlang", females["id"].tolist())
        cow = females[females["id"] == selected].iloc[0]

        st.markdown('<div class="ai-box">🤖 <b>AI demo tahlili</b><br>Quyidagi tavsiya zot, mahsuldorlik, vazn va nasl maʼlumotlari asosida qoidaviy model bilan hisoblanadi.</div>', unsafe_allow_html=True)

        st.write(f"Tanlangan sigir: {cow['id']} — {cow['breed']}, sut: {cow['milk']} L/kun")

        candidates = animals[animals["sex"] == "Erkak"].copy()
        if candidates.empty:
            st.warning("Erkak hayvonlar mavjud emas.")
        else:
            candidates["score"] = 50
            candidates.loc[candidates["breed"] == cow["breed"], "score"] += 25
            candidates["score"] += ((candidates["weight"] - 450).abs().clip(upper=150) * -0.08)
            candidates["score"] += (candidates["age"].between(3, 6).astype(int) * 10)
            candidates = candidates.sort_values("score", ascending=False)
            best = candidates.iloc[0]

            st.success(f"✅ Tavsiya etilayotgan demo nomzod: {best['id']} — {best['breed']}, moslik skori: {best['score']:.0f}/100")
            st.dataframe(candidates[["id", "breed", "age", "weight", "score"]].head(5),
                         use_container_width=True, hide_index=True)
            st.warning("⚠️ Bu veterinariya/genetik tashxis emas. Real mahsulotda naslchilik mutaxassisi va laboratoriya maʼlumotlari bilan validatsiya qilinadi.")

# ======================== AI ASSISTANT ========================
elif page == "AI Assistant":
    st.markdown("""
    <div class="section-desc">
        🤖 <b>AI Farm Assistant</b> — sun'iy intellekt yordamida ferma haqida savollarga javob olish. 
        "Sut", "mahsuldor", "vazn" yoki "nasl" kalit so'zlari bilan so'rang.
    </div>
    """, unsafe_allow_html=True)

    question = st.text_area("Savolingizni yozing", placeholder="Masalan: Qaysi sigirlar eng mahsuldor?")
    if st.button("🔍 Tahlil qilish"):
        if not question.strip():
            st.warning("Iltimos, savol kiriting.")
        else:
            q = question.lower()
            females = animals[animals["sex"] == "Urgʻochi"]
            if "mahsuldor" in q or "sut" in q:
                top = females.sort_values("milk", ascending=False).head(5) if not females.empty else pd.DataFrame()
                if not top.empty:
                    st.write("✅ Eng yuqori sut koʻrsatkichlari:")
                    st.dataframe(top[["id", "breed", "milk", "weight"]], use_container_width=True, hide_index=True)
            elif "vazn" in q:
                heavy = animals.sort_values("weight", ascending=False).head(5)
                st.write("✅ Eng yuqori vaznli hayvonlar:")
                st.dataframe(heavy[["id", "breed", "sex", "weight"]], use_container_width=True, hide_index=True)
            elif "nasl" in q or "urug" in q:
                st.write("🧬 Naslchilik boʻlimida hayvonni tanlang — tizim mavjud demo maʼlumotlar asosida mos nomzodlarni reyting qiladi.")
            else:
                st.info("📌 Demo AI: savolni “sut”, “mahsuldor”, “vazn” yoki “nasl” kalit soʻzlari bilan bering.")

# ======================== AGROGEN AI QANDAY ISHLAYDI ========================
st.divider()
st.subheader("🧠 AgroGen AI qanday ishlaydi?")

col1, col2 = st.columns([1, 2])
with col1:
    st.markdown("""


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
    
 """)

with col2:
    st.markdown("""
1. 🐄 HAYVON – Har bir hayvon tizimga kiritiladi. 
2. 📋 MA'LUMOTLAR – Zoti, yoshi, vazni, sog'lig'i yoziladi. 
3. 🗄️ RAQAMLI BAZA – Barcha ma'lumotlar xavfsiz saqlanadi. 
4. 📊 TAHLIL – AI va statistika modellari tahlil qiladi. 
5. 🧠 AI MODEL – Mahsuldorlik va naslchilik potentsiali baholanadi. 
6. 💡 TAVSIYA / SIGNAL – Fermerga tavsiyalar yoki xavf signali beriladi. 
7. 👨‍🌾 FERMER – Fermer qaror qabul qiladi va amalga oshiradi.
""")

# ======================== FAQ ========================
st.divider()
with st.expander("❓ Tez-tez beriladigan savollar"):
st.markdown("""
1. AgroGen AI qanday ishlaydi? 
→ Hayvon ma'lumotlarini kiritasiz, tizim ularni tahlil qiladi va tavsiyalar beradi.

2. Ma'lumotlar qayerda saqlanadi? 
→ Hozircha JSON faylda, kelajakda PostgreSQL ulanishi rejalashtirilgan.

3. AI modeli qanday o'rgatilgan? 
→ Hozircha qoidaviy tizim, kelajakda ML modeli o'rnatiladi.

4. Ilovani qanday ishga tushirish mumkin? 
→ pip install -r requirements.txt va streamlit run app.py

5. Ma'lumotlarni eksport qilsa bo'ladimi? 
→ Ha, "Hayvonlar" bo'limida CSV yuklab olish mumkin.
""")

# ======================== SHARHLAR ========================
st.subheader("⭐ Foydalanuvchi sharhlari")
col1, col2 = st.columns(2)

with col1:
st.markdown("""
<div class="testimonial">
<div class="name">🧑‍🌾 Alisher Xo'jayev</div>
<div>"AgroGen AI yordamida fermamdagi barcha hayvonlarni bir tizimda boshqarish imkoniga ega bo'ldim. Juda qulay!"</div>
<div class="stars">⭐⭐⭐⭐⭐</div>
</div>
""", unsafe_allow_html=True)

with col2:
st.markdown("""
<div class="testimonial">
<div class="name">👩‍🌾 Dilorom Qodirova</div>
<div>"Naslchilik AI bo'limi menga eng yaxshi sigirlarni tanlashda yordam berdi. Mahsuldorlik 20% ga oshdi!"</div>
<div class="stars">⭐⭐⭐⭐⭐</div>
</div>
""", unsafe_allow_html=True)

# ======================== QO'LLAB-QUVVATLASH ========================
st.divider()
st.subheader("☕ Qo'llab-quvvatlash")
st.markdown("""
Agar loyiham sizga foydali bo'lsa, quyidagi orqali qo'llab-quvvatlashingiz mumkin:

- 💳 PayMe: +998 97 373 93 99
- 🏦 Bank kartasi: 9860 6004 0506 3766
- 🌐 GitHub Sponsor: [github.com/sponsors/Jaloldin007](https://github.com/sponsors/Jaloldin007)
""")

# ======================== BIO ========================
st.divider()
st.subheader("👨‍💻 Muallif haqida")
st.markdown("""
Jaloldin007 — AgroGen AI asoschisi. 
Chorvachilik va sun'iy intellekt sohalarida faoliyat yuritadi.

📧 Email: shahandtel265@gmail.com 
🔗 GitHub: [github.com/Jaloldin007](https://github.com/Jaloldin007) 
🌐 Loyiha: [AgroGen AI](https://agrogen-ai.streamlit.app)
""")

# ======================== FOOTER ========================
st.divider()
st.markdown('<div class="footer">🌱 Kelajak nasli — bugundan boshlanadi. | AgroGen AI MVP</div>', unsafe_allow_html=True)
