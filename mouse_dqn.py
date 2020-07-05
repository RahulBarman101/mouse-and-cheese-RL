from mouse import mouse
import numpy as np
import random

m = mouse()

### the Q table
q_table = np.zeros((4,4,m.num_actions))
# print(q_table[0,0])

### hyperparameters
num_iter = 15000
steps = 100
epsilon = 1.0   # exploit/explore rate
gamma = 0.95   # reduction value of future values
lr = 0.01    # learning rate
decay = 0.001    # decay rate of gamma
min_epsilon = 0.01    # min amount of decay to be reached

# begin the main for loop of training

for i in range(num_iter):
	statex,statey = m.reset()
	total_reward = 0
	for step in range(steps):
		if random.uniform(0,1) > epsilon:
			action = np.argmax(q_table[statex,statey])
		else:
			action = m.sample()	
		new_statex, new_statey, reward, done = m.step(action)
		q_table[statex,statey,action] += lr * (reward+gamma*np.max(q_table[new_statex,new_statey,:])-q_table[statex,statey,action])
		total_reward += reward
		statex,statey = new_statex,new_statey

		if done:
			break
	epsilon = min_epsilon+(1.0-min_epsilon)*np.exp(-decay*i)
	if i%10 == 0:
		print(f'episode number {i} with total_reward: {total_reward}')


with open('q_table.npy','wb+') as f:
	np.save(f,q_table)




