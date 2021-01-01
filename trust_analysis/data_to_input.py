import pandas as pd
import datetime
import time


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
            if row[0] == row[0] and row[1] == row[1]:
                res.append((row[0], row[1], row[2]))
        return set(res)


class Enron_to_Input(object):
    def __init__(self, Filename):
        self.filename = Filename

    def __to_timestamp(self, x):
        """Change time from Enron to timestamp"""
        return time.mktime(datetime.datetime.strptime(x, "%a, %d %b %Y %H:%M:%S").timetuple())

    def to_input(self):
        # Read the lines of the file and convert to dictionary
        data = []
        f = open(self.filename, "r")
        lines = f.readlines()
        f.close()
        i = 0
        while i < len(lines):
            data.append((lines[i+1].strip("\n"), lines[i+2].strip("\n").split(", "), lines[i].strip("\n")))
            i += 3
        # Multiple receivers to multiple occurences
        for n in range(len(data)):
            value = data[n]
            if len(value[1]) > 1:
                while len(value[1]) != 1:
                    data.append((value[0], value[1][0], value[2]))
                    del value[1][0]
                    data[n] = (value[0], value[1], value[2])
                data[n] = (value[0], value[1], value[2])

        # Format the dictionnary to be converted to a dataframe
        df = {"sender": [], "receiver": [], "time": []}
        for i in data:
            df["sender"].append(i[0])
            df["receiver"].append(i[1])
            df["time"].append(i[2])
        # As a dataframe
        df = pd.DataFrame(df)
        # Time conversion
        df["time"] = df["time"].apply(self.__to_timestamp)

        # Dataframe to set
        res = []
        for i, row in df.iterrows():
            row[1] = str(row[1])
            if row[0] == row[0] and row[1] == row[1]:
                res.append((row[0], row[1], row[2]))
        return set(res)

