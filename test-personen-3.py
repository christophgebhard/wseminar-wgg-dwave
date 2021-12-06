from dwave.system import DWaveSampler, EmbeddingComposite
import dwave.inspector

sampler = EmbeddingComposite(DWaveSampler(
    solver='DW_2000Q_6',
    #token='',
))

h = {
    }


J = {
  

    ('0','1'): 2,
    ('0','3'): 2,
    ('0','4'): 1,
    ('0','5'): 1,
    ('0','7'): 1,
    ('1','3'): 2,
    ('1','4'): 3,
    ('1','5'): 1,
    ('1','7'): 3,
    ('3','4'): 1,
    ('3','5'): 1,
    ('3','7'): 1,
    ('4','5'): 2,   
    ('4','7'): 2,
    ('5','7'): 2,
}

response = sampler.sample_ising(
    h, 
    J, 
    num_reads=100,
    chain_strength=4,
)
print(response)
dwave.inspector.show(response)