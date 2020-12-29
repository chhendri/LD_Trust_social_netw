import numpy as np
from random import randint, choice, uniform


class Node: #node object, connected nodes form a network
    def __init__(self, id):
        self.id = id               #int
        self.connections = []      #list of id of nodes connected to this one

    def connect_to(self, x):       #add a new connection
        self.connections.append(x)

    def is_connected_to(self, x):  #check if connection exists
        if x in self.connections: return(True)
        else: return(False)

    def get_degree(self):          #return node's degree (aka nuber of connections)
        return(len(self.connections))

    def get_neighbors(self):       #return neighbors ids
        return(self.connections)

    def get_id(self):              #return id of this node
        return(self.id)

    def show_info(self, id):
        print('Id :', id,
              ' Deg :', self.get_degree(),
              ' Link list :', self.connections)


class BarabaskiNetwork():
    def __init__(self, nodes_tot, nodes_ini, nb_new_edges):
        #nodes_tot : final size of the network
        #nodes_ini : initial number of fully connected nodes
        #nb_new_edges : number of edges to add for each new node

        #add nodes_ini number of nodes and fully connect them
        self.nodes = [Node(i) for i in range(nodes_ini)] #list of nodes constituting the network
        self.nodes_tot = nodes_tot
        sum = 0
        for i in range(nodes_ini):
            for j in range(i+1,nodes_ini):
                if not self.nodes[i].is_connected_to(j):
                    self.nodes[i].connect_to(j)
                    self.nodes[j].connect_to(i)
                    sum+=2

        #add new nodes with preferential attachment until nodes_tot is reached
        while len(self.nodes) < nodes_tot:
            proba = [i.get_degree()/sum for i in self.nodes]
            self.nodes.append(Node(len(self.nodes)))
            while self.nodes[-1].get_degree() < nb_new_edges:
                randomIdx = np.random.choice(range(len(proba)), p=proba)
                if not self.nodes[-1].is_connected_to(randomIdx):
                    self.nodes[-1].connect_to(randomIdx)
                    self.nodes[randomIdx].connect_to(len(self.nodes)-1)
                    sum+=2

    def edges_count(self):
        #return the nuber of edges in the network
        count = 0
        for i in range(len(self.nodes)):
            count += self.nodes[i].get_degree()
        return(int(count/2))

    def get_avg_degree(self):
        #return avg degree over all network
        return(2*self.edges_count()/len(self.nodes))

    def show_info(self, edges_info=False):
        print('Nodes :', len(self.nodes), ' Edges :', self.edges_count())
        if edges_info:
            for i in range(len(self.nodes)): self.nodes[i].show_info(i)

    def get_random_pair(self, n):
        #return a list of n random pairs of connected peoples in the network
        pair_list = []
        for i in range(n):
            sender = choice(self.nodes)
            sender_id = sender.get_id()
            receiver_id = choice(sender.get_neighbors())
            pair_list.append((sender_id, receiver_id))
        return(pair_list)


#exemple for a 10 member network with 5 randomly picked pairs
#bara = BarabaskiNetwork(10, 4, 4)
#bara.show_info(True)
#for i in bara.get_random_pair(5): print(i)

#output
#Id : 0  Deg : 5  Link list : [1, 2, 3, 4, 8]
#Id : 1  Deg : 8  Link list : [0, 2, 3, 4, 5, 6, 8, 9]
#Id : 2  Deg : 7  Link list : [0, 1, 3, 4, 5, 7, 9]
#Id : 3  Deg : 7  Link list : [0, 1, 2, 4, 5, 6, 7]
#Id : 4  Deg : 8  Link list : [2, 0, 3, 1, 5, 6, 8, 9]
#Id : 5  Deg : 7  Link list : [2, 3, 4, 1, 6, 7, 8]
#Id : 6  Deg : 5  Link list : [4, 1, 5, 3, 7]
#Id : 7  Deg : 5  Link list : [2, 5, 3, 6, 9]
#Id : 8  Deg : 4  Link list : [5, 1, 0, 4]
#Id : 9  Deg : 4  Link list : [4, 2, 7, 1]
#(8, 0)
#(1, 5)
#(9, 7)
#(5, 3)
#(1, 8)
