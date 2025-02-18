from jsons.handlejson import export
import numpy

def RenderTest():
    id=0
    n_cells=100
    template="graph"
    filename="test.json"

    for _ in range(0,100):
        id+=1
        rand_cell=numpy.random.randint(Low=0,high=101)
        export()