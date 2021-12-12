import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression




st.sidebar.image('inovarq.jpeg')
st.image('inovarq.jpeg')

st.markdown('# Prevendo preços de casas')

colunas = ['tamanho','ano','garagem']

model = pickle.load(open('modelo.sav','rb'))

tamanho = st.sidebar.text_input(' Tamanho', float())
ano = st.sidebar.text_input(' Ano', int())
garagem = st.sidebar.text_input(' Quantidade de Carros', float())

obj = {
      "tamanho":[tamanho],
      "ano":[ano],
      "garagem":[garagem]
}


df = pd.DataFrame(data=obj)
df

#check_array(data, dtype = 'numeric')
if st.button("Predict"):    
    st.subheader('Previsão: ')
    st.write(model.predict(df))


#st.sidebar.write('Criado por Inova-Arq')

st.sidebar.markdown('**Criado por Inova-Arq**')
#st.sidebar.image('logo.jpeg', width=50)