import pandas as pd
import datetime
import time
import pickle


class Twitter_to_Input(object):
    def __init__(self, Filename):
        self.filename = Filename

    def __to_timestamp(self, x):
        """Change time from twitter to timestamp"""
        return time.mktime(datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").timetuple())
    
    def to_input(self):
        # Loading in the twitter date
        data = pd.read_csv(self.filename)
        # Change data
        tr_data = data.loc[:, ["user", "is_reply_to", "time"]]
        tr_data.columns = ["sender", "receiver", "time"]
        tr_data["time"] = tr_data["time"].apply(self.__to_timestamp)
        # Dataframe to set
        res = []
        for i, row in tr_data.iterrows():
            res.append((row[0], row[1], row[2]))
        return set(res)

