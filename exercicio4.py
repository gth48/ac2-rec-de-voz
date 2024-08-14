import streamlit as st
st.title("Calculadora de idade por anos/meses/dias.")
ano_atual = st.number_input("Digite o ano atual")
nascimento_ano = st.number_input("Digite o ano em que você nasceu")
calcular_button=st.button("Calcular")

if calcular_button:
    st.write("Sua idade em anos : ", ano_atual - nascimento_ano)
    st.write("Sua idade em meses : ", ano_atual*12 - nascimento_ano*12)
    st.write("Sua idade em dias : ", ano_atual*365 - nascimento_ano*365)
