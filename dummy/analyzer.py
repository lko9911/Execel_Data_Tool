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

    def basic_info(self):
        rows, cols = self.df.shape
        missing = self.df.isnull().sum()
        return {
            "행(Row)": rows,
            "열(Column)": cols,
            "결측치(Missing)": missing.to_dict()
        }

    def describe(self):
        return self.df.describe(include="all")
