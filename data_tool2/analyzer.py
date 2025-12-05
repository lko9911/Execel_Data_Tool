import pandas as pd

class DataAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load(self):
        if self.file_path.endswith(".csv"):
            self.df = pd.read_csv(self.file_path)
        elif self.file_path.endswith(".xlsx") or self.file_path.endswith(".xls"):
            self.df = pd.read_excel(self.file_path)
        else:
            raise ValueError("지원하지 않는 파일 형식입니다.")
        return self.df

    def describe(self):
        """수치형 column만 통계 계산하고, 문자열 컬럼은 min/max 없음"""
        if self.df is None:
            raise ValueError("데이터가 로드되지 않았습니다.")

        stats = {}

        for col in self.df.columns:
            series = self.df[col]

            # 숫자형 컬럼 여부 판단
            if pd.api.types.is_numeric_dtype(series):
                stats[col] = {
                    "mean": series.mean(),
                    "std": series.std(),
                    "min": series.min(),
                    "max": series.max(),
                    "missing": series.isna().sum()
                }
            else:
                # 문자형, 날짜형 컬럼 통계
                stats[col] = {
                    "mean": None,
                    "std": None,
                    "min": None,
                    "max": None,
                    "missing": series.isna().sum()
                }

        return stats