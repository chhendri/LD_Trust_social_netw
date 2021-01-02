from random import randint, random
#pip install randomtimestamp
import randomtimestamp
import datetime
import time


class Random_netw(object):
    def __init__(self, N, K):
        self.n = N
        self.k = K

    def __to_timestamp(self, x):
        """Change time from Enron to timestamp"""
        return time.mktime(datetime.datetime.strptime(x, "%d-%m-%Y %H:%M:%S").timetuple())
        
    def random_network_constr(self):
        # Making a random network as an adjacency list
        rd_netw = {}
        # Initializing: Dictionary containing a list being the connected vertices
        for i in range(1, self.n + 1):
            rd_netw[i] = []
        # Adding edges
        n_edges = 0
        while n_edges < self.k:
            v1 = randint(1, self.n);
            v2 = randint(1, self.n)
            if v2 not in rd_netw[v1] and v1 != v2:
                rd_netw[v1].append(v2)
                rd_netw[v2].append(v1)
            n_edges = sum([len(rd_netw[x]) for x in rd_netw])

        # To 3-tuples format
        netw = set()
        for key, value in rd_netw.items():
            # Add a random time
            time = self.__to_timestamp(randomtimestamp.randomtimestamp())
            for i in value:
                netw.add((key, i, time))

        return netw


class Scale_free_netw(object):
    def __init__(self, N):
        self.n = N

    def __to_timestamp(self, x):
        """Change time from Enron to timestamp"""
        return time.mktime(datetime.datetime.strptime(x, "%d-%m-%Y %H:%M:%S").timetuple())

    def __attachment_p(self, links, n, k_j):
        return links[n] / k_j

    def scale_free_network_constr(self):
        sf_netw = {}
        # Initialise a scale-free network of 4 nodes
        for i in range(1, 5):
            sf_netw[i] = [j for j in range(1, 5) if j != i]

        # Storage of the number of links of each node -> reduces time needed for probability computation
        n_links = {}
        # Initial number of links
        k_j = 0
        for n in sf_netw.keys():
            l = len(sf_netw[n])
            k_j += l
            n_links[n] = l

        n_nodes = 4
        while n_nodes < self.n:
            # Make 4 connections
            n_con = 0
            while n_con < 4:
                # Select a random node and define a probability
                r = randint(1, n_nodes)
                ap = random()
                # Calculate the attachment probability to that node r
                p = self.__attachment_p(n_links, r, k_j)
                # Append the new nodes if the probability is lower than the probability of appending
                if ap < p:
                    # Add the new node to the existing randomly selected node and increase the number of links for both nodes
                    if n_nodes + 1 not in sf_netw.keys():
                        sf_netw[n_nodes + 1] = [r]
                        n_links[n_nodes + 1] = 1
                    else:
                        sf_netw[n_nodes + 1].append(r)
                        n_links[n_nodes + 1] += 1
                    sf_netw[r].append(n_nodes + 1)
                    sf_netw[r] = list(dict.fromkeys(sf_netw[r]))
                    sf_netw[n_nodes + 1] = list(dict.fromkeys(sf_netw[n_nodes + 1]))
                    n_links[r] += 1
                    n_con += 1
                    k_j += 1
            n_nodes += 1

        # To 3-tuples format
        netw = set()
        for key, value in sf_netw.items():
            # Add a random time
            time = self.__to_timestamp(randomtimestamp.randomtimestamp())
            for i in value:
                netw.add((key, i, time))

        return netw

