import pandas as pd
from ydata_profiling import ProfileReport

file_path = input("분석할 CSV/엑셀 파일 경로 입력: ")

# 파일 로드
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
else:
    df = pd.read_excel(file_path)

# 자동 보고서 생성
profile = ProfileReport(
    df, 
    title="자동 데이터 분석 보고서", 
    explorative=True
)

# HTML 보고서로 저장
profile.to_file("data_report.html")
print("보고서 생성 완료: data_report.html")
