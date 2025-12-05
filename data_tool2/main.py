from analyzer import DataAnalyzer
from visualizer import DataVisualizer
from report import Report

file_path = input("분석할 CSV/엑셀 파일을 입력하세요: ").strip()

# 1️⃣ 분석기 생성
analyzer = DataAnalyzer(file_path)

# 2️⃣ 반드시 먼저 데이터 로드!
df = analyzer.load()

# 3️⃣ 통계 계산
stats = analyzer.describe()

# 4️⃣ 시각화 생성
visualizer = DataVisualizer(df)
figures = []
figures.extend(visualizer.numeric_histograms())
figures.extend(visualizer.correlation_heatmap())

# 5️⃣ 보고서 생성
report = Report(stats=stats, figures=figures, df=df)
report.generate_html("analysis_report.html")

