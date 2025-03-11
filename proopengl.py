# from OpenGL.GL import *
# import numpy as np
# from numpy import *
# import glfw

# glfw.init( )
# window=glfw.create_window(500, 500, "test", None, None)
# glfw.set_window_pos(window, 100, 100)

# glfw.make_context_current(window)
# glClearColor(200,200,0,0.5)


# vertices = [ -0.50,-0.50,
#             0,0.50,-0.50,
#             0,0,0.50,0]
# colors = [ 1,0,0,
#           0,1,0,
#           0,0,1]
# vertices = np.array(vertices)
# colors = np.array(colors)

# glfw.poll_events()
# glEnableClientState(GL_VERTEX_ARRAY)
# glEnableClientState(GL_COLOR_ARRAY)
# glVertexPointer(3,GL_FLOAT,0,vertices)
# glColorPointer(3,GL_FLOAT,0,colors)

# while not glfw.window_should_close(window):
#     glDrawArrays(GL_TRIANGLES,0,3)
#     glfw.swap_buffers(window)

from OpenGL.GL import *
import glfw
import numpy as np
import time
import math

#window
glfw.init()
window=glfw.create_window(800,800,"draw",None,None)
glfw.make_context_current(window)
glClearColor(0,0,0,1)

points=[]
for theta in range (0,360):
    theta_rad=math.radians(theta)
    x=0.6*math.cos(theta_rad)
    y=0.6*math.sin(theta_rad)
    points.append(x)
    points.append(y)
    points.append(0)
  
glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3,GL_FLOAT,0,points)

# color=[1,0,0,
#        0,1,1]
   
# colors=np.array(color)

# glEnableClientState(GL_COLOR_ARRAY)
# glColorPointer(3,GL_FLOAT,2,color)

while not glfw.window_should_close(window):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_POINT_BIT,0,200)
    # glRotatef(20,0,0,1)

    glDrawArrays(GL_POINT_BIT,199,140)


    glRotatef(20,1,0,1)

    glfw.swap_buffers(window)
    time.sleep(0.1)

   
    


# vertex=[-0.5,0.5,0,
#         0.5,0.5,0,
#         0.5,-0.5,0,
#         -0.5,-0.5,0]

# color=[1,0,0,
#         0,0,1,
#         0,1,0,
#         1,1,0]

# vertex=np.array(vertex)
# colors=np.array(color)
# glEnableClientState(GL_VERTEX_ARRAY)
# glEnableClientState(GL_COLOR_ARRAY)

# glVertexPointer(3,GL_FLOAT,0,vertex)
# glColorPointer(3,GL_FLOAT,0,color)

# while not glfw.window_should_close(window):
#     glfw.poll_events()
#     glClear(GL_COLOR_BUFFER_BIT)
#     glRotatef(20,0,1,0)
#     glDrawArrays(GL_POINT_BIT,0,4)
#     glfw.swap_buffers(window)
#     time.sleep(0.01)



# glfw.terminate()





