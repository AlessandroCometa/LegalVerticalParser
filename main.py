from random import randint, sample

class Environment:
  
  def __init__(self):
    
    rows = randint(1,2)*3
    cols = randint(3,6)
    self.board = (rows, cols, rows*cols)
    print("{} rows * {} cols = {} cells".format(*self.board))
    self.points = sample(range(self.board[2]), randint(self.board[1], int(self.board[2]/3)))
    print("Notable points in cells: {}".format(sorted(self.points)))
    
  def __repr__(self):
    
    i_idx = self.points.pop(0)
    print(i_idx)
    g_idx = self.points.pop(-1)
    print(g_idx)
    e_list = ["o" if i in self.points else "i" if i == i_idx else "g" if i == g_idx else "#" for i in range(self.board[2])]
    return e_list
    
  def __str__(self):
    
    e_list = self.__repr__()
    e_matr = [[e_list[j+i*self.board[1]] for j in range(self.board[1])] for i in range(self.board[0])]
    e_str = ""
    for i in e_matr:
      e_str = str(*i) + "/n"
    return e_str
    
Lalla = Environment()
print(*Lalla.__repr__())
print(Lalla)