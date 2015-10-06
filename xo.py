class Board:
	def __init__(self):
		self.empty_token = ' '
		self.arr = [self.empty_token for i in range(9)]

	def is_winner(self):
		if self.arr[0] == self.arr[1] == self.arr[2] and self.arr[0] != ' ':
			return self.arr[0]
		if self.arr[3] == self.arr[4] == self.arr[5] and self.arr[3] != ' ':
			return self.arr[3]
		if self.arr[6] == self.arr[7] == self.arr[8] and self.arr[6] != ' ':
			return self.arr[6]
		if self.arr[0] == self.arr[3] == self.arr[6] and self.arr[0] != ' ':
			return self.arr[0]
		if self.arr[1] == self.arr[4] == self.arr[7] and self.arr[1] != ' ':
			return self.arr[1]
		if self.arr[2] == self.arr[5] == self.arr[8] and self.arr[2] != ' ':
			return self.arr[2]
		if self.arr[0] == self.arr[4] == self.arr[8] and self.arr[0] != ' ':
			return self.arr[0]
		if self.arr[2] == self.arr[4] == self.arr[6] and self.arr[2] != ' ':
			return self.arr[2]
		return self.empty_token

	def is_game_over(self):
		for v in self.arr:
			if v == self.empty_token:
				return False
		return True

	def list_of_moves(self):
		return [i for i, v in enumerate(self.arr) if v == self.empty_token]

	def display(self):
		pass

class AI:
	def __init__(self, board):
		self.board = board
		self.ai_token = 'X'
		self.opponent_token = 'O'

	def play(self, move, curr_token):
		self.board.arr[move] = curr_token
		total = 0
		count = 0
		print curr_token, move
		t = self.board.is_winner()
		if t == self.ai_token:
			self.board.arr[move] = self.board.empty_token
			print 'x is winner'
			return 100
		elif t == self.opponent_token:
			self.board.arr[move] = self.board.empty_token
			print 'o is winner'
			return 0
		elif self.board.is_game_over():
			self.board.arr[move] = self.board.empty_token
			print 'x is draw'
			return 50
		else:
			for m in range(9):
				if self.board.arr[m] == self.board.empty_token:
					total += self.play(m, self.ai_token if curr_token == self.opponent_token else self.opponent_token)
					count = count + 1
			self.board.arr[move] = self.board.empty_token
			return total / count

	def evaluate_move(self):
		moves = self.board.list_of_moves()
		scores = {}
		max_score = 0
		best_move = 0
		print moves
		for m in moves:
			scores[m] = self.play(m, self.ai_token)
			if max_score < scores[m]:
				max_score = scores[m]
				best_move = m
		print scores
		return best_move

def TestCase1():
	board = Board()
	board.arr =		['O', ' ', ' ',
					' ', ' ', ' ',
					' ', ' ', ' ',
			]
	ai = AI(board)
	print ai.evaluate_move()

if __name__ == '__main__':
	TestCase1()
