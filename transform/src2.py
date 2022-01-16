from .utils import split_column, get_openings_days

from .config import target_columns_names
import pandas as pd


class Src2:

    def __init__(self, df):
        self.df = df
        self.id_list = []
        self.delimiter = ["/", ",", "-"]

    def move_header_row(self):
        self.df.loc[-1] = self.df.columns.values
        self.df.index = self.df.index + 1
        self.df.sort_index(inplace=True)

    def add_header(self):
        self.df = pd.DataFrame(self.df.values, columns=["name", "to_parse"])

    def gen_id_from_name(self):
        for row in self.df.iterrows():
            self.id_list.append(row[1][0].split()[0].lower())

    def ids_to_df(self):
        self.df["id"] = self.id_list

    def split_opening_sections(self):
        for idx, row in enumerate(self.df["to_parse"]):
            sections = []
            for section in row:
                sections.append(section.split(","))
            self.df["to_parse"][idx] = sections
            #self.df["to_parse"] = self.df["to_parse"].apply(lambda x: x.split(delimiter))

    def split_into_rows(self):
        for idx, row in enumerate(self.df["to_parse"]):
            for section in row:
                print(get_openings(section))
                for sub_section in section:
                    #print(sub_section)
                    pass

    def rename_columns(self):
        pass
        #print(split_column("Mon-Sun 11:30 am - 9 pm", self.delimiters))

    def process(self):
        self.move_header_row()
        self.add_header()
        self.gen_id_from_name()
        self.ids_to_df()
        #self.split_to_parse("/")
        #self.split_to_parse("")
        self.df["to_parse"] = split_column(self.df, "/")
        self.split_opening_sections()
        self.split_into_rows()
        print(self.df["to_parse"])

        #self.parsed_column = split_column(self.df, "/")
        return self.df
        #print(self.df)
