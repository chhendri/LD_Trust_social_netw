"""
Conversational_trust:
    Input: set of tuples (sender, receiver, time)
    Inheritance: Conversation_AB
    Methods: 
        conv_trust : returns normalised trust graph as a dictionary with keys being the (sender, receiver) pairs and values being the trust between them
        
Conversation_AB: 
    Input: 
        Input = set of tuples (sender, receiver, time)
        A = str, agent name
        B = str, second agent name
    Methods:
        message_list: returns list of times when a message was exchanged
        conv : returns list of times a message was exchanged in a conversation
        conv_trust_AB: returns float being the conversational trust between agent A and agent B
"""


from random import sample
from math import log
from Random_input_generator import Random_input

class Conversation_AB(object):
    def __init__(self, Input, a, b, s=10000):
        # Input: set of tuples (sender, receiver, time)
        self.input = Input
        # Criteria to say if two messages are in the same conversation
        self.S = s
        # Agents
        self.A = a; self.B = b

    def __interactions_AB(self):
        """List of the interactions between A and B"""
        return [i for i in self.input if self.A and self.B in i]

    def message_list(self):
        """List of times at which a message was exchanged between the two agents A and B"""
        interactions = self.__interactions_AB()
        # Sorted list of times of these interactions
        M = [i[2] for i in interactions]
        M.sort()
        return M

    def __average_time_messages(self, M):
        """tau, average time between two messages"""
        return ((max(M) -min(M))/ len(M))

    def conv(self, M):
        """List of messages being in a conversation"""
        C = []
        # Average time between messages
        tau = self.__average_time_messages(M)
        for i in range(len(M)-1):
            # Define t_i and t_i+1
            t_i = M[i]; t_i1 = M[i+1]
            # Criteria for these two messages being in the same conversation
            if (t_i1 - t_i) < (self.S * tau):
                # Add message to the conversation
                C.append(t_i1)
        # Look if C is empty
        if len(C) >= 2:
            return C

    def __fraction_a(self, conv):
        """Fraction of the messages sent by A (p)"""
        n_a = 0
        inters = {}
        interactions = self.__interactions_AB()
        # Dictionnary with keys being the time and values being the agents
        for i in interactions:
            inters[i[2]] = (i[0], i[1])
        # Number of times A was the sender
        for t in conv:
            if inters[t][0] == self.A:
                n_a += 1
        return n_a/len(conv)

    def __entropy_func(self, conv):
        """Entropy function giving the balance of the conversation"""
        # Fraction of messages coming from A
        p = self.__fraction_a(conv)
        if p == 1:
            return (-p * log(p))
        if p == 0:
            return -((1-p) * log(1-p))
        else:
            return ((-p * log(p)) - ((1-p) * log(1-p)))

    def conv_trust_AB(self):
        """Trust between the agents A and B"""
        tc = []
        # Conversations
        convs = self.conv(self.message_list())
        # Trust between A and B
        tc.append(len(convs) * self.__entropy_func(convs))
        return sum(tc)




class Conversational_Trust(Conversation_AB):
    def __init__(self, Input):
        self.input = Input

    def __agent_pairs(self):
        """All existing agent pairs"""
        return set([(i[0], i[1]) for i in self.input])

    def __normalization(self, trust):
        """Normalisation of the trust values (relative trust)"""
        # Maximal trust
        m = max(trust.values())

        norm_trust = {}
        for key, value in trust.items():
            norm_val = value / m
            # Keep only normalised values higher than 0.01
            if norm_val > 0.01:
                norm_trust[key] = norm_val
        return norm_trust

    def conv_trust(self):
        """Dictionary of the agents and their conversations """
        trust = {}
        agents = self.__agent_pairs()
        for a in agents:
            c = Conversation_AB(self.input, a[0], a[1])
            # If a conversation between A and B exists, compute the trust
            if c.conv(c.message_list()) != None:
                trust[a] = c.conv_trust_AB()
        trust = self.__normalization(trust)
        return trust
