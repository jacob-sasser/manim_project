import pyglet
from manim import *
from manim.opengl import *
class Assignment():
    locations={}
    last_node=None
    correct_node = None
    incorrect_counter = 0
    incorrect_max = 3
    question_text = None
    feedback_text = None  
    assignments=[]
    current_assignment_index=0
    def check_answer(self,node):
        if self.feedback_text:
            self.remove(self.feedback_text)
        if node==self.correct_node:
            self.feedback_text=Text("Correct").to_edge(DOWN)
            self.add(self.feedback_text)
            self.is_assignment=False

            self.play(FadeOut(self.feedback_text), FadeOut(self.question_text), run_time=0.5 )      
            self.current_assignment_index+=1
            self.start_next_assignment()
        else:
            self.incorrect_counter+=1
            if self.incorrect_counter>=self.incorrect_max:
                self.feedback_text = Text("Too many incorrect attempts.").to_edge(DOWN)
                self.is_assignment=False
                
            else: self.feedback_text=Text(f"Incorrect ( {self.incorrect_counter}/{self.incorrect_max})").to_edge(DOWN)
            self.add(self.feedback_text)

    def start_next_assignment(self):
        if(self.current_assignment_index<len(self.assignments)):
            correct_node,question=self.assignments[self.current_assignment_index]
            self.assignment(correct_node,question)
        else:
            self.complete_all_assignments()


    def assignment(self, correct_node, question):
        self.correct_node = correct_node
        self.incorrect_counter = 0
        self.is_assignment = True

        if self.question_text:
            self.remove(self.question_text)
        if self.feedback_text:
            self.remove(self.feedback_text)
        self.question_text = Text(question).to_edge(UP)
        self.add(self.question_text)
        
    def complete_all_assignments(self):
        self.clear()
        completion_text=Text("All assignments completed")
        self.add(completion_text)

    def calculate_relative_node_pos(self,nodes,scale):
        camera_center=np.array(self.camera.get_center())
        relative_nodes_pos={}
        for node in self.pos:
            node_pos=np.array(self.pos[node])
            relative_pos=(node_pos-camera_center)/scale
            relative_nodes_pos[node]=relative_pos

        
        return relative_pos