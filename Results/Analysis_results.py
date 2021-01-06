"""
Analysis_results:
    Input: set of tuples (sender, receiver, time)
    Methods:
        n_nodes: returns dictionary with number of nodes that send, receives, total number of nodes and number of edges
        connection_graph_netw: plots histogram of the number of nodes that are connected to x other nodes
        connection_graph_av: connection graph for the average of a network
        random_netw/ scale_free_netw : constructs a random/scale-free network set of 3-tuples
        multiple_netw: makes N networks of type (str) "random"/"scale-free", returns list of sets of tuples
        average_netw: averages the number of nodes having x connections over multiples graphs,
            returns df "conn" = number of connection, "n" = number of nodes having that number of connections
        trust_distribution: shows a density plot of the trust in a network
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
from Synthetic_netw import *

class Analysis_results(object):
    def __init__(self, Input):
        self.input = Input

    def n_nodes(self):
        """Number of senders, receivers and distinct nodes"""
        senders = [i[0] for i in self.input]
        receivers = [i[1] for i in self.input]
        nodes = set(senders + receivers)
        return {"n_senders": len(set(senders)), "n_receivers": len(set(receivers)), "n_nodes": len(nodes), "n_edges": len(self.input)}

    def __connections(self, netw=input):
        # Dictionnary of who is connected to who
        connect = {}
        for i in netw:
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
        return df

    def connection_graph_netw(self, netw=input):
        df = self.__connections(netw)
        # Plotting
        plt.bar(x=df["conn"], height=df["n"], width=1)
        plt.xlabel("Number of connections")
        plt.ylabel("Number of nodes")
        plt.show()
        return df

    def connection_graph_av(self, df):
        # Plotting
        plt.bar(x=df["conn"], height=df["n"], width=1)
        plt.xlabel("Number of connections")
        plt.ylabel("Number of nodes")
        plt.show()
        return df

    def random_netw(self):
        """Random network with the same number of nodes and edges as our input"""
        n_nodes = self.n_nodes()["n_nodes"]
        n_edges = self.n_nodes()["n_edges"]
        rd = Random_netw(n_nodes, n_edges)
        return rd.random_network_constr()

    def scale_free_netw(self):
        """Scale-free network with the same number of nodes and edges as our input"""
        n_nodes = self.n_nodes()["n_nodes"]
        sf = Scale_free_netw(n_nodes)
        return sf.scale_free_network_constr()

    def multiple_netw(self, N, type):
        """Makes list of N networks of given type (random or scale_free)"""
        netws = []
        # Make the networks
        if type == "random":
            for i in range(N):
                netws.append(self.random_netw())
        elif type == "scale-free":
            for i in range(N):
                netws.append(self.scale_free_netw())
        return netws

    def average_netw(self, netws):
        # Number of connections
        for i in range(len(netws)):
            if i == 0:
                df = self.__connections(netws[i])
            else:
                df = pd.merge(df, self.__connections(netws[i]), how="outer", on="conn")
        # Average of the number of nodes
        df['n'] = df.loc[:,df.columns != "conn"].mean(axis=1)
        df = df.loc[:,["conn", "n"]]
        return df


    def trust_distribution(self):
        """Density of the trust values"""
        trust = np.array([value for value in self.input.values()])
        plt.figure(figsize=(5, 5))
        plt.xlabel("Trust")
        plt.ylabel("Number of interactions")
        sn.kdeplot(trust)
        plt.show()

