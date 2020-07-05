import numpy as np
# directions = ['right','left','up','down']
class mouse:
	def __init__(self):
		self.board = np.ones((4,4),dtype=str)
		self.MOUSE = 'M'
		self.done = False
		# self.num_states = self.board.shape[0]*self.board.shape[1]
		self.num_actions = 4

	def reset(self):
		self.posx = 0
		self.posy = 0
		self.reward = 0
		self.scheese = 1
		self.mcheese = 1
		self.lcheese = 1
		self.scheesx,self.scheesy = 2,1
		self.mcheesx,self.mcheesy = 1,2
		self.lcheesx,self.lcheesy = 3,3
		self.trapx,self.trapy = 2,2
		self.board = np.ones((4,4),dtype=str)
		self.board[self.posx][self.posy] = self.MOUSE
		self.board[self.scheesx][self.scheesy] = 'q'
		self.board[self.mcheesx][self.mcheesy] = 'w'
		self.board[self.lcheesx][self.lcheesy] = 'e'
		self.board[self.trapx][self.trapy] = 'TR'
		return [self.posx,self.posy]

	def step(self,action):
		reward = 0
		#### actions - 0: right 1: left 2: up 3: down
		if action == 0:
			if self.posy != 3:
				self.board[self.posx][self.posy] = '1'
				self.posy += 1
				reward += self.get_reward()
				self.board[self.posx][self.posy] = self.MOUSE
				self.done = self.is_done()
			else:
				reward += self.get_reward()
		elif action == 1:
			if self.posy != 0:
				self.board[self.posx][self.posy] = '1'
				self.posy -= 1
				reward += self.get_reward()
				self.board[self.posx][self.posy] = self.MOUSE
				self.done = self.is_done()
			else:
				reward += self.get_reward()
		elif action == 2:
			if self.posx != 0:
				self.board[self.posx][self.posy] = '1'
				self.posx -= 1
				reward += self.get_reward()
				self.board[self.posx][self.posy] = self.MOUSE
				self.done = self.is_done()
			else:
				reward += self.get_reward()
		else:
			if self.posx != 3:
				self.board[self.posx][self.posy] = '1'
				self.posx += 1
				reward += self.get_reward()
				self.board[self.posx][self.posy] = self.MOUSE
				self.done = self.is_done()
			else:
				reward += self.get_reward() 

		return self.posx,self.posy,reward,self.done

	def sample(self):
		action = np.random.choice([0,1,2,3])
		# print(directions[action])
		return action

	def get_reward(self):
		if self.posx == self.scheesx and self.posy == self.scheesy:
			if self.scheese == 1:
				reward = 25
				self.scheese -= 1
				self.board[self.scheesx][self.scheesy] = '1'
			else:
				reward = -1
		elif self.posx == self.mcheesx and self.posy == self.mcheesy:
			if self.mcheese == 1:
				reward = 50
				self.mcheese -= 1
				self.board[self.mcheesx][self.mcheesy] = '1'
			else:
				reward = -1
		elif self.posx == self.lcheesx and self.posy == self.lcheesy:
			if self.lcheese == 1:
				reward = 100
				self.lcheese -= 1
				self.board[self.lcheesx][self.lcheesy] = '1'
			else:
				reward = -1
		elif self.posx == self.trapx and self.posy == self.trapy:
			reward = -500
		else:
			reward = -1
		return reward

	def is_done(self):
		if self.posx == self.trapx and self.posy == self.trapy:
			print('done by trap')
			return True
		elif self.scheese == 0 and self.mcheese == 0 and self.lcheese == 0:
			print('finished')
			return True
		else:
			return False

	def render(self):
		print(self.board)

