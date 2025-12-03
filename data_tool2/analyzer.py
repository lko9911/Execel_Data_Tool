import pandas as pd

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load(self):
        if self.file_path.endswith(".csv"):
            self.df = pd.read_csv(self.file_path)
        else:
            self.df = pd.read_excel(self.file_path)
        return self.df

    def summary_stats(self):
        stats = {}
        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                stats[col] = {
                    "mean": self.df[col].mean(),
                    "std": self.df[col].std(),
                    "min": self.df[col].min(),
                    "max": self.df[col].max(),
                    "missing": self.df[col].isnull().sum()
                }
        return stats
