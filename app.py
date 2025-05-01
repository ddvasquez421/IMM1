import streamlit as st
import os
import time
import glob
from gtts import gTTS
from PIL import Image
import base64

# --- INTERFAZ RENOVADA ---
st.set_page_config(page_title="Narrador Virtual", layout="centered")

st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 2rem;
        border-radius: 12px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🗣️ Narrador Virtual")

col1, col2 = st.columns([1, 2])
with col1:
    image = Image.open("gato_raton.png")
    st.image(image, width=250)
with col2:
    st.subheader("Transforma tu texto en voz")
    st.markdown(
        "Convierte cuentos, reflexiones o ideas en audio fácilmente usando inteligencia artificial."
    )

# --- CREAR CARPETA TEMPORAL ---
os.makedirs("temp", exist_ok=True)

# --- TEXTO EJEMPLO ---
st.markdown("---")
st.markdown("### 🐭 Una Fábula para Escuchar")
fabula = (
    "\u00a1Ay! -dijo el rat\u00f3n-. El mundo se hace cada d\u00eda m\u00e1s peque\u00f1o. Al principio era tan grande que le ten\u00eda miedo. "
    "Corr\u00eda y corr\u00eda y por cierto que me alegraba ver esos muros, a diestra y siniestra, en la distancia. "
    "Pero esas paredes se estrechan tan r\u00e1pido que me encuentro en el \u00faltimo cuarto y ah\u00ed en el rinc\u00f3n est\u00e1 la trampa sobre la cual debo pasar. "
    "Todo lo que debes hacer es cambiar de rumbo -dijo el gato... y se lo comi\u00f3. \n\n_Franz Kafka._"
)
st.info(fabula)

# --- ENTRADA DE TEXTO ---
text = st.text_area("\ud83c\udfa7 Escribe o pega tu texto:", height=150, value=fabula)

# --- SELECCIÓN DE IDIOMA ---
language = st.selectbox("\ud83c\udf0d Idioma del Audio:", ("Espa\u00f1ol", "English"))
lg = "es" if language == "Espa\u00f1ol" else "en"

# --- CONVERSIÓN DE TEXTO A AUDIO ---
def text_to_speech(text, lg):
    tts = gTTS(text, lang=lg)
    filename = f"temp/audio_{int(time.time())}.mp3"
    tts.save(filename)
    return filename

if st.button("\ud83d\udd0a Generar Audio"):
    if text.strip():
        filepath = text_to_speech(text, lg)
        audio_file = open(filepath, "rb")
        audio_bytes = audio_file.read()

        st.success("\ud83d\udd0a Reproduciendo tu audio:")
        st.audio(audio_bytes, format="audio/mp3")

        with open(filepath, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            dl_link = f'<a href="data:audio/mp3;base64,{b64}" download="tu_audio.mp3">\ud83d\udcc1 Descargar Audio</a>'
            st.markdown(dl_link, unsafe_allow_html=True)
    else:
        st.warning("\u26a0\ufe0f Por favor ingresa texto para convertirlo.")

# --- BORRADO AUTOMÁTICO DE ARCHIVOS ANTIGUOS ---
def remove_old_files(days_old):
    cutoff = time.time() - (days_old * 86400)
    for file in glob.glob("temp/*.mp3"):
        if os.path.getmtime(file) < cutoff:
            os.remove(file)
            print("Archivo eliminado:", file)

remove_old_files(7)
