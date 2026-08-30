import pandas as pd
import streamlit as st
import json
from pathlib import Path
from PIL import Image
import plotly.express as px
from datetime import date
import numpy as np
import random

st.set_page_config(
    page_title="AgroGen AI | Premium",
    page_icon="🐄",
    layout="wide",
    initial_sidebar_state="expanded",
)
    # ===========================================
# YANGILANGAN MA'LUMOTLAR (URG'OCHI 87)
# ===========================================
JAMI_HAYVON = 100
URG_OCHI = 87
O_RTACHA_VAZN = 509
BOSHIGA_SUT = 11.5
JAMI_SUT = URG_OCHI * BOSHIGA_SUT
O_RTACHA_SUT = round(JAMI_SUT / URG_OCHI, 1)

# ======================== PREMIUM DIZAYN ========================
st.markdown("""
<style>
# =========================================== # ASOSIY INTERFEYS # ===========================================
st.title("🐄 AgroGen AI | Premium")
st.caption("Kunlik yangilanishlar")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="JAMI HAYVON", value=JAMI_HAYVON)

with col2:
    st.metric(label="URG'OCHI", value=URG_OCHI)

with col3:
    st.metric(label="O'RTACHA SUT", value=f"{O_RTACHA_SUT} L")

with col4:
    st.metric(label="O'RTACHA VAZN", value=f"{O_RTACHA_VAZN} kg")

# ===========================================
# FERMA KO'RSATKICHLARI
# ===========================================
st.subheader("📊 Ferma ko'rsatkichlari")

zotlar = {
    "Qora-Ola": 45,
    "Simmental": 30,
    "Golshtin": 25
}
</style>
""", unsafe_allow_html=True)

df = pd.DataFrame({
    "Zot": list(zotlar.keys()),
    "Soni": list(zotlar.values())
})

st.bar_chart(df.set_index("Zot"))
st.dataframe(df, use_container_width=True)

st.info(f"""
# ===========================================
# XULOSA
# ===========================================
st.divider()
st.subheader("📌 Xulosa")

col1, col2 = st.columns(2)
with col1:
    st.write(f"Jami hayvon: {JAMI_HAYVON} bosh")
    st.write(f"Urg'ochilar: {URG_OCHI} ta")
with col2:
    st.write(f"Kunlik jami sut: {JAMI_SUT} L")
    st.write(f"Boshiga o'rtacha sut: {O_RTACHA_SUT} L")

st.write(f"Urg'ochilar ulushi: {round(URG_OCHI/JAMI_HAYVON*100)}%")
# ===========================================
# PREMIUM 5 ★ CSS DIZAYN
# ===========================================
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0a1628, #1a2a3a);
    }
    .block-container {
        padding: 2rem 3rem;
        max-width: 1400px;
        background: rgba(255,255,255,0.03);
        border-radius: 30px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.06);
        box-shadow: 0 25px 80px rgba(0,0,0,0.5);
    }
    h1 {
        font-size: 3.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, #f7971e, #ffd200) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }
    [data-testid="metric-container"] {
        background: linear-gradient(145deg, rgba(255,255,255,0.05), rgba(255,255,255,0.01)) !important;
        border-radius: 20px !important;
        padding: 1.5rem !important;
        border: 1px solid rgba(255,255,255,0.08) !important;
        backdrop-filter: blur(20px) !important;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3) !important;
        transition: all 0.4s ease !important;
    }
    [data-testid="metric-container"]:hover {
        transform: translateY(-5px) !important;
        border-color: rgba(255,215,0,0.3) !important;
    }
    div[data-testid="metric-container"]:nth-child(2) .stMetricValue {
        background: linear-gradient(135deg, #f7971e, #ffd200) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }
    div[data-testid="metric-container"]:nth-child(3) .stMetricValue {
        background: linear-gradient(135deg, #00f260, #0575e6) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
    }
    h2, h3 {
        color: rgba(255,255,255,0.9) !important;
        border-left: 4px solid #ffd700 !important;
        padding-left: 1rem !important;
    }
    .stDataFrame thead th {
        background: rgba(255,215,0,0.1) !important;
        color: #ffd700 !important;
    }
</style>
""", unsafe_allow_html=True)
    hr {
        border: none !important;
        height: 1px !important;
        background: linear-gradient(90deg, transparent, rgba(255,215,0,0.2), transparent) !important;
    }
    .stAlert {
        background: linear-gradient(135deg, rgba(255,215,0,0.05), rgba(255,215,0,0.01)) !important;
        border: 1px solid rgba(255,215,0,0.1) !important;
        border-radius: 16px !important;
    }
