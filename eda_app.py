# -*- coding:UTF-8 -*-
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import utils

def run_eda_app():
    st.subheader('탐색적 자료 분석')

    iris = pd.read_csv('data/iris.csv')
    st.markdown('## IRIS 데이터확인')
    st.write(iris) # print

    # 메뉴 지정
    submenu = st.sidebar.selectbox ('하위메뉴',['기술통계량','그래프분석', '통계분석'])
    if submenu == '기술통계량':
        st.dataframe(iris)

        with st.expander('데이터 타입'):
            result= pd.DataFrame(iris.dtypes)
            st.write(result)
        with st.expander('기술통계량'):
            result2 =iris.describe()
            st.write(result2)

        with st.expander('타깃 빈도 수 확인'):
            st.write(iris['species'].value_counts())
    elif submenu == '그래프분석':
        st.title("Title")
        with st.expander("산점도"):
            fig2 = px.scatter(iris,
                             x='sepal_width',
                             y='sepal_length',
                             color='species',
                             size='petal_width',
                             hover_data=['petal_length'])
            st.plotly_chart(fig2)

        #layouts
        col1, col2 = st.columns(2)
        with col1:
            st.title('Seaborn')
            fig, ax = plt.subplots()
            sns.boxplot(iris,x='species',y='sepal_length',ax=ax)
            st.pyplot(fig)
            # 그래프 작성

        with col2:
            st.title('Matplotlib')
            # 그래프작성
            fig1, ax=plt.subplots()
            ax.hist(iris['sepal_length'],color='green')
            st.pyplot(fig1)

        # Tabs
        tab1, tab2 =st.tabs(['탭1','탭2'])
        with tab1:
            st.write("탭1")
            if iris(iris['species'] == 'setosa'):
                fig2 = px.scatter(iris,
                                  x='sepal_width',
                                  y='sepal_length')
            # 종 선택할때 마다
            # 산점도 그래프 가 달라지도록 함
            # plotly 그래프로 구현
        with tab2:
            st.write("탭2")
            # 캐글 데이터 /공모전데이터
            # 해당데이터 그래프 1개만그리기
    elif submenu == '통계분석':
        pass
    else:
        st.warning('뭔가 없어요')