from .config import target_columns_names
from itertools import chain
from re import split
from opening_hours import OpeningHours
from pyparsing.exceptions import ParseException

week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def flatten(array):
    return [item for sublist in array for item in sublist]


def generate_empty_columns(df):
    for num in range(len(target_columns_names) - df.shape[1]):
        print("adding empty")
        df[num] = ""
    return df


def split_column(df, delimiter):
    splitted_list = []
    for d in df.iterrows():
        splitted_list.append(d[1][1].split(delimiter))
    return splitted_list


def get_days(boundaries):

    if len(boundaries) == 2:
        return list(map(lambda x: x[0:2], week_days[boundaries[0]:boundaries[1] + 1]))

    return [week_days[boundaries[0]][0:2]]


def get_days_boundaries(sub_section):
    boundaries = []
    for idx, day in enumerate(week_days):
        if day[0:3] in sub_section:
            boundaries.append(idx)

    return boundaries


def get_hours():
    pass


def get_opening_times(section):
    for sub_section in section:
        opening_time = []
        for sub_sub_section in sub_section.split(","):
            try:
                opening_time.append(OpeningHours.parse(sub_sub_section).json())
            except ParseException:
                day_boundaries = get_days_boundaries(sub_section)
                opening_time.append(get_days(day_boundaries))

    return opening_time

def get_openings_days(section):
    days = []
    for sub_section in section:
        boundaries = []
        for idx, day in enumerate(week_days):
            if day[0:3] in sub_section:
                boundaries.append(idx)

        days.append(get_days(boundaries))

    return list(chain.from_iterable(days))