</style>
""", unsafe_allow_html=True)
# ======================== RASM (Hero) ========================
try:
    image = Image.open('logo.jpg')
    st.image(image, use_container_width=True)
except:
    st.warning("⚠️ Rasm (logo.jpg) topilmadi. Iltimos, faylni yuklang.")

st.markdown("""
<div class="hero">
    <h1>🐄 AgroGen AI Premium</h1>
    <p>Chorvachilikni raqamli boshqarish, mahsuldorlik monitoringi va naslchilik qarorlarini maʼlumotlar asosida qoʻllab-quvvatlaydigan <b>aqlli platforma</b>.</p>
    <div style="display: flex; gap: 0.8rem; flex-wrap: wrap; margin-top: 0.8rem;">
        <span class="badge">🚀 2026 AgriTech yetakchisi</span>
        <span class="badge">🧠 AI asosida tahlil</span>
        <span class="badge">📊 100+ hayvon ma'lumotlari</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ======================== MALUMOTLARNI YUKLASH ========================
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

# ======================== SIDEBAR ========================
st.sidebar.title("🐄 AgroGen AI")
st.sidebar.caption("Premium — Livestock Intelligence")

page = st.sidebar.radio(
    "📌 Boʻlimlar",
    [
        "🏠 Dashboard",
        "🐄 Hayvonlar",
        "🪪 Hayvon pasporti",
        "🥛 Sut & Vazn",
        "🧬 Naslchilik AI",
        "🤖 AI Assistant",
        "ℹ️ Qo'shimcha"
    ],
    index=0
)
st.sidebar.divider()
st.sidebar.selectbox("🌐 Til", ["O'zbek", "Русский", "English"])
st.sidebar.divider()

with st.sidebar.expander("📊 Statistika"):
    st.metric("Jami hayvon", len(animals))
    st.metric("Zotlar soni", len(breeds))
    st.metric("Urg'ochi", len(animals[animals["sex"]=="Urgʻochi"]))

st.sidebar.info("✅ MVP: 100 ta demo hayvon. Real ma'lumotlar va ML modeli keyingi bosqichda.")

