from webbrowser import Error


class Queqe:
    def __init__(self, n):
        self.tab=[]
        self.n = n

    def add(self, elem):
        if len(self.tab) < self.n:
            self.tab.append(elem)
        else:
            raise Exception("Queqe is full")

    def remove(self):
        if len(self.tab) == 0:
            raise Exception("Queqe is empty")
        else:
            return self.tab.pop(0)
