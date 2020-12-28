from random import sample
from math import log
from Random_input_generator import Random_input

class Conversation_AB(object):
    def __init__(self, Input, a, b, s=0.1):
        # Input: set of tuples (sender, receiver, time)
        self.input = Input
        # Criteria to say if two messages are in the same conversation
        self.S = s
        # Agents
        self.A = a; self.B = b

    def __interactions_AB(self):
        """List of the interactions between A and B"""
        return [i for i in self.input if (i[0] == self.A and i[1] == self.B) or (i[0] == self.B and i[1] == self.A)]

    def message_set(self):
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
        """List of sets grouping the messages by conversations"""
        C = []
        # Average time between messages
        tau = self.__average_time_messages(M)

        for i in range(len(M)-1):
            # Define t_i and t_i+1
            t_i = M[i]; t_i1 = M[i+1]
            # Criteria for these two messages being in the same conversation
            if (t_i1 - t_i) < (self.S * tau):
                # Add message to the conversation
                C[-1].add(t_i1)
            else:
                # Make new conversation
                C.append(set())
        # Retain only conversations of more than 2 messages
        for i in C:
            if len(i) < 2:
                C.remove(i)
        # Look if C is empty
        if len(C) != 0:
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
        #print(conv)
        for t in conv:
            if inters[t][0] == self.A:
                n_a += 1
            #print(t)
        return n_a/len(conv)

    def __entropy_func(self, conv):
        """Entropy function giving the balance of the conversation"""
        # Fraction of messages coming from A
        p = self.__fraction_a(conv)
        return ((-p * log(p)) - ((1-p) * log(1-p)))

    def conv_trust_AB(self):
        """Trust between the agents A and B"""
        tc = []
        # Conversations
        convs = self.conv(self.message_set())
        # Trust between A and B
        for c in convs:
            tc.append(len(c) * self.__entropy_func(c))
        return sum(tc)




class Conversational_Trust(Conversation_AB):
    def __init__(self, Input):
        self.input = Input

    def __agent_pairs(self):
        """All existing agent pairs"""
        return set([(i[0], i[1]) for i in self.input])

    def conv_trust(self):
        """Dictionary of the agents and their conversations """
        trust = {}
        agents = self.__agent_pairs()
        for a in agents:
            c = Conversation_AB(self.input, a[0], a[1])
            # If a conversation between A and B exists, compute the trust
            if c.conv(c.message_set()) != None:
                trust[a] = c.conv_trust_AB()
        return trust

