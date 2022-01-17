from .config import target_columns_names
from .utils import generate_empty_columns


class Src1:

    def __init__(self, df):
        self.df = df

    def rename_columns(self):
        self.df.set_axis([target_columns_names], axis=1, inplace=True)

    def process(self):
        self.rename_columns()
        return self.df
