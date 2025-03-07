from manim import *
import networkx as nx
from manim.opengl import *
import pyglet
import time
import random



class GraphTemp2(MovingCameraScene):
    def construct(self):
        start = time.time()
        #Variable n defines number of nodes.
        n = 9
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
        self.pos = {i: (random.randint(-2,2), random.randint(-2,2), 0) for i in range(n)}
        #Creating graph mobject.
        self.G = Graph(
            nodes, 
            edges, 
            layout = self.pos,
            layout_config = {"space_x": 10, "space_y": 10},
            layout_scale = 0.25,
            labels = True,
            label_fill_color= 'BLUE'
        )
        self.highlight = Circle(radius=0.25).move_to(self.pos[1])
        self.original_width = self.camera.scale
        self.add(self.G)
        end = time.time()
        
        print(f"Time taken: {(end-start)*10**3:.03f}ms")       
        self.interactive_embed()
    def on_key_press(self,symbol,modifiers):
            if symbol == pyglet.window.key._1:
                if 1 in self.pos:
                    self.play(
                    self.camera.animate.scale(0.5).move_to(self.pos[1]),
                    FadeOut(self.highlight),
                    FadeIn(Circle(radius=0.25).move_to(self.pos[1]))  
                )
            super().on_key_press(symbol, modifiers)




