# import packages

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import math

# determine frame rate and number of frames in each animation

Nfrm = 20
fps = 5


# create plane of our wave, simulated as a sine wave

def generate(X, Y, phi):
    '''
    Generates Z data for the points in the X, Y meshgrid and parameter phi.
    '''
    R = np.sqrt(X ** 2 + Y ** 2)
    return np.sin(2 * np.pi * X + phi) * R


# create 3D grid

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Make the X, Y mesh for the wave.
xs = np.linspace(0, .3, 50)
ys = np.linspace(0, .3, 50)

# define X and Y of plane
X, Y = np.meshgrid(xs, ys)

# Set the z axis limits so they aren't recalculated each frame.
ax.set_zlim(-1, 1)

# Begin plotting.

# create placeholder for wave and pulsars
wframe = None
points = None
points2 = None
points3 = None
points4 = None
points5 = None
points6 = None
points7 = None
points8 = None

# define the Z motion of the plane and pulsars in that plane

Z = generate(X, Y, 0)
T = generate(.1, .15, 0)
T2 = generate(.25, .2, 0)
T3 = generate(.2, .1, 0)
T4 = generate(.1, .2, 0)
T5 = generate(.05, .05, 0)
T6 = generate(.1, .05, 0)
T7 = generate(.2, .13, 0)
T8 = generate(.03, .2, 0)


# define and update the postion of the wave for each frame

def update(idx):
    phi = phis[idx]
    global wframe
    global points
    global points2
    global points3
    global points4
    global points5
    global points6
    global points7
    global points8

    # remove previous frame before drawing new frame
    if wframe:
        ax.collections.remove(wframe)
    if points:
        ax.collections.remove(points)

    if points2:
        ax.collections.remove(points2)
    if points3:
        ax.collections.remove(points3)
    if points4:
        ax.collections.remove(points4)
    if points5:
        ax.collections.remove(points5)
    if points6:
        ax.collections.remove(points6)
    if points7:
        ax.collections.remove(points7)
    if points8:
        ax.collections.remove(points8)

    # Plot the new wireframe and pause briefly before continuing.

    # define Z coordinates
    Z = generate(X, Y, phi)
    T = generate(.1, .15, phi)
    T2 = generate(.25, .2, phi)
    T3 = generate(.2, .1, phi)
    T4 = generate(.1, .2, phi)
    T5 = generate(.05, .05, phi)
    T6 = generate(.1, .05, phi)
    T7 = generate(.2, .13, phi)
    T8 = generate(.03, .2, phi)

    wframe = ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2, color='blue', linewidth=0.5)

    points = ax.scatter(.1, .15, T, s=100, color='green')
    points2 = ax.scatter(.25, .2, T2, s=100, color='red')
    points3 = ax.scatter(.2, .1, T3, s=100, color='yellow')
    points4 = ax.scatter(.1, .2, T4, s=100, color='orange')
    points5 = ax.scatter(.05, .05, T5, s=100, color='aqua')
    points6 = ax.scatter(.1, .05, T5, s=100, color='black')
    points7 = ax.scatter(.2, .13, T5, s=100, color='gray')
    points8 = ax.scatter(0.03, .2, T5, s=100, color='purple')


    # Function to find distance between pulsar one and all others as they move

    def distance1(x1, y1, z1, x2, y2, z2):

        d = math.sqrt(math.pow(x2 - x1, 2) +
                      math.pow(y2 - y1, 2) +
                      math.pow(z2 - z1, 2) * 1.0)
        print("Distance between pulsar 1 (green) and pulsar 2 (red)", d)

    def distance2(x1, y1, z1, x3, y3, z3):

        d = math.sqrt(math.pow(x3 - x1, 2) +
                      math.pow(y3 - y1, 2) +
                      math.pow(z3 - z1, 2) * 1.0)
        print("Distance between pulsar 1 (green) and pulsar 3 (yellow)", d)

    x1 = .1
    y1 = .15
    z1 = T
    x2 = .25
    y2 = .2
    z2 = T2

    distance1(x1, y1, z1, x2, y2, z2)

    x3 = .2
    y3 = .1
    z3 = T3

    # function call for distance
    distance2(x1, y1, z1, x3, y3, z3)

    # Function to find distance
    def distance3(x1, y1, z1, x4, y4, z4):

        d = math.sqrt(math.pow(x4 - x1, 2) +
                      math.pow(y4 - y1, 2) +
                      math.pow(z4 - z1, 2) * 1.0)
        print("Distance between pulsar 1 (green) and pulsar 4 (orange)", d)

    # Driver Code

    x4 = .1
    y4 = .2
    z4 = T4

    # function call for distance
    distance3(x1, y1, z1, x4, y4, z4)

    def distance3(x1, y1, z1, x5, y5, z5):

        d = math.sqrt(math.pow(x5 - x1, 2) +
                      math.pow(y5 - y1, 2) +
                      math.pow(z5 - z1, 2) * 1.0)
        print("Distance between pulsar 1 (green) and pulsar 5 (aqua)", d)

    # Driver Code

    x5 = .05
    y5 = .05
    z5 = T5

    # function call for distance
    distance3(x1, y1, z1, x5, y5, z5)

    def distance3(x1, y1, z1, x6, y6, z6):

        d = math.sqrt(math.pow(x6 - x1, 2) +
                      math.pow(y6 - y1, 2) +
                      math.pow(z6 - z1, 2) * 1.0)
        print("Distance between pulsar 1 (green) and pulsar 6 (black)", d)

    # Driver Code

    x6 = .1
    y6 = .05
    z6 = T6

    # function call for distance
    distance3(x1, y1, z1, x6, y6, z6)

    def distance3(x1, y1, z1, x7, y7, z7):

        d = math.sqrt(math.pow(x7 - x1, 2) +
                      math.pow(y7 - y1, 2) +
                      math.pow(z7 - z1, 2) * 1.0)
        print("Distance between pulsar 1 (green) and pulsar 7 (grey)", d)

    # Driver Code

    x7 = .2
    y7 = .13
    z7 = T7

    # function call for distance
    distance3(x1, y1, z1, x7, y7, z7)

    def distance3(x1, y1, z1, x8, y8, z8):

        d = math.sqrt(math.pow(x8 - x1, 2) +
                      math.pow(y8 - y1, 2) +
                      math.pow(z8 - z1, 2) * 1.0)
        print("Distance between pulsar 1 (green) and pulsar 8 (purple)", d)
        print(" ")

    # Driver Code

    x8 = .03
    y8 = .2
    z8 = T8

    # function call for distance
    distance3(x1, y1, z1, x8, y8, z8)


# animate code
phis = np.linspace(0, 180. / np.pi, 100)
ani = animation.FuncAnimation(fig, update, Nfrm, interval=1000 / fps)
ani.save('animation.gif', writer='imagemagick', fps=60)
plt.show()
