class Exp:  
    def eval(self):
        pass

class Num(Exp):  
    def __init__(self, value):
        self.value = int(value)

    def eval(self):
        return self.value   

class BinOp(Exp):  
    def __init__(self, left, op, right):
        self.left = left  
        self.op = op  
        self.right = right  

    def eval(self):
        if self.op == '+':
            return self.left.eval() + self.right.eval()
        elif self.op == '-':
            return self.left.eval() - self.right.eval()
        elif self.op == '*':
            return self.left.eval() * self.right.eval()
        elif self.op == '/':
            return self.left.eval() / self.right.eval()
