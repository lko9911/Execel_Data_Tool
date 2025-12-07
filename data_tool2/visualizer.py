import plotly.graph_objs as go
import pandas as pd

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    # ✔ 상관관계 히트맵
    def correlation_heatmap(self):
        numeric_df = self.df.select_dtypes(include=['number'])

        if numeric_df.empty:
            raise ValueError("상관관계 분석 가능한 수치형 데이터가 없습니다.")

        corr = numeric_df.corr()

        fig = go.Figure(data=go.Heatmap(
            z=corr.values,
            x=corr.columns,
            y=corr.columns,
            coloraxis="coloraxis"
        ))

        fig.update_layout(
            title="📌 Correlation Heatmap",
            coloraxis={'colorscale': 'Blues'},
            template='plotly_white',
            height=600
        )

        return fig

    # 수치형 컬럼 히스토그램 자동 생성
    def numeric_histograms(self):
        figures = []
        numeric_cols = self.df.select_dtypes(include=['number']).columns

        for col in numeric_cols:
            fig = go.Figure()

            fig.add_trace(go.Histogram(
                x=self.df[col],
                nbinsx=30,
                marker=dict(line=dict(width=1)),
                opacity=0.8
            ))

            fig.update_layout(
                title=f"📊 {col}",
                xaxis_title=col,
                yaxis_title="Count",
                template='plotly_white',
                height=400
            )

            figures.append(fig)

        return figures
