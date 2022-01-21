from datetime import datetime


class Restaurant:

    def __init__(self, df):
        self.df = df
        self.restaurants_ids = []
        self.restaurants_names = []

    def filter_days(self, day):
        for idx in self.df.index:
            if day not in self.df["days"][idx]:
                self.df.drop(index=idx, inplace=True)

    def filter_hours(self, time):
        for idx in self.df.index:
            if self.df["open"][idx] > time > self.df["close"][idx]:
                self.df.drop(index=idx, inplace=True)

    def get_open_restaurants(self, date=None, weekday=None):
        if date is None:
            time = datetime.now()
        if weekday is None:
            weekday = datetime.now().strftime("%A")[0:2]



        print(weekday)
        self.filter_days(weekday)
        self.filter_hours(time)

        return self.restaurants_names







