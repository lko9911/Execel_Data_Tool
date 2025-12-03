from plotly.subplots import make_subplots
import plotly.io as pio

class Report:
    def __init__(self, stats, figures):
        self.stats = stats
        self.figures = figures

    def generate_html(self, output_file="report.html"):
        html_parts = []

        # 통계 요약
        html_parts.append("<h1>데이터 분석 보고서</h1>")
        for col, stat in self.stats.items():
            html_parts.append(f"<h2>{col}</h2>")
            html_parts.append("<ul>")
            for k, v in stat.items():
                html_parts.append(f"<li>{k}: {v}</li>")
            html_parts.append("</ul>")

        # 그래프 삽입
        for fig in self.figures:
            html_parts.append(fig.to_html(full_html=False, include_plotlyjs='cdn'))

        # HTML 저장
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(html_parts))
        print(f"보고서 생성 완료: {output_file}")
