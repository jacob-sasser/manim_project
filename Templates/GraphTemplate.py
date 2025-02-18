from manim import *
import networkx as nx
from jsons.handlejson import importjson

class Graph(Scene):
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
        
        

