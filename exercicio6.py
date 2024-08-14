import streamlit as st
st.title("Calculadora de IMC")
st.text("Insira a sua altura e peso para descobrir o indice de massa corporal:")
peso=st.number_input("Insira o peso em kg:")
altura=st.number_input("Insira a altura em metros:")
calcular_button=st.button("Calcular IMC")
st.text("""
IMC	                Classificação          Obesidade (grau)
Menor que 18,5	        Magreza	               0
Entre 18,5 e 24,9	Normal	               0
Entre 25,0 e 29,9	Sobrepeso	       I
Entre 30,0 e 39,9	Obesidade	       II
Maior que 40,0	        Obesidade Grave        III""")

if calcular_button:
    imc=peso/(altura*altura)
    st.success(f"O IMC é: {imc}")
