from manim import *
import networkx as nx
from manim.opengl import *
import pyglet
import random
from pyglet.window import mouse
import numpy as np

class GraphTemp2(MovingCameraScene):
    locations={}
    last_node=None
    

    def construct(self):
        self.zoom_scale=0.75
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
        self.locations=self.pos
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
       
        self.highlight=None
        self.original_scale=self.camera.scale

        self.interactive_embed()
    def on_key_press(self,symbol,modifiers):
            if symbol == pyglet.window.key._1:
                if 1 in self.pos:
                    self.play(
                    self.camera.animate.scale(0.5).move_to(self.pos[1]),
                    FadeOut(self.highlight),
                    FadeIn(Circle(radius=0.25).move_to(self.pos[1]))  
                )
            if symbol==pyglet.window.key.MINUS:
                 self.camera.scale((1/self.zoom_scale)).move_to(ORIGIN)

            super().on_key_press(symbol, modifiers)


    def on_mouse_press(self, point, button, modifiers):
            x,y,z=point
            scene_x=x
            scene_y=y
            print(x,y)
            #if self.last_node is not None: 
             #   scene_x,scene_y,_=self.calculate_relative_node_pos(self.last_node,self.zoom_scale)

            rounded_x = round(scene_x, 0)
            rounded_y = round(scene_y, 0)
            if rounded_x==-0.0:rounded_x=0.
            if rounded_y == -0.0:rounded_y=0.
            print(rounded_x,rounded_y)
            
            for node, pos in self.pos.items():
                if (round(pos[0], 1), round(pos[1], 1)) == (rounded_x, rounded_y):
                    self.focus_node(node)

            super().on_mouse_press(point, button, modifiers)

    def focus_node(self,node):
        '''if self.last_node is not None and self.last_node!=node:
            self.play(self.camera.animate.scale(1/self.zoom_scale).move_to(ORIGIN))'''
        if self.highlight:
            self.play(FadeOut(self.highlight))
        self.highlight = Circle(radius=0.25).move_to(self.pos[node])
        
        self.play(
                #self.camera.animate.scale(1).move_to(self.pos[node]),
                FadeIn(self.highlight))
        self.last_node = node
    

    def calculate_relative_node_pos(self,nodes,scale):
        camera_center=np.array(self.camera.get_center())
        relative_nodes_pos={}
        for node in self.pos:
            node_pos=np.array(self.pos[node])
            relative_pos=(node_pos-camera_center)/scale
            relative_nodes_pos[node]=relative_pos

        
        return relative_pos