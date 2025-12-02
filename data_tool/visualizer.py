import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, df):
        self.df = df

    def plot_hist(self):
        numeric_cols = self.df.select_dtypes(include=["int", "float"]).columns

        for col in numeric_cols:
            plt.figure()
            self.df[col].hist()
            plt.title(f"Histogram of {col}")
            plt.savefig(f"hist_{col}.png")
            plt.close()
