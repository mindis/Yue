from random import choice
from collections import defaultdict
class SparseMatrix(object):
    def __init__(self):
        self.matrix = defaultdict(dict)
        self.contructed = False

    def set(self,r,c,val):
        self.matrix[r][c]=val

    def get(self,r,c):
        if self.matrix.has_key(r) and self.matrix[r].has_key(c):
            return self.matrix[r][c]
        else:
            print 'No element in row',r,'and column',c
            raise KeyError

    def anyone(self):
        if not self.contructed:
            self.rows = self.matrix.keys()
