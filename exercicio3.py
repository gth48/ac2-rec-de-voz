import streamlit as st
st.title("Códigos de desconto:")
st.text("""Região Norte com desconto de 5%: código 1
Região Sul com desconto de 15%: código 2
Região Sudeste com desconto de 7%: código 3
Região Nordeste com desconto de 12%: código 4
Região Centro-Oeste com desconto de 20%: código 5""")
valor = st.number_input("Insira o valor que receberá o desconto: ")
codigo = st.number_input("Insira o código: ")

if codigo == 1:
    st.title(f"Valor final: {valor*0.95}")
elif codigo == 2:
    st.title(f"Valor final:  {valor*0.85}")
elif codigo == 3:
    st.title(f"Valor final: {valor*0.93}")
elif codigo == 4:
    st.title(f"Valor final: {valor*0.88}")
elif codigo == 5:
    st.title(f"Valor final: {valor*0.8}")
else:
    st.title("Valor final:")

    