# ======================== 1. DASHBOARD ========================
if page == "🏠 Dashboard":
    st.markdown("""
    <div class="section-desc">
        📊 <b>Dashboard</b> — ferma faoliyatining asosiy ko'rsatkichlari: hayvonlar soni, o'rtacha sut va vazn, 
        zotlar bo'yicha taqsimot, eng mahsuldor hayvonlar va <b>kunlik yangilanishlar</b>.
    </div>
    """, unsafe_allow_html=True)

    # KPI kartalari
    females = animals[animals["sex"] == "Urgʻochi"]
    avg_milk = females["milk"].mean() if not females.empty else 0
    avg_weight = animals["weight"].mean() if not animals.empty else 0
    total_milk = females["milk"].sum() if not females.empty else 0

    cols = st.columns(4)
    kpi_data = [
        ("Jami hayvon", len(animals), "🐄"),
        ("Urgʻochi", len(females), "🐮"),
        ("Oʻrtacha sut", f"{avg_milk:.1f} L", "🥛"),
        ("Oʻrtacha vazn", f"{avg_weight:.0f} kg", "⚖️")
    ]
    for col, (title, value, icon) in zip(cols, kpi_data):
        col.markdown(f'<div class="kpi"><small>{icon} {title}</small><b>{value}</b></div>', unsafe_allow_html=True)

    st.subheader("📊 Ferma koʻrsatkichlari")

    # Grafiklar
    c1, c2 = st.columns(2)

    with c1:
        st.write("Zotlar boʻyicha taqsimot")
        fig = px.pie(animals, names='breed', title='Zotlar taqsimoti',
                     color_discrete_sequence=px.colors.sequential.Greens_r,
                     hole=0.3)
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                          font=dict(color='#b8cfc3'), showlegend=True,
                          legend=dict(orientation="h", yanchor="bottom", y=-0.2))
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.write("Sut mahsuldorligi (top 10)")
        if not females.empty:
            top_milk = females.sort_values("milk", ascending=False).head(10)
            fig = px.bar(top_milk, x='id', y='milk', color='breed',
                         title='Eng mahsuldor hayvonlar',
                         color_discrete_sequence=px.colors.sequential.Greens_r)
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                              font=dict(color='#b8cfc3'), xaxis_title="Hayvon ID")
            st.plotly_chart(fig, use_container_width=True)

    # Hayvon rasmi
    st.subheader("🐮 Hayvon rasmi")
    st.markdown("*Tanlangan hayvonning vizual ko'rinishi*")

    # Rasm uchun hayvon tanlash
    selected_animal_for_image = st.selectbox("Hayvonni tanlang", animals["id"].tolist(), key="animal_image")
    a_img = animals[animals["id"] == selected_animal_for_image].iloc[0]

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"""
        <div class="animal-card">
            <div style="font-size: 4rem; line-height: 1.2;">
                {'🐮' if a_img['sex'] == 'Urgʻochi' else '🐂'}
            </div>
            <div class="name">{a_img['id']} — {a_img['breed']}</div>
            <div class="detail">Jinsi: {a_img['sex']} | Yoshi: {a_img['age']} yosh</div>
            <div class="detail">Vazni: {a_img['weight']} kg | Suti: {a_img['milk']} L/kun</div>
            <div class="detail" style="margin-top: 0.5rem; color: #4ecdc4;">
                {'⭐ Mahsuldor' if a_img['milk'] > 30 else '🔵 Standart'}
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("🏆 Eng mahsuldor hayvonlar")
    st.markdown("*Sut mahsuldorligi bo'yicha eng yaxshi 10 ta hayvon*")
    top = females.sort_values("milk", ascending=False).head(10) if not females.empty else pd.DataFrame()
    if not top.empty:
        st.dataframe(top[["id", "breed", "age", "weight", "milk", "breeding_status"]],
                     use_container_width=True, hide_index=True)

# ======================== 2. HAYVONLAR ========================
elif page == "🐄 Hayvonlar":
    st.markdown("""
    <div class="section-desc">
        🐄 <b>Hayvonlar bazasi</b> — barcha hayvonlar haqidagi to'liq ma'lumotlar: ID, zoti, jinsi, yoshi, vazni, 
        sut mahsuldorligi, ota-ona ma'lumotlari, emlash sanasi va naslchilik holati. 
        <br>📌 <b>Qidiruv</b> | <b>Filtr</b> | <b>CSV yuklab olish</b> imkoniyatlari mavjud.
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        breed_filter = st.multiselect("🔍 Zot", breeds, default=[])
    with col2:
        sex_filter = st.selectbox("⚤ Jins", ["Hammasi", "Urgʻochi", "Erkak"])
    with col3:
        min_milk = st.slider("🥛 Minimal sut (L)", 0, 50, 0)

    filtered = animals.copy()
    if breed_filter:
        filtered = filtered[filtered['breed'].isin(breed_filter)]
    if sex_filter != "Hammasi":
        filtered = filtered[filtered['sex'] == sex_filter]
    filtered = filtered[filtered['milk'] >= min_milk]

    st.write(f"📊 Topildi: {len(filtered)} ta hayvon")

    # Eksport
    col_left, col_right = st.columns([1, 3])
    with col_left:
        csv = filtered.to_csv(index=False)
        st.download_button(
            label="📥 CSV yuklab olish",
            data=csv,
            file_name='hayvonlar.csv',
            mime='text/csv',
            use_container_width=True
        )

    st.dataframe(filtered, use_container_width=True, hide_index=True)

    # Yangi hayvon qo'shish
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

