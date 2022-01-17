from .utils import split_column, get_opening_times, generate_empty_columns
from .config import target_columns_names

import pandas as pd


class Src2:

    def __init__(self, df):
        self.df = df
        self.target_df = pd.DataFrame(columns=target_columns_names)
        self.id_list = []
        self.delimiter = ["/", ",", "-"]
        self.restaurant_parsed = []

    def move_header_row(self):
        self.df.loc[-1] = self.df.columns.values
        self.df.index = self.df.index + 1
        self.df.sort_index(inplace=True)

    def add_header(self):
        self.df = pd.DataFrame(self.df.values, columns=["name", "to_parse"])

    def gen_id_from_name(self):
        for row in self.df.iterrows():
            if len(row[1][0].split()) == 1:
                gen_id = row[1][0].split()[0].lower()
            if len(row[1][0].split()) > 1:
                gen_id = row[1][0].split()[0].lower() + row[1][0].split()[1].lower()

            self.id_list.append(gen_id)

    def ids_to_df(self):
        self.df["id"] = self.id_list

    def split_opening_sections(self):
        for idx, row in enumerate(self.df["to_parse"]):
            sections = []
            for section in row:
                sections.append(section.split(","))
            self.df["to_parse"][idx] = sections
            # self.df["to_parse"] = self.df["to_parse"].apply(lambda x: x.split(delimiter))

    def parse_days_hours(self):
        for idx, row in enumerate(self.df["to_parse"]):
            restaurant_name = self.df["id"][idx]
            openings = []
            for section in row:
                openings.append(get_opening_times(section))

            self.restaurant_parsed.append({restaurant_name: openings})

    def to_target_df(self, id, idx, days_hours):
        self.target_df = self.target_df.append({"id":id,
                               "name": self.df["name"][idx],
                               "days": days_hours["days"],
                               "open": days_hours["open"],
                               "close": days_hours["close"]}, ignore_index=True)

    def parsed_to_df(self):
        for idx, restaurants in enumerate(self.restaurant_parsed):
            for id in restaurants:
                for days_hours in restaurants[id]:
                    self.to_target_df(id, idx, days_hours[0])

    def process(self):
        self.move_header_row()
        self.add_header()
        self.gen_id_from_name()
        self.ids_to_df()
        self.df["to_parse"] = split_column(self.df, "/")
        self.split_opening_sections()
        self.parse_days_hours()
        self.df.drop('to_parse', inplace=True, axis=1)
        self.parsed_to_df()
        print(self.target_df)
        return self.df
        # print(self.df)
