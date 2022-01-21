from .config import target_columns_names
from .utils import to_datetime
import pandas as pd


class Src1:

    def __init__(self, df):
        self.df = df
        self.days = []

    def rename_columns(self):
        self.df.columns = target_columns_names

    def process(self):
        self.rename_columns()
        self.df = to_datetime(self.df)

        return self.df
