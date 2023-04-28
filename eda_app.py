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
        st.title('Title')
        with st.expander('산점도'):
            fig1 = px.scatter(iris,
                             x = 'sepal_width',
                             y ='sepal_length',
                             color = 'species',
                             size = 'petal_width',
                             hover_data = ['petal_length'])
            st.plotly_chart(fig1)

        # layouts
        col1, col2 = st.columns(2)
        with col1:
            st.title('Seaborn')
            fig, ax= plt.subplots()
            sns.boxplot(iris, x ='species',y = 'sepal_length', ax = ax)
            st.pyplot(fig)

        with col2:
            st.title('Matplotlib')
            fig, ax = plt.subplots()
            ax.hist(iris['sepal_length'], color="green")
            st.pyplot(fig)

        # Taps
        tab1, tab2, tab3 = st.tabs(['탭1', '탭2', '탭3'])
        with tab1:
            st.write('Setosa')
            choice1 = iris['species'].unique()[0]
            result3 = iris[iris['species'] == choice1]
            fig2 = px.scatter(result3,
                              x='sepal_width',
                              y='sepal_length')
            st.plotly_chart(fig2)

        # with tab2:
        #      st.write('virsicolor')
        #      choice2 = iris['species'].unique()[1]
        #      result4 = iris[iris['species'] == choice2]
        #      fig3 = px.scatter(result4,
        #                        x='sepal_width',
        #                        y='sepal_length')
        #     st.plotly_chart(fig3)
        #
        # with tab3:
        #      st.write('virginica')
        #      choice3 = iris['species'].unique()[2]
        #      result5 = iris[iris['species'] == choice3]
        #      fig4 = px.scatter(result5,
        #                         x='sepal_width',
        #                         y='sepal_length')
        #     st.plotly_chart(fig4)


            # 캐글 데이터 / 공모전 데이터
            # 해당데이터 그래프 1개만 그리기

    elif submenu == '통계분석':
        pass
    else:
        st.warning('뭔가 없어요')