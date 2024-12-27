import streamlit as st

st.header('Обучение модели')
shared_data = None
if 'shared_data' in st.session_state:
    shared_data = st.session_state['shared_data']
if shared_data is not None:
    model = st.selectbox("Выберите модель для обучение", ['Logistic Regression', 'SVC', 'Кастомная модель'])
    if model:
        st.button('Обучить модель')
else:
    st.write('Для обучения модели необходимо загрузить данные во вкладке "Main"')