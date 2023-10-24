import streamlit as st
import altair as alt
import pandas as pd
import plotly.express as px

st.title('종합 실습')
st.header('_2021 서울교통공사 지하철 월별 하차 인원_')

#### streamlit\data_subway_in_seoul.csv
####  encoding='cp949'  읽어오고 확인하기 
df = 

####  button을 누르면 원본데이터 주소가 나타남: https://www.data.go.kr/data/15044247/fileData.do
if st.  ('data copyright link'):
    st.

####  checkbox를 선택하면 원본 데이터프레임이 나타남
if st.   ('원본 데이터 보기'):
    st.subheader('원본 데이터')
    st.

#### '구분' 컬럼이 '하차'인 데이터를 선택
#### 새로운 데이터프레임에 저장 & checkbox를 선택하면 데이터프레임이 나타남
df_off = 
if st.  ('하차 데이터 보기'):
    st.subheader('하차 데이터')
    st.

#### 불필요한 컬럼 '날짜','연번','역번호','역명','구분','합계' 제외
#### 새로운 데이터프레임에 저장 & checkbox를 선택하면 데이터프레임이 나타남
df_line = df_off
if st. ('호선, 시간대별 인원수 보기'):
    st.subheader('호선, 시간대별 인원수')
    st.

####  melt 함수 사용 unpivot: identifier-'호선', unpivot column-'시간', value column-'인원수' 
#### 새로운 데이터프레임에 저장 & checkbox를 선택하면 데이터프레임이 나타남
df_line_melted = pd.melt(df_line, id_vars=['호선'], var_name='시간', value_name='인원수')
if st. ('Unpivot 데이터 보기'):
    st.subheader('구조변경 (Unpivot by melt) 데이터')
    st. 


#### ‘호선‘,＇시간＇별  ‘인원수’ 합, .reset_index()
#### 새로운 데이터프레임에 저장 & checkbox를 선택하면 데이터프레임이 나타남
df_line_groupby = df_line_melted.
if st. ('호선, 시간대별 인원 집계 데이터 보기'):
    st.subheader('호선, 시간대별 인원 집계 데이터')
    st.

#### altair mark_line 차트 그리기
st.subheader('전체 호선 시간대별 하차 인원')
chart = 

st.


st.subheader('선택한 호선의 시간대별 하차 인원')

#### selectbox를 사용하여 '호선' 선택
#### 데이터프레임은 '호선', '시간대별' 인원 집계 df_line_groupby 사용

#### .unique() 매소드를 사용하여 selectbox에 호선이 각각 하나만 나타나게 함
option = st.

#### .loc 함수를 사용하여 선택한 호선 데이터 선별하고
#### 새로운 데이터 프레임-에 저장 & 확인
df_selected_line = df_line_groupby.loc
st.write(option, ' 데이터',  )

#### altair mark_area 차트 그리기
chart = 
               .properties(width=650, height=350)
st.


st.subheader('선택한 역의 시간대별 하차 인원')

#### selectbox를 사용하여 '하차역' 선택
#### 데이터프레임은 '구분' 컬럼이 '하차'인 df_off 사용

#### .unique() 매소드를 사용하여 selectbox에 역명이 각각 하나만 나타나게 함
option = st.

#### .loc 함수를 사용하여 선택한 역의 데이터를 선별하고
#### 새로운 데이터 프레임-에 저장 & 확인
df_sta = df_off.loc

# 불필요한 컬럼 '연번','호선','역번호','역명','구분','합계' 제외하고 기존 데이터 프레임에 저장
df_sta = df_sta
st.write('날짜, 시간대별 인원수 ',  )

# melt 함수 사용 unpivot: identifier-'날짜', unpivot column-'시간', value column-'인원수' 
# 새로운 데이터 프레임-에 저장 & 확인
df_sta_melted = 
st.write('Unpivot ',  )

# '시간' 별 인원수 집계 +.reset_index() & 확인
df_sta_groupby = df_sta_melted.groupby(['시간'])['인원수'].sum().reset_index()
st.write(option, ' 집계 데이터',  )

# altair mark_bar 차트 + text 그리기- x='시간', y='인원수'
chart = 
               .properties(width=650, height=350)
text = alt.Chart

# format=',.0f' : 천 단위 구분기호+소수점 이하 0

st.

# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run streamlit\8.prac.py