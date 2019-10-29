

import numpy as np
import json

# ass : 質量(kg)
# vel_x: X方向初速(m/s)
# vel_y: Y方向初速(m/s)
# vel_z: Z方向初速(m/s)
# Force_x : X方向的分力(N)
# Force_y : Y方向的分力(N)
# Force_z : Z方向的分力(N)

def delt(v, m, f, t):
    a = f / m
    s = v * t + (a * t * t / 2)
    return s

with open('/Users/chenthungfang/desktop/homework.json') as json_file:
    data = json.load(json_file)  # type: dict

c = ['x', 'y', 'z']
velo = np.ones(3)
forc = np.zeros(3)
poit = np.zeros(3)
m = 1

if data. __contains__("ass"):
    m = data["ass"]
    for i in mass:
        i = m

for i in range(3):
    f_now = "Force_" + c[i]
    v_now = "vel_" + c[i]
    if data. __contains__(f_now):
        forc[i] = data[f_now]
    if data. __contains__(v_now):
        velo[i] = data[v_now]



t = 10
for i in range(3):
    # print(c[i] + " -> " + str(velo[i]) + " " + str(m) + " " + str(forc[i]))
    print("position_" + c[i] + ": " + str(delt(velo[i], m, forc[i], t)))