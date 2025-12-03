import plotly.express as px
import plotly.graph_objects as go

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def histogram(self, column):
        fig = px.histogram(self.df, x=column, title=f"{column} 분포")
        return fig

    def boxplot(self, column):
        fig = px.box(self.df, y=column, title=f"{column} 박스플롯")
        return fig

    def correlation_heatmap(self):
        corr = self.df.corr()
        fig = px.imshow(corr, text_auto=True, title="상관계수 히트맵")
        return fig
