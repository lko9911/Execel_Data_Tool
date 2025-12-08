import streamlit as st
import pandas as pd
from analyzer import DataAnalyzer
from visualizer import DataVisualizer
from report import Report

st.set_page_config(page_title="데이터 자동 분석 툴", layout="wide")

st.title("📊 CSV / Excel 자동 분석 웹앱")


# 파일 업로드
uploaded_file = st.file_uploader("분석할 파일을 업로드하세요 (.csv, .xlsx)", type=["csv", "xlsx"])

if uploaded_file:
    # 임시 저장 없이 바로 읽기
    file_path = uploaded_file.name

    # 파일형식 판별하여 pandas로 읽기
    if file_path.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.success("✔ 데이터 로드 완료!")

    # 데이터 표시
    st.subheader("📁 데이터 미리보기")
    st.dataframe(df, use_container_width=True)

    # Analyzer 작동
    analyzer = DataAnalyzer(file_path=None)
    analyzer.df = df  # 직접 전달
    stats = analyzer.describe()

    # 통계 요약 표시
    st.subheader("📌 기본 통계 요약")

    stats_df = pd.DataFrame(stats).T
    st.datafr
