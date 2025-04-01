from manim import *
import random
import time
import networkx as nx
from typing import override
from networkx.algorithms import tree
#from jsons.handlejson import importjson
import IPython
import time
from Assignment import Assignment

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
        #Creating Labels
        labels = {node: Text(str(node)) for node in nodes}
        #Populating array with all configured graph data to be returned.
        graph_data = [nodes, edges, pos, labels]
        return graph_data

def randomEdgeGen(vCount: int, edgesArr: list):
    #Used in SPFAlgorithm
    for i in range(vCount):
        while(True): #Loop is used to ensure no duplicate edges.
            randEdge = random.randrange(vCount)
            if((randEdge, i) in edgesArr or i == randEdge):
                continue
            else:
                break
        edgesArr.append((i, randEdge)) #Add edge tuple to array of edges.        


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
                layout_scale = 2,
                labels = True
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

class BFSAnim(Scene,Assignment):
    def construct(self):
        #self.layer_index=0
        #self.next_edge = -1
        self.mouse_locked = False
        tree_depth = 2
        children = 2
        nx_graph = nx.balanced_tree(children, tree_depth)
        self.m_graph = Graph(list(nx_graph.nodes),
                        list(nx_graph.edges),
                        layout = "tree",
                        layout_scale= 3.5,
                        labels = True,
                        label_fill_color=BLUE,
                        edge_config={"color":RED},
                        vertex_config = {"color": RED, "stroke_width": 3, "radius": 0.3},
                        root_vertex = 0,
                        )
        self.add(self.m_graph,Text("BFS Search Algorithm").scale(0.5).to_corner(UL))

        self.bfs_edges = list(nx.bfs_edges(nx_graph, 0, sort_neighbors=lambda n: sorted(n, reverse=True)))
        self.bfs_layers = dict(enumerate(nx.bfs_layers(nx_graph, 0)))
        print(self.bfs_edges)
        print(self.bfs_layers)
        # Assignment.assignments=[(0,"Select which node is next"),
        #                         (1,"Select which node is next"),
        #                         (2,"Select which node is next")]
        
        #Assignment Population via NetworkX BFS Layers.
        Assignment.assignments = []
        for layer in self.bfs_layers.values():
            Assignment.assignments.append((layer, "Select which node is next"))
        print(Assignment.assignments)
            

        Assignment.start_next_assignment(self) 
        self.pos={}
        #self.pos[0]=self.m_graph.vertices[0].get_center().tolist()
        # for k,edge in enumerate(self.bfs_edges):
        #     for i in edge:
        #         self.pos[k+1] = self.m_graph.vertices[i].get_center().tolist()
        
        #Changed previous version due to position numbers not lining up with actual vertice numbers.
        for i,vertice in enumerate(self.m_graph.vertices.values()):
            self.pos[i] = vertice.get_center().tolist()
        
        self.node_radius=0.5
        self.interactive_embed() 
        
        
    #Old - Used specific node order not layered approach
    # def highlight_node(self):
    #     print(self.edge_order)
    #     if(self.next_edge == -1):
    #         self.play(self.m_graph.vertices[0].animate.set_color(GREEN), run_time = 0.5)
    #     else:
    #         edge_tup = self.edge_order[self.next_edge]
    #         to_node = self.m_graph.vertices[edge_tup[1]]
    #         self.play(self.m_graph.edges[(edge_tup[0], edge_tup[1]) or (edge_tup[1], edge_tup[0])].animate.set_color(GREEN), run_time = 0.5)
    #         if(to_node.get_color() != GREEN):
    #             self.play(to_node.animate.set_color(GREEN), run_time = 0.5)
    
    def highlight_node(self, node):
        edge_to_highlight = None
        for edge in self.bfs_edges:
            if edge[1] == node:
                edge_to_highlight = edge
                self.bfs_edges.remove(edge)
                break
        print(edge_to_highlight)
        if edge_to_highlight == None:
            self.play(self.m_graph.vertices[node].animate.set_color(GREEN), run_time = 0.5)
        else:           
            to_node = self.m_graph.vertices[edge_to_highlight[1]]
            self.play(self.m_graph.edges[(edge_to_highlight[0], edge_to_highlight[1]) or (edge_to_highlight[1], edge_to_highlight[0])].animate.set_color(GREEN), run_time = 0.5)
            if(to_node.get_color() != GREEN):
                self.play(to_node.animate.set_color(GREEN), run_time = 0.5)
            
            
            
        
        
        
    @override
    def check_answer(self,node):
        def correct_answer():
            self.feedback_text=Text("Correct").to_edge(DOWN)
            self.add(self.feedback_text)
            
            self.highlight_node()
            #self.next_edge += 1
            
            self.is_assignment=False
            self.play(FadeOut(self.feedback_text), FadeOut(self.question_text), run_time=0.5 )      
            self.current_assignment_index+=1
            self.start_next_assignment()
        if self.feedback_text:
            self.remove(self.feedback_text)
        if node in self.correct_node:
            self.correct_node.remove(node)
            print("Correct Node", self.correct_node)
            print("Assignments", Assignment.assignments)
            #self.layer_index+=1
            self.feedback_text=Text("Correct").to_edge(DOWN)
            self.add(self.feedback_text)
            
            self.highlight_node(node)
            #self.next_edge += 1
            
            self.is_assignment=False
            self.play(FadeOut(self.feedback_text), FadeOut(self.question_text), run_time=0.5 )      
            #if self.layer_index >= len(Assignment.assignments(Assignment.current_assignment_index)):
            #    Assignment.current_assignment_index+=1
            if len(self.correct_node) <= 0:
                Assignment.current_assignment_index += 1
            self.start_next_assignment()
        elif node==self.correct_node:
            correct_answer()
        else:
            self.incorrect_counter+=1
            if self.incorrect_counter>=self.incorrect_max:
                self.feedback_text = Text("Too many incorrect attempts.").to_edge(DOWN)
                self.add(self.feedback_text)
                self.failed_assignment() #Displays a failed assignment screen
                self.is_assignment=False
            else: 
                self.feedback_text=Text(f"Incorrect ( {self.incorrect_counter}/{self.incorrect_max})").to_edge(DOWN)
                self.add(self.feedback_text)
            
    def on_mouse_press(self, point, button, modifiers):
            if self.mouse_locked:
                print("Cant click!")
                return
            
            x,y,z=point
            scene_x=x
            scene_y=y
            
            #print(x,y)
            #if self.last_node is not None: 
             #   scene_x,scene_y,_=self.calculate_relative_node_pos(self.last_node,self.zoom_scale)
            
            rounded_x = round(scene_x, 1)
            rounded_y = round(scene_y, 1)
            if rounded_x==-0.0:rounded_x=0.
            if rounded_y == -0.0:rounded_y=0.
            print(rounded_x,rounded_y)
            
            for node, pos in self.pos.items():
                node_x, node_y, _ = pos
                if (abs(scene_x - node_x) <= self.node_radius) and (abs(scene_y - node_y) <= self.node_radius):
                    print(abs(scene_x-node_x))
                    print(abs(scene_y-node_y))
                    self.mouse_locked = True
                    print("Mouse Locked")
                    self.check_answer(node)
                    self.mouse_locked = False
                    print("Mouse unlocked!")
            
            super().on_mouse_press(point, button, modifiers)
                      
            
