# streamlit 라이브러리와 datetime 모듈 불러오기
import streamlit as st
from datetime import datetime  

st.title('Unit 4. Input Widgets')
st.caption('참조사이트: https://docs.streamlit.io/library/api-reference/widgets')

st.header('1. Button')
if st.button('Say hello'):
    st.write('Hello')
else:
    st.write('Goodbye')

st.header('2. Radio button')
genre = st.radio('좋아하는 장르를 선택하세요', ['코메디', 'SF', '액션'])

if genre ==  '코메디':
    st.write('유쾌하시네요')
elif genre == 'SF':
    st.write('저도 SF 좋아합니다')
else:
    st.write('멋지시네요')

st.header('3. Checkbox')    # 😄
agree = st.checkbox('I agree')
if agree:
    st.write('Great')

st.header('4. Select box')
option = st.selectbox('어떻게 연락드릴까요?', ['Email', 'Mobile Phone', 'Office Phone'])
st.write('네,',option,'(으)로 연락드리겠습니다.')

st.header('5. Multi select')
options = ('좋아하는 색을 모두 선택하세요', ['Yellow', 'Red', 'Green', 'Blue'])
st.write('선호 색상:', options)




st.header('6. Input: Text/Number')

st.subheader('**_text_input_**')
title = st.text_input('최애 영화를 입력하세요', 'Sound of Music')
st.write('당신이 가장 좋아하는 영화는:', title)

st.subheader('**_number_input_**')
number = st.number_input('Insert a number(1-10)', min_value=1, max_value=10, value=5, step=1)
st.write('Current number:', number)

st.header('7. Date input')
ymd = st.date_input('When is your birthday?', datetime(1998,2,20))
st.write('Your birthday is:', ymd)

st.header('8. Slider')

st.subheader('**_Slider- 이전 구간_**')
age = st.slider('나이가 어떻게 되세요?', 0, 130, 25)
st.write("I'm ", age, 'years old')

st.subheader('**_최소-최대값 내에서 숫자 사이 구간_**')
values = st.slider('값 구간을 선택사세요', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.subheader('**_년 월 일 사이 구간_**')

slider_time = st.slider(
    'Select a range of datetime?',
    datetime(2023, 1, 1), datetime(2023, 12, 31),
    value=(datetime(2023, 7, 1), datetime(2023, 10, 31)),
    format='YY/MM/DD')
st.write('Slider time: ', slider_time)

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\4-1.input.py