from dwave.system import DWaveSampler
import dwave.inspector

sampler = DWaveSampler(
    solver='DW_2000Q_6',
    #token='',
)

h = {
    }


J = {
    (0,4): -1,
    (0,7): -1,
    (3,4): -1,
    (3,7): -1,
    (1,4): 1,
    (1,7): 1,
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
