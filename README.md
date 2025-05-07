#Animation and Interactivity Research  
A project worked on by Jacob Sasser and Brandon Tiseo for the bridges team at UNC Charlotte.  
Goal of the project was to demonstrate the capabilities of Manim as an animation engine to be  
utilized for Computer Science education.  
    
# To run:  
Need to have UV installed, https://docs.manim.community/en/stable/installation.html  
other packages needed: pyglet, IPython, numpy, networkx, Manim  
To run the project do: uv run manim Tests/InteractivityTest.py -p --renderer=opengl  

Each animation is contained within a class. To run any of the animations type the following:  
manim -pqm GraphTemplate.py classname  

## To run BFSAnim:  
cd .\Templates\  
manim -pqm GraphTemplate.py BFSAnim --renderer=opengl  

BFSAnim Notes:  
Set input mode to 0 for keyboard input, 1 for mouse input.  
When running the program use keyboard to input answer choices  
or mouse to select the node that will be traversed next.  

