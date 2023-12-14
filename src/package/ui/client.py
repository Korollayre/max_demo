import streamlit as st
import torch

from package.model import load_model, get_text

# определяем на чем будем запускать модель
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

st.title('Краткий пересказ текстов')
# получаем текст от клиента
text = st.text_area('Введите текст')

# запускаем модель
load_model = st.cache_resource(load_model)
summary = load_model()

st.write('Краткий пересказ')

if st.button('Применить'):
    # вывод решения на экран
    st.success(get_text(summary, text))
