import pickle
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class Analysis_results(object):
    def __init__(self, Input):
        self.input = Input

    def n_nodes(self):
        """Number of senders, receivers and distinct nodes"""
        senders = [i[0] for i in self.input]
        receivers = [i[1] for i in self.input]
        nodes = set(senders + receivers)
        return {"n_senders": len(set(senders)), "n_receivers": len(set(receivers)), "n_nodes": len(nodes)}

    def connection_graph(self):
        # Dictionnary of who is connected to who
        connect = {}
        for i in self.input:
            if i[0] not in connect.keys():
                connect[i[0]] = [i[1]]
            else:
                connect[i[0]].append(i[1])
        # Number of nodes (value) having ... (key) connections
        n_connect = {}
        for i in connect.keys():
            if len(connect[i]) in n_connect.keys():
                n_connect[len(connect[i])] += 1
            else:
                n_connect[len(connect[i])] = 1
        # Set values to keys
        df = {"conn": [], "n": []}
        for key, value in n_connect.items():
            df["conn"].append(key)
            df["n"].append(value)
        # To dataframe
        df = pd.DataFrame(df)
        # Plotting
        plt.bar(x=df["conn"], height=df["n"], width=1)
        plt.xlabel("Number of connections")
        plt.ylabel("Number of nodes")
        plt.show()
        return df




f = open("conversational_trust_twitter", "rb")
c_twitter = pickle.load(f)
f.close()
Analysis_results(c_twitter).connection_graph()


# Loading the results of conversational trust
f = open("conversational_trust_enron", "rb")
c_enron = pickle.load(f)
f.close()
Analysis_results(c_enron).connection_graph()
