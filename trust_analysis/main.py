from data_to_input import Twitter_to_Input
from Conversational_Trust import Conversational_Trust, Conversation_AB
from Propagation_Trust import Propagation_trust, Propagation_Trust_AB


# Loading in the twitter date
data1 = "/media/charlotte/Elements/Learning_dynamics/tweeter_data.csv"
data2 = "/media/charlotte/Elements/Learning_dynamics/tweeter_data'.csv"

set1 = Twitter_to_Input(data1).to_input()
set2 = Twitter_to_Input(data2).to_input()
res = set1.union(set2)

c = Conversational_Trust(res)
print(c.conv_trust())

p = Propagation_trust(res)
print(p.prop_trust())