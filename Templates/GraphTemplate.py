from manim import *
import random
import networkx as nx
#from jsons.handlejson import importjson

class Graphtemp1(Scene):
    def construct(self):
        n=0
        self.camera.background_color=BLACK
        graph=nx.gnm_random_graph(100,20)  
        pos=nx.spring_layout(graph)
        nodes={i:Dot(point=[pos[i][0]*5,pos[i][1]*5,0],color=WHITE) for i in graph.nodes()}
        edges=[Line(nodes[u].get_center(), nodes[v].get_center(), color=WHITE) for u, v in graph.edges]

        for edge in edges:
            self.add(edge)
        for node in nodes:
            self.add(nodes)
        

        if n in nodes:
            self.play(self.camera.set_x(nodes[n].get_x()).set_y(nodes[n].get_y()))
            

class GraphTemp2(MovingCameraScene):
    def construct(self):
        #Variable n defines number of nodes.
        n = 5
        nodes = [i for i in range(n)]
        edges = []
        #Populating edges array.
        for i in range(n-1):
            if(i+1 >= n):
                continue
            c1 = (i, i+1)
            edges.append(c1)
            if(i+2 >= n):
                continue
            c2 = (i, i+2)
            edges.append(c2)
        #Randomizing the position of nodes.
        pos = {i: (random.randint(-2,2), random.randint(-2,2), 0) for i in range(n)}
        #Creating graph mobject.
        G = Graph(
            nodes, 
            edges, 
            layout = pos,
            layout_config = {"space_x": 10, "space_y": 10},
            layout_scale = 0.25,
            labels = True,
            label_fill_color= 'BLUE'
        )
        
        self.play(Create(G))
        self.wait(2)
        random_node = random.randint(0, n-1)
        #save the original state of the camera (zoomed out)
        self.camera.frame.save_state()
        self.play(self.camera.frame.animate.set(width = 2).move_to(pos[random_node]))
        self.wait(2)
        
        
        
        
        
        
        
        

