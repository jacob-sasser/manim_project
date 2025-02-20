import subprocess
import numpy
import time
import numpy

def RenderTest():
    id=0
    n_cells=100
    template="graph"
    script="Templates/GraphTemplate.py"
    scene="GraphTemp2"
    times=list()
    for i in range(0,30):
        output_filename = f"manim_output_{int(time.time())}_{i}.mp4"

        id+=1
        start=time.time()
        #Make sure to change the output file location
        subprocess.run(["manim", "-pql", "Templates/GraphTemplate.py", "GraphTemp2", "--media_dir", "Your desired output location","--output_file",output_filename], check=True)
        end=time.time()
        times.append(end-start)
    print(numpy.mean(times))


RenderTest()
