from matplotlib import pyplot as plt
import matplotlib.patches as patches
from random import *
 
m = 10 # para gerar pontos entre 0 e m
n = 10 # número de pontos
 
pontos = [(randint(0,m), randint(0,m)) for i in range(n)]
 
segmentos = [(0,2), (0,3), (5,1), (6,2)]
 
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal')
ax1.tick_params(labelbottom=False, labelleft=False, bottom=False, left=False)
ax1.grid(False)
 
for segmento in segmentos:
  ax1.add_patch(patches.ConnectionPatch(xyA=pontos[segmento[0]], xyB=pontos[segmento[1]], coordsA="data", coordsB="data",color='black'))
 
 
for ponto in pontos:
  ax1.add_patch(patches.Circle((ponto[0],ponto[1]), radius= 0.03*m, color = 'r'))
        
plt.ylim(-1,m+1)
plt.xlim(-1,m+1)
fig1.show()

input()