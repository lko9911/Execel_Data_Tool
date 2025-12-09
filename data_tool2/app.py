import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="📊 데이터 분석 도구", layout="wide")

st.title("📊 Excel/CSV 데이터 분석 도구")

# ------------------- 파일 업로드 -------------------
uploaded_file = st.file_uploader("파일을 선택하세요 (CSV, XLSX)", type=["csv", "xlsx"])

if uploaded_file is not None:
    # 파일 로드
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.success("파일 로드 성공!")
    except Exception as e:
        st.error(f"파일 로드 오류 발생: {e}")
        st.stop()

    st.subheader("📄 데이터 미리보기")
    st.dataframe(df)

    # ------------------- 기본 통계 -------------------
    st.subheader("📊 기본 통계 요약")
    st.dataframe(df.describe(include="all"))

    # ------------------- Plotly 시각화 -------------------
    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        st.warning("숫자형 데이터가 없어 시각화를 수행할 수 없습니다.")
        st.stop()

    st.subheader("📈 Plotly 시각화")

    # 히스토그램
    col1, col2 = st.columns(2)
    with col1:
        col = st.selectbox("히스토그램 컬럼 선택", numeric_cols)
        try:
            fig = px.histogram(df, x=col)
            st.plotly_chart(fig, use_container_width=True)
        except Exception as e:
            st.error(f"Plot 오류: {e}")

    # 산점도
    with col2:
        x_col = st.selectbox("X축", numeric_cols, key="x")
        y_col = st.selectbox("Y축", numeric_cols, key="y")

        try:
            fig2 = px.scatter(df, x=x_col, y=y_col)
            st.plotly_chart(fig2, use_container_width=True)
        except Exception as e:
            st.error(f"Plot 오류: {e}")

    # ------------------- 상관관계 heatmap -------------------
    st.subheader("📉 상관관계 Heatmap")

    try:
        corr = df[numeric_cols].corr()
        fig3 = px.imshow(corr, text_auto=True, aspect="auto")
        st.plotly_chart(fig3, use_container_width=True)
    except Exception as e:
        st.error(f"Heatmap Plot 오류: {e}")

else:
    st.info("CSV 또는 Excel 파일을 업로드하세요.")
