from itertools import chain
from opening_hours import OpeningHours
from pyparsing.exceptions import ParseException
import pandas as pd

week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


def flatten(array):
    return [item for sublist in array for item in sublist]


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


def group_subsections(openings):
    for day in openings[0]:
        openings[1]['days'].append(day)

    del openings[0]
    return openings


def group_opening_days(parsed_days_hours):
    days = []
    for row in parsed_days_hours:
        days.append(row['day'][0:2].capitalize())

    return {"days": days, "open": parsed_days_hours[0]["opens"], "close": parsed_days_hours[0]["closes"]}


def get_opening_times(section):
    opening_time = []
    for sub_section in section:
        try:
            # Library opening_hours, doesn't recognize "Thu", instead needs to be "Thurs" or "Th"
            sub_section = sub_section.replace("Thu", "Thurs")
            parsed_days_hours = OpeningHours.parse(sub_section).json()
            grouped_parsed_hours = group_opening_days(parsed_days_hours)
            opening_time.append(grouped_parsed_hours)
        except ParseException:
            day_boundaries = get_days_boundaries(sub_section)
            opening_time.append(get_days(day_boundaries))

    if len(opening_time) > 1:
        return group_subsections(opening_time)

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


def to_datetime(df):
    df["open"] = df["open"] = pd.to_datetime(df['open'])
    df["close"] = df["close"] = pd.to_datetime(df['close'])

    return df