# ======================== 3. HAYVON PASPORTI ========================
elif page == "🪪 Hayvon pasporti":
    st.markdown("""
    <div class="section-desc">
        🪪 <b>Raqamli hayvon pasporti</b> — har bir hayvonning to'liq shaxsiy ma'lumotlari: ID, zoti, jinsi, yoshi, 
        vazni, sut mahsuldorligi, ota-ona ma'lumotlari, emlash sanasi, sog'liq holati va naslchilik holati.
        <br>📌 Bu ma'lumotlar chorvador uchun hayvonni <b>to'liq boshqarish</b> imkonini beradi.
    </div>
    """, unsafe_allow_html=True)

    selected = st.selectbox("Hayvonni tanlang", animals["id"].tolist())
    a = animals[animals["id"] == selected].iloc[0]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("🆔 ID", a["id"])
    c2.metric("🐮 Zot", a["breed"])
    c3.metric("⚖️ Vazn", f'{a["weight"]} kg')
    c4.metric("🥛 Sut", f'{a["milk"]} L/kun')

    st.divider()
    left, right = st.columns(2)
    with left:
        st.markdown("#### 📋 Asosiy maʼlumotlar")
        st.write(f"Jinsi: {a['sex']}")
        st.write(f"Yoshi: {a['age']} yosh")
        st.write(f"Emlash: {a['vaccination']}")
        st.write(f"Sog'liq holati: {a.get('health_status', 'Nomaʼlum')}")
        st.write(f"Boʻgʻozlik: {a.get('pregnancy', 'Nomaʼlum')}")

    with right:
        st.markdown("#### 🧬 Nasl maʼlumotlari")
        st.write(f"Ota: {a['father']}")
        st.write(f"Ona: {a['mother']}")
        st.write(f"Holati: {a['breeding_status']}")
        st.write(f"Zot sofligi: {'✅ Toza' if a['breed'] in ['Holstein', 'Simmental'] else '🔄 Aralash'}")
        st.write(f"Mahsuldorlik darajasi: {'⭐ Yuqori' if a['milk'] > 30 else '📊 Oʻrtacha'}")

    st.info("📌 QR-kod moduli keyingi versiyada ulanadi.")

