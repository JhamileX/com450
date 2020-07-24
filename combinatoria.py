class Combinatoria:

    def combi(self, n,x):
        if(isinstance(n, str ) or isinstance(x, str )):
            self.ans = "error"
            return

        if(n < 0 or x<0 ):
            self.ans = "error"
        else:
            self.factorial(n)
            N = self.value
            self.factorial(x)
            X = self.value
            self.factorial(n-x)
            NX = self.value
            self.ans = N/(X*NX)
    
    def factorial(self, x):
        f = 1
        for i in range(2, x+1):
            f = f * i
        self.value = f
