import streamlit as st
import os
import time
import glob
from gtts import gTTS
from PIL import Image
import base64

# 🎃 Estilo oscuro personalizado
st.markdown("""
    <style>
    body { background-color: #000000; }
    .stApp {
        background-color: #0a0a0a;
        color: #ff3333;
        font-family: 'Courier New', monospace;
    }
    h1, h2, h3, .css-10trblm { 
        color: #ff0000; 
        text-shadow: 0 0 5px #ff0000;
    }
    .stButton>button {
        background-color: #1a1a1a;
        color: #ff4444;
        border: 1px solid #ff0000;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #550000;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🕸️ Simulador de Vida Atrapada en una Computadora 🧠💻")

image = Image.open("Cursed.jpg")  # Puedes cambiarla por una imagen de glitch o terror
st.image(image, width=350)

with st.sidebar:
    st.subheader("💀 Escoge tu sentencia... quiero decir... texto para escuchar.")
    st.write("Tu voz resonará en este vacío eterno.")

try:
    os.mkdir("temp")
except:
    pass

st.subheader("📜 Fragmento del código maldito:")
st.write("""Hermana mayor vomita sangre,
La hermana menor escupe fuego
Mientras el dulce Tomino
simplemente escupe las joyas.2

Tomino está completamente solo
Ve cayendo en ese infierno,
Un infierno de oscuridad absoluta,
Sin siquiera flores.

¿Es la hermana mayor de Tomino?
¿el que lo azota?
El propósito de la flagelación
cuelga oscuro en su mente.3

¡Azotándolo y golpeándolo, ah!
Pero nunca del todo destrozado.
Un camino seguro hacia Avici,4
el infierno eterno.

En el más negro de los infiernos
Guíalo ahora, te lo ruego.
a la oveja de oro,
al ruiseñor.

¿Cuánto puso?
en esa bolsa de cuero
para prepararse para su viaje
¿El infierno eterno?

Se acerca la primavera
al valle, al bosque,
a los abismos en espiral
del infierno más negro.

El ruiseñor en su jaula,
las ovejas a bordo del carro,
y las lágrimas brotan de los ojos
del dulce Tomino.5

Canta, oh ruiseñor,
en el vasto y brumoso bosque—
Grita, pero solo falla.
su hermana pequeña.

Su desesperación lamentable
ecos por todo el infierno—
Una peonía de zorro
Abre sus pétalos dorados.

Más allá de las siete montañas
y siete ríos del infierno—
el viaje solitario
del dulce Tomino.

Si en este infierno se encuentran,
Que vengan entonces a mí, por favor,
esas afiladas puntas de castigo
Desde la montaña Needle.6

No sólo por un capricho vacío
¿Es la carne atravesada por alfileres de color rojo sangre?
Sirven como señales infernales
Para el dulce Tomino.""")

st.markdown("¿Te atreves a escucharlo? Copia un texto… si te atreves.")
text = st.text_area("✍️ Ingrese el texto maldito:")

option_lang = st.selectbox("🌐 Lenguaje del conjuro:", ("Español", "English"))
lg = "es" if option_lang == "Español" else "en"

def text_to_speech(text, tld, lg):
    tts = gTTS(text, lang=lg)
    file_name = text[0:20].replace(" ", "_") or "audio"
    path = f"temp/{file_name}.mp3"
    tts.save(path)
    return path

if st.button("🔊 Convertir a Audio"):
    audio_path = text_to_speech(text, 'com', lg)
    st.markdown("🎧 He aquí tu mensaje... o maldición:")
    st.audio(audio_path, format="audio/mp3", start_time=0)

    with open(audio_path, "rb") as f:
        data = f.read()

    def get_download_link(data, filename):
        b64 = base64.b64encode(data).decode()
        return f'<a href="data:application/octet-stream;base64,{b64}" download="{filename}">⬇️ Descargar Audio</a>'

    st.markdown(get_download_link(data, "audio.mp3"), unsafe_allow_html=True)

def remove_files(n_days):
    now = time.time()
    for f in glob.glob("temp/*.mp3"):
        if os.stat(f).st_mtime < now - n_days * 86400:
            os.remove(f)

remove_files(7)