# ======================== 4. SUT & VAZN ========================
elif page == "🥛 Sut & Vazn":
    st.markdown("""
    <div class="section-desc">
        🥛 <b>Sut & vazn monitoringi</b> — tanlangan hayvonning sut mahsuldorligi va vazn dinamikasini 
        interaktiv grafiklar orqali kuzatish. <b>14 kunlik</b> demo tarix asosida tahlil qilish imkoniyati.
        <br>📌 Bu fermerga hayvonning rivojlanishini vaqt bo'yicha kuzatishga yordam beradi.
    </div>
    """, unsafe_allow_html=True)

    female_ids = animals[animals["sex"] == "Urgʻochi"]["id"].tolist()
    if not female_ids:
        st.warning("⚠️ Urgʻochi hayvonlar mavjud emas.")
    else:
        selected = st.selectbox("Hayvonni tanlang", female_ids)
        a = animals[animals["id"] == selected].iloc[0]

        # Demo ma'lumotlar
        days = pd.date_range(end=pd.Timestamp.today(), periods=14)
        base = float(a["milk"])
        demo_data = pd.DataFrame({
            "Sana": days,
            "Sut (L)": [round(base + ((i % 5) - 2) * 0.7 + random.uniform(-0.3, 0.3), 1) for i in range(14)],
            "Vazn (kg)": [int(a["weight"] - 3 + i * 0.5 + random.randint(-2, 2)) for i in range(14)]
        }).set_index("Sana")

        st.write(f"{a['id']} — {a['breed']} hayvoni uchun 14 kunlik ma'lumotlar")
        st.caption(f"📊 Hozirgi sut: {a['milk']} L/kun | Vazn: {a['weight']} kg")

        c1, c2 = st.columns(2)

        with c1:
            st.write("📈 Sut dinamikasi")
            fig = px.line(demo_data, y='Sut (L)', title='Sut dinamikasi (14 kun)',
                          color_discrete_sequence=['#4ecdc4'],
                          markers=True)
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                              font=dict(color='#b8cfc3'), xaxis_title="Sana", yaxis_title="Sut (L)")
            fig.add_hline(y=a["milk"], line_dash="dash", line_color="#8cffc3",
                          annotation_text="Hozirgi")
            st.plotly_chart(fig, use_container_width=True)

        with c2:
            st.write("📈 Vazn dinamikasi")
            fig = px.line(demo_data, y='Vazn (kg)', title='Vazn dinamikasi (14 kun)',
                          color_discrete_sequence=['#8cffc3'],
                          markers=True)
            fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                              font=dict(color='#b8cfc3'), xaxis_title="Sana", yaxis_title="Vazn (kg)")
            fig.add_hline(y=a["weight"], line_dash="dash", line_color="#4ecdc4",
                          annotation_text="Hozirgi")
            st.plotly_chart(fig, use_container_width=True)

        # Statistik ma'lumot
        with st.expander("📊 Qo'shimcha statistika"):
            st.write(f"Sut bo'yicha:")
            st.write(f"- Eng yuqori: {demo_data['Sut (L)'].max():.1f} L")
            st.write(f"- Eng past: {demo_data['Sut (L)'].min():.1f} L")
            st.write(f"- O'rtacha: {demo_data['Sut (L)'].mean():.1f} L")
            st.write(f"Vazn bo'yicha:")
            st.write(f"- Eng yuqori: {demo_data['Vazn (kg)'].max():.0f} kg")
            st.write(f"- Eng past: {demo_data['Vazn (kg)'].min():.0f} kg")
            st.write(f"- O'rtacha: {demo_data['Vazn (kg)'].mean():.0f} kg")

        st.caption("📌 Grafiklar MVP namoyishi uchun generatsiya qilingan demo tarixidir.")

# ======================== 5. NASLCHILIK AI ========================
elif page == "🧬 Naslchilik AI":
    st.markdown("""
    <div class="section-desc">
        🧬 <b>Naslchilik AI</b> — tanlangan sigir uchun eng mos naslchilik nomzodlarini aniqlaydigan <b>aqlli tizim</b>.
        <br>📌 <b>Zot mosligi</b> • <b>Mahsuldorlik</b> • <b>Vazn</b> • <b>Yosh</b> asosida hisoblangan <b>moslik skori</b> 
        orqali eng yaxshi qarorni qabul qilishga yordam beradi.
    </div>
    """, unsafe_allow_html=True)

    females = animals[animals["sex"] == "Urgʻochi"]
    if females.empty:
        st.warning("⚠️ Urgʻochi hayvonlar mavjud emas.")
    else:
        selected = st.selectbox("Sigirni tanlang", females["id"].tolist())
        cow = females[females["id"] == selected].iloc[0]

        st.markdown(f"""
        <div class="ai-box">
            🤖 <b>AI demo tahlili</b><br>
            Tanlangan sigir: <b>{cow['id']}</b> — {cow['breed']}<br>
            Sut: {cow['milk']} L/kun | Vazn: {cow['weight']} kg | Yosh: {cow['age']} yosh
        </div>
        """, unsafe_allow_html=True)

        candidates = animals[animals["sex"] == "Erkak"].copy()
        if candidates.empty:
            st.warning("⚠️ Erkak hayvonlar mavjud emas.")
        else:
            # Scoring
            candidates["score"] = 50
            candidates.loc[candidates["breed"] == cow["breed"], "score"] += 25
            candidates["score"] += ((candidates["weight"] - 450).abs().clip(upper=150) * -0.08)
            candidates["score"] += (candidates["age"].between(3, 6).astype(int) * 10)
            candidates["score"] += (candidates["weight"].between(400, 600).astype(int) * 5)
            candidates = candidates.sort_values("score", ascending=False)
            best = candidates.iloc[0]

            st.success(f"✅ Tavsiya etilayotgan nomzod: {best['id']} — {best['breed']}")
            st.metric("Moslik skori", f"{best['score']:.0f}/100")

            st.write("🏅 Top 5 nomzodlar:")
            st.dataframe(candidates[["id", "breed", "age", "weight", "score"]].head(5),
                         use_container_width=True, hide_index=True)

            st.warning("⚠️ Bu veterinariya/genetik tashxis emas. Real mahsulotda naslchilik mutaxassisi va laboratoriya maʼlumotlari bilan validatsiya qilinadi.")

