import time
import streamlit as st
import pandas as pd
import asyncio
import matplotlib.pyplot as plt
from process_data import is_data_correct

st.title('Приложение для анализа и визуализации данных о токсичных комментариев')
st.header('Загрузите файл файл с комментариями')

@st.cache_data
def load_data(filepath):
    return pd.read_csv(filepath)

uploaded_file = st.file_uploader('Загрузите файл файл с комментариями', type=['csv'])

if uploaded_file is not None:
    data = load_data(uploaded_file)
    if is_data_correct(data) is False:
        st.error('Необходимые столбцы: toxicity и comment_text - отсутствуют в вашем файле.')
    else:
        st.dataframe(data)
else:
    st.write('Файл не выбран.')