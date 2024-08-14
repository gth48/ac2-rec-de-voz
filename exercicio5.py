import streamlit as st
st.title("Lanchonete")
st.text("""
                           LANCHE          CÓDIGO      VALOR

                           Cachorro Quente  101         8,50

                           Bauru Simples    102         4,50

                           Hambúrger        104         5,50

                           Cheeseburger     105         6,60

                           Refrigerante     106         6,00""")
total=0

codigo=st.number_input("Digite o código do produto")
quantidade=st.number_input("Digite a quantidade")
total_button=st.button("Ver o total")

if not codigo :
    st.warning("Você precisa inserir um código!")
if codigo == 101:
    total+=quantidade*8.5
elif codigo==102:
    total+=quantidade*4.5
elif codigo==104:
    total+=quantidade*5.5
elif codigo==105:
    total+=quantidade*6.6
elif codigo==106:
    total+=quantidade*6
else:
    st.warning("Codigo inválido!")

if total_button:
      st.write(f"O total é: R${total:.2f}")