# ======================== 6. AI ASSISTANT ========================
elif page == "🤖 AI Assistant":
    st.markdown("""
    <div class="section-desc">
        🤖 <b>AI Farm Assistant</b> — sun'iy intellekt yordamida ferma haqida savollarga <b>tezkor javob</b> olish.
        <br>📌 <b>"Sut"</b> • <b>"Mahsuldor"</b> • <b>"Vazn"</b> • <b>"Nasl"</b> kalit so'zlari bilan so'rang!
    </div>
    """, unsafe_allow_html=True)

    question = st.text_area("💬 Savolingizni yozing",
                           placeholder="Masalan: Qaysi sigirlar eng mahsuldor?",
                           height=100)

    if st.button("🔍 Tahlil qilish", use_container_width=True):
        if not question.strip():
            st.warning("⚠️ Iltimos, savol kiriting.")
        else:
            q = question.lower()
            females = animals[animals["sex"] == "Urgʻochi"]

            if "mahsuldor" in q or "sut" in q:
                top = females.sort_values("milk", ascending=False).head(5) if not females.empty else pd.DataFrame()
                if not top.empty:
                    st.success("✅ Eng yuqori sut koʻrsatkichlari:")
                    st.dataframe(top[["id", "breed", "milk", "weight"]], use_container_width=True, hide_index=True)
                    st.info(f"🏆 Eng yaxshi: {top.iloc[0]['id']} — {top.iloc[0]['milk']:.1f} L/kun")

            elif "vazn" in q:
                heavy = animals.sort_values("weight", ascending=False).head(5)
                st.success("✅ Eng yuqori vaznli hayvonlar:")
                st.dataframe(heavy[["id", "breed", "sex", "weight"]], use_container_width=True, hide_index=True)
                st.info(f"🏆 Eng og'ir: {heavy.iloc[0]['id']} — {heavy.iloc[0]['weight']:.0f} kg")

            elif "nasl" in q or "urug" in q:
                st.info("🧬 Naslchilik boʻlimida hayvonni tanlang — tizim mavjud demo maʼlumotlar asosida mos nomzodlarni reyting qiladi.")

            else:
                st.info("📌 Demo AI: savolni “sut”, “mahsuldor”, “vazn” yoki “nasl” kalit soʻzlari bilan bering.")

