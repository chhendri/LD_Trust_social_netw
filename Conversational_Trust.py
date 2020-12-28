from random import sample
from Random_input_generator import Random_input

class Conversational_trust(object):
    def __init__(self, Input, s=0.1):
        # Input: set of tuples (sender, receiver, time)
        self.input = Input
        # Criteria to say if two messages are in the same conversation
        self.S = s

    def message_set(self, A, B):
        """List of times at which a message was exchanged between the two agents A and B"""
        # List of the interactions between A and B
        interactions = [i for i in self.input if (i[0] == A and i[1] == B) or (i[0] == B and i[1] == A)]
        # Sorted list of times of these interactions
        M = [i[2] for i in interactions]
        M.sort()
        return M

    def average_time_messages(self, M):
        """tau, average time between two messages"""
        return ((max(M) -min(M))/ len(M))

    def conversations(self, M):
        """List of sets grouping the messages by converseations"""
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
        return C


