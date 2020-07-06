import numpy as np
from mouse import mouse
import time

m = mouse()
steps = 100
q_table = np.load('q_table.npy')
# print(q_table[0,0])
directions = ['right','left','up','down']

statex,statey = m.reset()
for i in range(steps):
	action = np.argmax(q_table[statex,statey])
	
	m.render()
	time.sleep(2)
	new_statex, new_statey, reward, done = m.step(action)
	print(directions[action])
	if done:
		break
	statex,statey = new_statex,new_statey


m.render()
# print(q_table)