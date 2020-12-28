from random import sample
from Random_input_generator import Random_input

class Conversation(object):
    def __init__(self, Input, a, b, s=0.1):
        # Input: set of tuples (sender, receiver, time)
        self.input = Input
        # Criteria to say if two messages are in the same conversation
        self.S = s
        # Agents
        self.A = a; self.B = b

    def message_set(self):
        """List of times at which a message was exchanged between the two agents A and B"""
        # List of the interactions between A and B
        interactions = [i for i in self.input if (i[0] == self.A and i[1] == self.B) or (i[0] == self.B and i[1] == self.A)]
        # Sorted list of times of these interactions
        M = [i[2] for i in interactions]
        M.sort()
        return M

    def average_time_messages(self, M):
        """tau, average time between two messages"""
        return ((max(M) -min(M))/ len(M))

    def conv(self, M):
        """List of sets grouping the messages by conversations"""
        C = []
        # Average time between messages
        tau = self.average_time_messages(M)

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

        return C


class Conversational_Trust(Conversation):
    def __init__(self, Input):
        self.input = Input

    def agent_pairs(self):
        """All existing agent pairs"""
        return set([(i[0], i[1]) for i in self.input])

    def all_convs(self):
        """Dictionary of the agents and their conversations """
        convs = {}
        agents = self.agent_pairs()
        for a in agents:
            c = Conversation(self.input, a[0], a[1])
            convs[a] = c.conv(c.message_set())
        return convs


