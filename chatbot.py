import streamlit as st
from langchain.llms import OpenAI

st.title('간단한 챗봇')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('프롬프트를 입력하세요:', '샌드위치를 만드는 방법에 대해 알려주세요.')
    submitted = st.form_submit_button('실행')
    if not openai_api_key.startswith('sk-'):
        st.warning('OpenAI API Key를 입력하세요!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
