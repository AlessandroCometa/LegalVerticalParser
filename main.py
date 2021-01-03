from random import randint, sample

def env_init():
  board_val = (randint(1,3)*2, randint(3,5))
  print(board_val)
  max_board = max(board_val[0], board_val[1])
  half_board = int(board_val[0]*board_val[1]/2) 
  points_num = randint(max_board, half_board)
  points_val = set(sample(range(2*half_board), points_num))
  return points_val


print(env_init()) 