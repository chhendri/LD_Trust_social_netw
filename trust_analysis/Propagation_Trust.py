from Random_input_generator import Random_input

class Propagation_Trust_AB(object):
    """B sends message to A who can then propagate it to X"""
    def __init__(self, Input, a, b, T_min=0, T_max=10):
        self.input = Input
        self.A = a
        self.B = b
        self.t_min = T_min
        self.t_max = T_max

    def incoming_A(self):
        """Messages incoming to A as a dict with keys being the time and values the input tuples (sender, receiver, time)"""
        i_A = {}
        for i in self.input:
            if i[1] == self.A:
                i_A[i[2]] = i
        return i_A

    def sent_by_A(self):
        """Messages sent by A"""
        s_A = {}
        for i in self.input:
            if i[0] == self.A:
                s_A[i[2]] = i
        return s_A

    def __list_times(self, dic):
        """Times of the sent or received messages (sorted list)"""
        lst = list(dic.keys())
        lst.sort()
        return lst

    def all_propagations_A(self):
        """All possible propagations for A: associations between messages received and messages sent by A"""
        # Sent by A
        s_A = self.sent_by_A()
        # Incoming to A
        i_A = self.incoming_A()
        # Times A sent messages
        t_sA = self.__list_times(s_A)
        # Times A received messages
        t_iA = self.__list_times(i_A)

        # Maximal number of propagations
        max_props = []
        # Loop over all sent messages and all received messages
        for s in t_sA:
            for i in t_iA:
                # Time difference between sent and receives
                diff = s - i
                # Condition for propagation
                if self.t_min <= diff and self.t_max >= diff:
                    max_props.append((i_A[i],s_A[s]))
        return [i for i in max_props if i[0][0] != i[1][1]]

    # TODO def statistically significant

    def propagations_AB(self):
        """Statistically significant propagations between A and B"""
        # All propagations of A
        all_props_A = self.all_propagations_A()
        # Subset being the propagations between A and B (from B to A)
        potential_props_AB = [i for i in all_props_A if i[0][0] == self.B and i[0][1] == self.A]
        # TODO if propagations are significant
        return potential_props_AB

    def trust_weight(self):
        # number of messages B sent to A
        m_AB = len([i for i in self.incoming_A().values() if i[0] == self.B])
        # number of propagations by A
        prop_A = len(self.all_propagations_A())
        # number of messages B sent to A that were propagated by A
        prop_AB = len(self.propagations_AB())
        # Quantification of the propagation energy used by A to propagate messages from B
        energy_AB_prop = prop_AB/prop_A
        # Fraction of the messages sent by B that A propagated
        frac_AB_prop = prop_AB/m_AB
        return energy_AB_prop, frac_AB_prop


class Propagation_trust(Propagation_Trust_AB):
    def __init__(self, Input):
        self.input = Input

    def __agent_pairs(self):
        """All existing agent pairs"""
        return set([(i[0], i[1]) for i in self.input])

    def prop_trust(self):
        """Dictionary of the agents and their conversations """
        trust = {}
        agents = self.__agent_pairs()
        for a in agents:
            p = Propagation_Trust_AB(self.input, a[0], a[1])
            # If a propagation between A and B exists, compute the trust
            if len(p.propagations_AB()) > 1:
                trust[a] = p.trust_weight()[1]
        return trust