class SPFAlgorithm(Scene):
    def construct(self):
        #Scene graph parameters.
        vCount = 8
        pos = {
            0:(0,4,0),
            1:(-2,2,0),
            2:(2,2,0),
            3:(-2,-2,0),
            4:(2,-2,0),
            5:(0,-4,0),
            6:(-4,0,0),
            7:(4,0,0)
        }
        verticesArr = [i for i in range(vCount)]
        edgesArr = []
        randomEdgeGen(vCount, edgesArr)
        
        #Scene graph creation
        sceneNXGraph = nx.DiGraph() #Ensures edge tuple (u, v) doesn't get flipped to (v, u).
        sceneNXGraph.add_nodes_from(verticesArr)
        sceneNXGraph.add_edges_from(edgesArr)
        sceneGraph = Graph.from_networkx(sceneNXGraph, 
                                         layout = pos, 
                                         labels = True, 
                                         label_fill_color = BLUE,
                                         layout_scale = 4.0, 
                                         edge_type = DashedLine)
        
        #Weight population
        weights = [random.randrange(1,10) for edge in edgesArr]
        weightedEdgesArr = [(*edge, weights[i]) for i, edge in enumerate(edgesArr)]
        
        #Weight label mobject creation & positioning.
        edgeLabels = VGroup()
        for wEdge in weightedEdgesArr:
            edge = (wEdge[0],wEdge[1])
            weight = wEdge[2]
            edgeLine = sceneGraph.edges[edge]
            label = Text(str(weight)).scale(0.75)
            center = edgeLine.get_center()
            label.move_to(center)
            edgeLabels.add(label)
        
        #Calculate minnimum spanning tree of the graph using Prim's algorithm.
        mstGraph = nx.Graph() #Duplicate graph of sceneNXGraph. Used to calculate minnimum spanning tree.
        mstGraph.add_nodes_from(verticesArr)
        mstGraph.add_weighted_edges_from(weightedEdgesArr)
        mst = tree.minimum_spanning_edges(mstGraph, data = True, algorithm="prim")
        mstEdges = list(mst)
        
        #Animation.
        self.add(sceneGraph, edgeLabels)
        self.play(sceneGraph.vertices[mstEdges[0][0]].animate.set_color(RED)) #Highlights first node.
        for edge in mstEdges:
            #Matching edge values to a tuple in the original edges array (value order inconsistent between sceneGraph & mstGraph)
            if(edge[0], edge[1]) in edgesArr: 
                temp = (edge[0], edge[1])
            else:
                temp = (edge[1], edge[0])
            self.play(sceneGraph.edges[temp].animate.set_color(RED)) #Highlight the chosen edge.
            if sceneGraph.vertices[temp[0]].get_color() != RED: #Check if the first node is highlighted.
                self.play(sceneGraph.vertices[temp[0]].animate.set_color(RED))
            if sceneGraph.vertices[temp[1]].get_color() != RED: #Check if the second node is highlighted
                self.play(sceneGraph.vertices[temp[1]].animate.set_color(RED))
            
        
        
            
            
        
            
        
        
        
        
        

