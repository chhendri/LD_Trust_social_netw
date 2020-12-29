import numpy as np
from random import randint, choice, uniform
from Scale_free import Node


class RandomNetwork:
    def __init__(self, n, k):
        #n : total number of nodes in the RandomNetwork
        #k : total number of edges to draw between the n nodes
        self.nodes = [Node(i) for i in range(n)] #list of nodes constituting the network
        self.n = n
        while self.edges_count() < k:
            random_idx1 = randint(0, n-1)
            random_idx2 = randint(0, n-1)
            if random_idx1 != random_idx2 and not self.nodes[random_idx1].is_connected_to(random_idx2):
                self.nodes[random_idx1].connect_to(random_idx2)
                self.nodes[random_idx2].connect_to(random_idx1)

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
#erdros = RandomNetwork(10, 20)
#erdros.show_info(True)
#for i in erdros.get_random_pair(5): print(i)

#output
#Nodes : 10  Edges : 20
#Id : 0  Deg : 5  Link list : [6, 7, 5, 4, 9]
#Id : 1  Deg : 3  Link list : [7, 2, 4]
#Id : 2  Deg : 6  Link list : [6, 3, 8, 4, 7, 1]
#Id : 3  Deg : 2  Link list : [7, 2]
#Id : 4  Deg : 5  Link list : [6, 0, 7, 2, 1]
#Id : 5  Deg : 2  Link list : [0, 9]
#Id : 6  Deg : 4  Link list : [0, 4, 2, 7]
#Id : 7  Deg : 7  Link list : [0, 8, 1, 3, 4, 6, 2]
#Id : 8  Deg : 3  Link list : [7, 2, 9]
#Id : 9  Deg : 3  Link list : [0, 8, 5]
#(6, 7)
#(3, 2)
#(5, 0)
#(5, 0)
#(6, 2)
