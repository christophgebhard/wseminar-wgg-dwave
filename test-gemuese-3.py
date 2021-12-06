from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
    #token='',
)

h = {}

# Hier wählen wir:
# 0 = Paprika
# 4 = Fenchel
# 7 = Kartoffel
# 3 = Pflücksalat
# 1 = Kohlrabi
# 5 = Spinat

J = {
    (0,4): +1,
    (0,7): +1,
    (3,4): -1,
    (3,7): +1,
    (1,4): +1,
    (1,7): -1,
    (5,1): -1,
    (5,3): -1,
    (0,5): -1,
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
)
print(response)
dwave.inspector.show(response)
