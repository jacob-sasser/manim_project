from manim import *
import random
import time
import networkx as nx
#from jsons.handlejson import importjson


def graphPopulation(n):
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
        #Populating array with all configured graph data to be returned.
        graph_data = [nodes, edges, pos]
        return graph_data
        

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
        start = time.time()
        #Variable n defines number of nodes.
        n = 100
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
        
        random_node = random.randint(0, n-1)
        highlight = Circle(radius = 0.25).move_to(pos[random_node]) #Red circle used to highlight nodes. 0.25 is the radius of each node(layout_scale).
        self.add(G)
        self.camera.frame.save_state() #Saves the original position (state) of camera.
        self.play(
            self.camera.frame.animate.set(width = 2).move_to(pos[random_node]), 
            FadeIn(highlight)                        
            )
        self.wait(2)
        self.play(
            FadeOut(highlight),
            Restore(self.camera.frame)
            )
        self.wait(2)
        
        end = time.time()
        print(f"Time taken: {(end-start)*10**3:.03f}ms")        

        
class variousSizedGraphs1(Scene):
    def construct(self):
        start = time.time()
        #25 Nodes
        n = 25
        graph_data = graphPopulation(n)
        g_25 = Graph(
            graph_data[0],
            graph_data[1],
            layout = graph_data[2],
            layout_scale = 2
        )
        random_node = random.randint(0, n-1)
        anim_group = [FadeIn(g_25),g_25.vertices[random_node].animate.set_color(RED),Wait(1.5),FadeOut(g_25)]
        self.play(Succession(*anim_group))
        self.remove(g_25,g_25.vertices[random_node])
        end = time.time()
        print(f"25 nodes time taken: {(end-start)*10**3:.03f}ms")        

        #50 nodes
        start = time.time()
        n = 50
        graph_data = graphPopulation(n)
        g_50 = Graph(
            graph_data[0],
            graph_data[1],
            layout = graph_data[2],
            layout_scale = 2
        )
        anim_group = [FadeIn(g_50),g_50.vertices[random_node].animate.set_color(RED),Wait(1.5),FadeOut(g_50)]
        self.play(Succession(*anim_group))
        self.remove(g_50,g_50.vertices[random_node])
        
        end = time.time()
        print(f"50 nodes time taken: {(end-start)*10**3:.03f}ms")  
        
        #100 nodes
        start = time.time()
        n = 100
        graph_data = graphPopulation(n)
        g_100 = Graph(
            graph_data[0],
            graph_data[1],
            layout = graph_data[2],
            layout_scale = 2
        )
        anim_group = [FadeIn(g_100),g_100.vertices[random_node].animate.set_color(RED),Wait(1.5),FadeOut(g_100)]
        self.play(Succession(*anim_group))
        self.remove(g_100,g_100.vertices[random_node])
    
        end = time.time()
        print(f"100 nodes time taken: {(end-start)*10**3:.03f}ms")  
        
        #200 nodes
        start = time.time()
        n = 200
        graph_data = graphPopulation(n)
        g_200 = Graph(
            graph_data[0],
            graph_data[1],
            layout = graph_data[2],
            layout_scale = 2
        )
        anim_group = [FadeIn(g_200),g_200.vertices[random_node].animate.set_color(RED),Wait(1.5),FadeOut(g_200)]
        self.play(Succession(*anim_group))
        self.remove(g_200,g_200.vertices[random_node])
        
        end = time.time()
        print(f"200 nodes time taken: {(end-start)*10**3:.03f}ms")  

class variousSizedGraphs2(Scene):
    #Previous variousSizedGraphs scene class but using a while loop.
    def construct(self):
        i = 25
        while i <= 200:
            start = time.time()
            graph_data = graphPopulation(i)
            g = Graph(
                graph_data[0],
                graph_data[1],
                layout = graph_data[2],
                layout_scale = 2
            )
            random_node = random.randint(0, i-1)
            anim_group = [FadeIn(g),g.vertices[random_node].animate.set_color(RED),Wait(1.5),FadeOut(g)]
            self.play(Succession(*anim_group))
            self.remove(g,g.vertices[random_node])
            
            end = time.time()
            print(f"{i} nodes time taken: {(end-start)*10**3:.03f}ms")  
            i = i * 2
            
            
        
    
class scalingTests(Scene):
    def construct(self):
        graph_data = graphPopulation(10)
        g_10 = Graph(
            graph_data[0],
            graph_data[1],
            layout = graph_data[2], 
            layout_scale = 2.0 
        )
        self.add(g_10)
        self.play(
            ScaleInPlace(g_10, 2.0)
        )
        
        
        

