import pyglet
from pyglet import shapes



window=pyglet.window.Window(800,600,"Test")

start_x,start_y=0,0

@window.event
def on_mouse_press(x,y,button,modifiers):
    global dragging,start_x,start_y 
    dragging=True
    start_x=x
    start_y=y
@window.event
def on_mouse_release(x,y,button,modifiers):
    global dragging
    dragging=False

def on_mouse_drag(x,y,dx,dy,button,modifiers):
    global dragging,start_y,start_x
    if dragging:
        pass #Fix
def run_app(): 
    pyglet.app.run()

def main():
    
    run_app
if __name__ == "__main__":
    from manim import config

    config.media_width = "100%"
    run_app()