# https://catagolue.hatsya.com/object/xq7_3nw17862z6952/b3s23
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

parser = argparse.ArgumentParser(description='Command line options parser')
parser.add_argument("-sp", "--spaceship", action="store_true", help="Creates a spaceship")
args = parser.parse_args()

ROW = 30
COL = 30
size = (ROW,COL)

if args.spaceship == True:
    glider_pattern = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ], dtype=np.int8)

    # Enlarge to a ROWxCOL matrix
    table = np.zeros((ROW, COL), dtype=np.int8)
    table[0:5, 0:5] = glider_pattern
else:
    proba_0 = 0.6
    table=np.random.choice([0, 1], size=size, p=[proba_0, 1-proba_0])

fig = plt.figure()
plt.axis('off')

im = plt.imshow(table, cmap="gray", animated=True)

def updatefig(*args):
    global table
    bigmask = np.zeros((ROW+2,COL+2))
    for r in range(3):
      for c in range(3):
        if r==c==1:
          continue
        bigmask[0+r:ROW+r, 0+c:COL+c] += table
    mask = bigmask[1:-1,1:-1]
    temp = np.zeros((ROW,COL))
    temp[np.logical_and(table==1, mask==2)]=1
    temp[mask==3]=1
    table = temp.copy()
    im.set_array(table)
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=50, frames=50, blit=True)
plt.show()

from matplotlib.animation import PillowWriter
ani.save("gameOfLife.gif", writer=PillowWriter(fps=4))



