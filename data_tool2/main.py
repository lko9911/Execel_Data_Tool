from analyzer import DataAnalyzer
from visualizer import DataVisualizer
from report import Report

file_path = input("분석할 CSV/엑셀 파일 경로 입력: ")
analyzer = DataAnalyzer(file_path)
df = analyzer.load()
stats = analyzer.summary_stats()

visualizer = DataVisualizer(df)
figures = []
for col in df.select_dtypes(include=["int","float"]).columns:
    figures.append(visualizer.histogram(col))
    figures.append(visualizer.boxplot(col))
figures.append(visualizer.correlation_heatmap())

report = Report(stats, figures)
report.generate_html("my_report.html")
