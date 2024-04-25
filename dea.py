import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt 

# 2개 이상 선택했을때와 그렇지 않을때로 개발
if len(selected_columns) >= 2:
    # 1. 페어플롯을 그린다.
    # todo :
    # 1. pairplot 을 다른 라이브러리 이용해서 하는 방법
    # 2. pairplot 말고, 반복문으로 두 컬럼씩의 관계를 차트로 그리는방법
    fig1 = plt.figure()
    sb.pairplot(data=df,vars=selected_columns)
    st.pyplot(fig1)

    # 2 상관계수 보여준다. 
    st.dataframe(df[selected_columns].corr())
else :
    st.text('컬럼은 2개 이상 선택해야 합니다')