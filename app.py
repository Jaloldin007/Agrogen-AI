import pandas as pd
import streamlit as st
import json
from pathlib import Path
import streamlit as st
from PIL import Image

# Rasmni yuklash
image = Image.open('logo.jpg')
st.image(image, use_container_width=True)

st.title("KELAJAK NASLI — BUGUNDAN BOSHLANADI")
st.write("AgroGen-AI loyihasiga xush kelibsiz!")
import json
from pathlib import Path
from datetime import date
import pandas as pd
import streamlit as st

st.set_page_config(page_title="AgroGen AI", page_icon="🐄", layout="wide")

DATA_FILE = Path("data/animals.json")

@st.cache_data
def load_animals():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return pd.DataFrame(json.load(f))

df = load_animals()

if "animals" not in st.session_state:
    st.session_state.animals = df.copy()

animals = st.session_state.animals
# Zotlar ro'yxati (animals.json dan avtomatik)
breeds = animals['breed'].unique().tolist()

st.markdown("""
<style>
.block-container {padding-top: 1.5rem; max-width: 1250px;}
.hero {padding: 1.4rem 1.6rem; border-radius: 18px; background: linear-gradient(135deg,#10251b,#173a27); margin-bottom: 1.2rem;}
.hero h1 {margin:0; font-size:2.5rem;}
.hero p {color:#b8cfc3; font-size:1.05rem;}
.kpi {padding:1rem; border:1px solid #254536; border-radius:14px; background:#0d1c15;}
.kpi small {color:#89a195;}
.kpi b {font-size:1.8rem;}
.ai {padding:1.1rem 1.3rem; border-radius:14px; background:#10251b; border:1px solid #355a43;}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🐄 AgroGen AI")
st.sidebar.caption("Livestock Intelligence — tanlov MVP")
page = st.sidebar.radio(
    "Bo‘lim",
    ["Dashboard", "Hayvonlar", "Hayvon pasporti", "Sut & vazn", "Naslchilik AI", "AI Assistant"]
)
st.sidebar.divider()
st.sidebar.info("MVP: 100 ta demo hayvon. Keyingi bosqichda real ferma ma’lumotlari va ML modeli ulanadi.")

st.markdown("""
<div class="hero">
<h1>🐄 AgroGen AI</h1>
<p>Chorvachilikni raqamli boshqarish, mahsuldorlik monitoringi va naslchilik qarorlarini ma’lumotlar asosida qo‘llab-quvvatlash.</p>
</div>
""", unsafe_allow_html=True)

if page == "Dashboard":
    females = animals[animals["sex"] == "Urg‘ochi"]
    avg_milk = females["milk"].mean()
    avg_weight = animals["weight"].mean()
    high = len(females[females["milk"] >= 30])

    cols = st.columns(4)
    for col, title, value in zip(
        cols,
        ["Jami hayvon", "Urg‘ochi", "O‘rtacha sut", "O‘rtacha vazn"],
        [len(animals), len(females), f"{avg_milk:.1f} L/kun", f"{avg_weight:.0f} kg"]
    ):
        col.markdown(f'<div class="kpi"><small>{title}</small><br><b>{value}</b></div>', unsafe_allow_html=True)

    st.subheader("📊 Ferma ko‘rsatkichlari")
    c1, c2 = st.columns(2)
    with c1:
        st.write("Zotlar bo‘yicha taqsimot")
        st.bar_chart(animals["breed"].value_counts())
    with c2:
        st.write("Sut mahsuldorligi — urg‘ochi hayvonlar")
        st.line_chart(females.set_index("id")["milk"].head(25))

    st.subheader("🏆 Eng mahsuldor hayvonlar")
    top = females.sort_values("milk", ascending=False).head(10)
    st.dataframe(top[["id","breed","age","weight","milk","breeding_status"]], use_container_width=True, hide_index=True)

elif page == "Hayvonlar":
    st.subheader("🐄 Hayvonlar bazasi")
    q = st.text_input("Qidirish", placeholder="UZ-0001, Holstein, Simmental...")
    filtered = animals.copy()
    if q:
        mask = filtered.astype(str).apply(lambda col: col.str.contains(q, case=False, na=False)).any(axis=1)
        filtered = filtered[mask]
    st.write(f"Topildi: **{len(filtered)}** ta")
    st.dataframe(filtered, use_container_width=True, hide_index=True)

    st.divider()
    st.subheader("➕ Yangi hayvon qo‘shish")
    with st.form("add_animal"):
        c1,c2,c3 = st.columns(3)
        new_id = c1.text_input("ID", value=f"UZ-{len(animals)+1:04d}")
        new_breed = c2.selectbox("Zot", breeds)
        new_sex = c3.selectbox("Jins", ["Urg‘ochi","Erkak"])
        c4,c5,c6 = st.columns(3)
        new_age = c4.number_input("Yosh", 0, 20, 2)
        new_weight = c5.number_input("Vazn (kg)", 0, 1500, 450)
        new_milk = c6.number_input("Sut (L/kun)", 0.0, 100.0, 25.0)
        submitted = st.form_submit_button("Hayvonni qo‘shish")
        if submitted:
            row = {
                "id": new_id, "name": f"Yangi hayvon", "breed": new_breed, "sex": new_sex,
                "age": new_age, "weight": new_weight, "milk": new_milk if new_sex=="Urg‘ochi" else 0,
                "father": "Noma’lum", "mother": "Noma’lum", "vaccination": str(date.today()),
                "breeding_status": "Kuzatuvda"
            }
            st.session_state.animals = pd.concat([animals, pd.DataFrame([row])], ignore_index=True)
            st.success(f"{new_id} muvaffaqiyatli qo‘shildi. Demo sessiyasi ichida saqlandi.")
            st.rerun()

elif page == "Hayvon pasporti":
    st.subheader("🪪 Raqamli hayvon pasporti")
    selected = st.selectbox("Hayvonni tanlang", animals["id"].tolist())
    a = animals[animals["id"] == selected].iloc[0]
    c1,c2,c3,c4 = st.columns(4)
    c1.metric("ID", a["id"])
    c2.metric("Zot", a["breed"])
    c3.metric("Vazn", f'{a["weight"]} kg')
    c4.metric("Sut", f'{a["milk"]} L/kun')
    st.divider()
    left,right = st.columns(2)
    with left:
        st.write("**Asosiy ma’lumotlar**")
        st.write(f"Jinsi: {a['sex']}")
        st.write(f"Yoshi: {a['age']} yosh")
        st.write(f"Emlash: {a['vaccination']}")
    with right:
        st.write("**Nasl ma’lumotlari**")
        st.write(f"Ota: {a['father']}")
        st.write(f"Ona: {a['mother']}")
        st.write(f"Holati: {a['breeding_status']}")
    st.info("QR-kod moduli keyingi versiyada ulanadi.")

elif page == "Sut & vazn":
    st.subheader("🥛 Sut & ⚖️ vazn monitoringi")
    selected = st.selectbox("Hayvon", animals[animals["sex"]=="Urg‘ochi"]["id"].tolist())
    a = animals[animals["id"] == selected].iloc[0]
    days = pd.date_range(end=pd.Timestamp.today(), periods=14)
    base = float(a["milk"])
    demo = pd.DataFrame({
        "Sana": days,
        "Sut (L)": [round(base + ((i % 5)-2)*0.7,1) for i in range(14)],
        "Vazn (kg)": [int(a["weight"] - 5 + i*0.4) for i in range(14)]
    }).set_index("Sana")
    c1,c2 = st.columns(2)
    with c1:
        st.write("Sut dinamikasi")
        st.line_chart(demo["Sut (L)"])
    with c2:
        st.write("Vazn dinamikasi")
        st.line_chart(demo["Vazn (kg)"])
    st.caption("Grafiklar MVP namoyishi uchun generatsiya qilingan demo tarixidir.")

elif page == "Naslchilik AI":
    st.subheader("🧬 Naslchilik AI — qarorlarni qo‘llab-quvvatlash")
    female = animals[animals["sex"]=="Urg‘ochi"]
    selected = st.selectbox("Sigirni tanlang", female["id"].tolist())
    cow = female[female["id"]==selected].iloc[0]

    st.markdown('<div class="ai">🤖 <b>AI demo tahlili</b><br>Quyidagi tavsiya zot, mahsuldorlik, vazn va nasl ma’lumotlari asosida qoidaviy model bilan hisoblanadi.</div>', unsafe_allow_html=True)
    candidates = animals[animals["sex"]=="Erkak"].copy()
    # Demo scoring: same/compatible breed gets a boost; weight and age are additional factors.
    candidates["score"] = 50
    candidates.loc[candidates["breed"] == cow["breed"], "score"] += 25
    candidates["score"] += ((candidates["weight"] - 450).abs().clip(upper=150) * -0.08)
    candidates["score"] += (candidates["age"].between(3,6).astype(int) * 10)
    candidates = candidates.sort_values("score", ascending=False)
    best = candidates.iloc[0]

    st.success(f"Tavsiya etilayotgan demo nomzod: **{best['id']} — {best['breed']}**, moslik skori: **{best['score']:.0f}/100**")
    st.dataframe(candidates[["id","breed","age","weight","score"]].head(5), use_container_width=True, hide_index=True)
    st.warning("Bu veterinariya/genetik tashxis emas. Real mahsulotda naslchilik mutaxassisi va laboratoriya ma’lumotlari bilan validatsiya qilinadi.")

elif page == "AI Assistant":
    st.subheader("🤖 AI Farm Assistant")
    question = st.text_area("Savolingizni yozing", placeholder="Masalan: Qaysi sigirlar eng mahsuldor?")
    if st.button("Tahlil qilish"):
        if not question.strip():
            st.warning("Savol kiriting.")
        else:
            q = question.lower()
            female = animals[animals["sex"]=="Urg‘ochi"]
            if "mahsuldor" in q or "sut" in q:
                top = female.sort_values("milk", ascending=False).head(5)
                st.write("**Eng yuqori sut ko‘rsatkichlari:**")
                st.dataframe(top[["id","breed","milk","weight"]], use_container_width=True, hide_index=True)
            elif "vazn" in q:
                heavy = animals.sort_values("weight", ascending=False).head(5)
                st.write("**Eng yuqori vaznli hayvonlar:**")
                st.dataframe(heavy[["id","breed","sex","weight"]], use_container_width=True, hide_index=True)
            elif "nasl" in q or "urug" in q:
                st.write("Naslchilik bo‘limida hayvonni tanlang — tizim mavjud demo ma’lumotlar asosida mos nomzodlarni reyting qiladi.")
            else:
                st.info("Demo AI: savolni “sut”, “mahsuldor”, “vazn” yoki “nasl” kalit so‘zlari bilan bering.")

st.divider()
st.caption("AgroGen AI MVP • Demo ma’lumotlari real ferma o‘lchovlari emas. AI moduli hozircha decision-support prototipidir.")