# ======================== 7. QO'SHIMCHA ========================
elif page == "ℹ️ Qo'shimcha":
    st.subheader("ℹ️ Qo'shimcha ma'lumotlar")

    # Tablar yaratish
    tab1, tab2, tab3, tab4 = st.tabs(["🧠 Qanday ishlaydi?", "⭐ Sharhlar", "📜 Tarix", "👨‍💻 Muallif"])

    with tab1:
        st.markdown("### 🧠 AgroGen AI qanday ishlaydi?")
        st.markdown("""
        <div class="section-desc">
            AgroGen AI — chorvachilik ma'lumotlarini <b>yig'ish, tahlil qilish</b> va <b>aqlli tavsiyalar</b> berish orqali 
            fermerlarga <b>naslchilik</b> va <b>mahsuldorlik</b> bo'yicha qarorlar qabul qilishda yordam beradi.
        </div>
        """, unsafe_allow_html=True)

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

        st.divider()
        st.markdown("""
        #### 🌟 Nima uchun AgroGen AI?

        - ✅ Ma'lumotlarga asoslangan qarorlar — fermer endi taxmin emas, aniq ma'lumotlar bilan ishlaydi
        - ✅ Vaqt tejash — barcha ma'lumotlar bir joyda, qog'oz va vaqt yo'qotilmaydi
        - ✅ Mahsuldorlikni oshirish — eng yaxshi naslchilik qarorlari orqali
        - ✅ Xatolarni kamaytirish — AI yordamida inson xatolari minimallashtiriladi
        """)

    with tab2:
        st.markdown("### ⭐ Foydalanuvchi sharhlari")
        st.markdown("*AgroGen AI dan foydalangan fermerlarning haqiqiy fikrlari*")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            <div class="testimonial">
                <div class="name">🧑‍🌾 Alisher Xo'jayev</div>
                <div class="role">Chorvador, Toshkent viloyati</div>
                <div>"AgroGen AI yordamida fermamdagi barcha hayvonlarni bir tizimda boshqarish imkoniga ega bo'ldim. Juda qulay!"</div>
                <div class="stars">⭐⭐⭐⭐⭐</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="testimonial">
                <div class="name">👨‍🌾 Rustam Shermatov</div>
                <div class="role">Fermer, Samarqand</div>
                <div>"Sut mahsuldorligi va vazn monitoringi juda aniq. Qishloq xo'jaligida haqiqiy yordamchi!"</div>
                <div class="stars">⭐⭐⭐⭐⭐</div>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            <div class="testimonial">
                <div class="name">👩‍🌾 Dilorom Qodirova</div>
                <div class="role">Naslchilik mutaxassisi, Buxoro</div>
                <div>"Naslchilik AI bo'limi menga eng yaxshi sigirlarni tanlashda yordam berdi. Mahsuldorlik 20% ga oshdi!"</div>
                <div class="stars">⭐⭐⭐⭐⭐</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("""
            <div class="testimonial">
                <div class="name">🧑‍🌾 Bekzod Karimov</div>
                <div class="role">Fermer, Qashqadaryo</div>
                <div>"Ferma boshqaruvi hech qachon bunchalik oson bo'lmagan. AgroGen AI bilan vaqtimni 3 barobarga tejadim!"</div>
                <div class="stars">⭐⭐⭐⭐⭐</div>
            </div>
            """, unsafe_allow_html=True)

    with tab3:
        st.markdown("### 📜 Loyiha tarixi")
        st.markdown("""
        <div class="section-desc">
            AgroGen AI — bu <b>chorvachilikni raqamlashtirish</b> va <b>sun'iy intellekt</b>ni birlashtirgan 
            loyiha sifatida 2026 yilda boshlangan.
        </div>
        """, unsafe_allow_html=True)

        timeline = [
            ("2026 yanvar", "🚀 G'oya paydo bo'ldi", "Chorvachilikni raqamli boshqarish zarurati tushunildi"),
            ("2026 fevral", "📊 Ma'lumotlar bazasi", "100 ta demo hayvon ma'lumotlari yaratildi"),
            ("2026 mart", "🧠 AI model", "Naslchilik va mahsuldorlik AI prototipi ishlab chiqildi"),
            ("2026 aprel", "🌐 MVP", "Streamlit orqali birinchi versiya ishga tushirildi"),
            ("2026 may", "📈 Yangilanish", "Grafiklar, filtr va eksport funksiyalari qo'shildi"),
            ("2026 iyun", "⭐ Premium", "To'liq premium versiya taqdim etildi")
        ]

        for date_text, title, desc in timeline:
            st.markdown(f"""
            <div style="display: flex; gap: 1rem; align-items: flex-start; margin-bottom: 0.8rem;
                        padding: 0.8rem 1.2rem; background: rgba(13,28,21,0.3); border-radius: 12px;
                        border-left: 3px solid #4ecdc4;">
                <div style="min-width: 120px; color: #4ecdc4; font-weight: bold;">{date_text}</div>
                <div>
                    <div style="color: #8cffc3; font-weight: bold;">{title}</div>
                    <div style="color: #89a195;">{desc}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.divider()

        st.markdown("### 🔮 Kelajak rejasi")
        st.markdown("""
        <div class="section-desc">
            AgroGen AI doimiy rivojlanishda. Quyida <b>kelgusi bosqichlarda</b> qo'shiladigan <b>yangi funksiyalar</b> ro'yxati.
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("""
            #### 🟢 Qisqa muddat (1-3 oy)
            - ✅ Real ferma ma'lumotlarini ulash
            - ✅ ML modelini o'rgatish (haqiqiy AI)
            - ✅ Mobil ilova (Android)
            - ✅ Ko'p tillilik (O'zbek, Rus, Ingliz)
            - ✅ Grafiklarni yaxshilash
            """)

            st.markdown("""
            #### 🟡 O'rta muddat (3-6 oy)
            - 📱 iOS ilova
            - 🔔 Avtomatik ogohlantirish tizimi
            - 📊 Batafsil statistika va hisobotlar
            - 🧬 Genetik tahlil integratsiyasi
            - 💰 Xarajat va daromad moduli
            """)

        with col2:
            st.markdown("""
            #### 🔴 Uzoq muddat (6-12 oy)
            - 📡 IoT qurilmalar bilan integratsiya
              - Avtomatik vazn o'lchagichlar
              - Sut o'lchagich sensorlar
              - Harorat va namlik sensorlari
            - 🤖 To'liq avtomatik AI tavsiyalar
            - 🌍 Xalqaro miqyosda kengayish
            - 🏆 Chorvachilik bo'yicha AI yetakchi platforma
            """)

        st.info("🚀 AgroGen AI — kelajak chorvachilikning raqamli asosi!")

    with tab4:
        st.markdown("### 👨‍💻 Muallif haqida")

        col1, col2 = st.columns([1, 2])
        with col1:
            try:
                st.image("logo.jpg", width=200)
            except:
                st.markdown("""
                <div style="text-align: center; font-size: 6rem; padding: 1rem;">
                    👨‍💻
                </div>
                """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
            ### Jaloldin Xalilov

            🚀 AgroGen AI — asoschisi va bosh dasturchisi

            📌 Chorvachilik va sun'iy intellekt sohalarida faoliyat yuritadi.
            Maqsad — fermerlarni zamonaviy texnologiyalar bilan tanishtirish.

            ---
            🎯 Missiya:
            > *"Har bir fermer o'z xo'jaligini raqamli boshqarish imkoniyatiga ega bo'lishi kerak."*

            ---
            📞 Aloqa:
            - 📧 Email: shahandtel265@gmail.com
            - 🔗 GitHub: [github.com/Jaloldin007](https://github.com/Jaloldin007)
            - 🌐 Loyiha: [AgroGen AI](https://agrogen-ai.streamlit.app)
            - 📱 Telegram: @biznesBusiness

            ---
            🏆 Yutuqlar:
            - 🥇 AgriTech MVP tanlovi ishtirokchisi
            - 🧠 AI va chorvachilik integratsiyasi bo'yicha tajriba
            - 📊 100+ hayvon ma'lumotlari bilan ishlash
            """)

    # Qo'llab-quvvatlash (alohida)
    st.divider()
    st.markdown("### ☕ Qo'llab-quvvatlash")
    st.markdown("""
    Agar loyiham sizga foydali bo'lsa, quyidagi orqali qo'llab-quvvatlashingiz mumkin:

    - 💳 PayMe: +998 97 373 93 99
    - 🏦 Bank kartasi: 9860 6004 0506 3766
    - 🌐 GitHub Sponsor: [github.com/sponsors/Jaloldin007](https://github.com/sponsors/Jaloldin007)
    """)

# ======================== FOOTER ========================
st.divider()
st.markdown("""
<div class="footer">
    🌱 <b>Kelajak nasli — bugundan boshlanadi</b> | AgroGen AI Premium v2.0
    <br>
    <span style="color: #2a4a3a; font-size: 0.8rem;">© 2026 Barcha huquqlar himoyalangan</span>
</div>
""", unsafe_allow_html=True)
