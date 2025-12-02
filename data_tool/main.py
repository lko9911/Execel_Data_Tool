from analyzer import DataAnalyzer
from visualizer import DataVisualizer

def main():
    file_path = input("분석할 CSV/엑셀 파일을 입력하세요: ")

    analyzer = DataAnalyzer(file_path)
    df = analyzer.load()

    print("\n[기본 정보]")
    print(analyzer.basic_info())

    print("\n[기본 통계량]")
    print(analyzer.describe())

    # 시각화
    vis = DataVisualizer(df)
    vis.plot_hist()

    print("\n그래프 저장 완료: hist.png\n")

if __name__ == "__main__":
    main()
