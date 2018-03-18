#Plot time on vertical axis and distance on horizontal axis.
# 0 > Time > 100,000 years ago
# 0 < Distance < 100,000 lightyears

#Draw a line that represents your light cone. On a spacetime diagram the maximum slope is 1 which 
#corresponds to the speed of light
#ct vs x

#1.Draw SpaceTime Diagram (Note that time is into the past...)
#2.Mark where I am on the SpaceTime Diagram
#3.Consider F, G, and K stars in Milky Way ~ 100 billion stars
#For N = 10,000 say that 1 in N of these stars has a communication civilisation
#Take the typical lifetime of a communication civilisation to be 10,000 years. 
#--For each communication civ randomly draw an epoch(temporal distance from current epoch) from [0:10 billion years] ~ Uniform
#---IF(choice > 105,000 years) then DISCARD and move on
#--For all remaining civilisations randomly draw a separation from [0:100,000 lightyears] ~ Uniform
#--Indicate the lifetime of each civilisation with a vertical bar of 10,000 years.

import matplotlib.pyplot as plt
import numpy as np
import random as rand

#1
fig = plt.figure()
ax = fig.add_subplot(111)

ax.set_title("Space-Time Diagram - Galactic Demographics - EPSS179 S16 - Conor Power")
ax.set_xlabel("Distance [light years]")
ax.set_ylabel("Time [ct] [years ago] - scaled by c")

major_x_ticks = np.arange(-20000, 101000, 10000)
major_ct_ticks = np.arange(-20000, 101000, 10000)

ax.set_xticks(major_x_ticks)
ax.set_yticks(major_ct_ticks)

ax.axis([-20000, 100000, -20000, 100000])

#2
earth = ax.plot(0,0,marker='^', markersize=12, label = 'Observer')
ax.annotate('Observer', xy=(0,0), xytext=(10000,-10000), arrowprops=(dict(facecolor='black', shrink=0.10, headlength=6, width=2, headwidth=8)))
#lightcone
lightcone = ax.plot([0,100000], [0,100000], label = 'Observer Lightcone')#Slope of 1 on SpaceTime Diagram -> Speed of light
ax.legend(loc='lower left')

ax.plot([0, 0], [-20000,0], '--')
ax.plot([-20000, 0], [0,0], '--')


#3 s_ for scaler a_ for array
s_milkyway_stars = 100000000000
s_N = 10000
s_comm_civ_lifetime = 10000

s_comm_civ_milkyway = int(s_milkyway_stars/s_N)

#All comm civs that satisfy the conditions set out above
a_all_comm_civ = []

for i in range(0, s_comm_civ_milkyway):
    rand_epoch = rand.randrange(0, 10e9, 1)
    if(rand_epoch <= 105000):
        a_comm_civ = [rand_epoch, 0]
        a_all_comm_civ.append(a_comm_civ)
 
for i in range(0, len(a_all_comm_civ)):
    rand_sep = rand.randrange(0, 100000, 1)
    a_all_comm_civ[i][1] = rand_sep


for i in range(0, len(a_all_comm_civ)):
    ax.plot(a_all_comm_civ[i][1], a_all_comm_civ[i][0],marker = 'o')

for i in range(0, len(a_all_comm_civ)):
    x_range = [a_all_comm_civ[i][1], a_all_comm_civ[i][1]]
    y_range = [(a_all_comm_civ[i][0]), (a_all_comm_civ[i][0] - 10000)]#Assume point is when they start transmitting
    ax.plot(x_range, y_range)

plt.show()
