import speech_recognition as sr
import streamlit as st

def principal():
    st.title("Transcrição de Áudio")
    uploaded_file = st.file_uploader("Faça upload do arquivo de áudio com a lista de compras.",type=["wav"])
    if uploaded_file is not None:
        transcrever(uploaded_file)
    
def transcrever(arquivo):
    recognizer = sr.Recognizer()
    with sr.AudioFile(arquivo) as source:
        audio = recognizer.record(source)
        texto_transcrito = recognizer.recognize_google(audio, language="pt-BR")
        st.write("Lista de compras: ",texto_transcrito)
        
principal()
