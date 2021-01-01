import numpy as np
from data_to_input import Twitter_to_Input

class Node: #node object, connected nodes form a network
    def __init__(self, id):
        self.id = id               #int
        self.connections_id = []   #list of id of nodes connected to this one
        self.connections_w = []    #list of weights for each edge symbolised by connections_id

    def connect_to(self, x, w=1):  #add a new edge
        self.connections_id.append(x)
        self.connections_w.append(w)

    def update_w(self, id, x):     #update weight of edge to given id by amount x
        idx = self.connections_id.index(id)
        self.connections_w[idx]+=x

    def is_connected_to(self, x):  #check if connection exists
        if x in self.connections_id: return(True)
        else: return(False)

    def get_degree(self):          #return node's degree (aka nuber of connections)
        return(len(self.connections_id))

    def get_neighbors(self):       #return neighbors ids
        return(self.connections_id)

    def get_weight(self, id=None): #return weight list or weight for specified neighbor
        if id is not None:
            idx = self.connections_id.index(id)
            return(self.connections_w[idx])
        else:
            return(self.connections_w)

    def get_id(self):              #return id of this node
        return(self.id)

    def show_info(self):
        #link = [(self.connections_id[i], self.connections_w[i]) for i in range(len(self.connections_id))]
        link = [(self.connections_id[i], self.connections_w[i]) for i in range(len(self.connections_id)) if self.connections_w[i]>10]
        print('Id :', self.id,
              ' Deg :', self.get_degree(),
              #' Link list :', link)
              ' Max weight :', link)


class TwitterNetwork():
    def __init__(self, tuple_list):
        #tuple_list : set of 3-tuples (sender, receiver, time)
        self.node_list=[]
        self.id_list=[]
        for t in tuple_list:
            if isinstance(t[0], str) and isinstance(t[1], str):
                for x in (t[0],t[1]):
                    if x not in self.id_list:
                        self.id_list.append(x)
                        self.node_list.append(Node(x))

                idx_s = self.id_list.index(t[0])
                idx_r = self.id_list.index(t[1])

                if not self.node_list[idx_s].is_connected_to(self.id_list[idx_r]):
                    self.node_list[idx_s].connect_to(self.id_list[idx_r])
                else:
                    self.node_list[idx_s].update_w(self.id_list[idx_r], 1)

                if not self.node_list[idx_r].is_connected_to(self.id_list[idx_s]):
                    self.node_list[idx_r].connect_to(self.id_list[idx_s])
                else:
                    self.node_list[idx_r].update_w(self.id_list[idx_s], 1)

    def edges_count(self):
        #return the nuber of edges in the network
        count = 0
        for i in range(len(self.node_list)):
            count += self.node_list[i].get_degree()
        return(int(count/2))

    def show_info(self, nodes=False):
        max_d = max([i.get_degree() for i in self.node_list])
        max_w = max([max(i.get_weight()) for i in self.node_list])
        print('Nodes :', len(self.node_list), ' Edges :', self.edges_count())
        print('Highest degree :', max_d, ' Highest weight :', max_w)
        if nodes:
            for i in self.node_list:
                if max(i.get_weight())>10 : i.show_info()


t = Twitter_to_Input("tweeter_data.csv")
n = TwitterNetwork(t.to_input())
n.show_info(nodes=True)
