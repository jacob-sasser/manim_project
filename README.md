#Animation and Interactivity Research
A project worked on by Jacob Sasser and Brandon Tiseo for the bridges team at UNC Charlotte.< br />
Goal of the project was to demonstrate the capabilities of Manim as an animation engine to be< br />
utilized for Computer Science education.< br />
    
# To run: 
Need to have UV installed, https://docs.manim.community/en/stable/installation.html< br />
other packages needed: pyglet, IPython, numpy, networkx, Manim< br />
To run the project do: uv run manim Tests/InteractivityTest.py -p --renderer=opengl< br />

Each animation is contained within a class. To run any of the animations type the following:< br />
manim -pqm GraphTemplate.py classname< br />

## To run BFSAnim:
cd .\Templates\< br />
manim -pqm GraphTemplate.py BFSAnim --renderer=opengl< br />

BFSAnim Notes:
Set input mode to 0 for keyboard input, 1 for mouse input.< br />
When running the program use keyboard to input answer choices< br />
or mouse to select the node that will be traversed next.< br />

