class patterns:
    def __init__(self,n):
        self.n = n
    def lowerTriangle(self) ->None:
        for i in range(self.n):
            for j in range(self.n):
                if i>=j:
                    # print('*',end=' ')
                    print(i+1 ,end=' ')
            print()
    def upperTriangle(self) -> None:
        for i in range(self.n):
            for j in range(self.n,
                           ):
                if i<=j:
                    # print('*',end =' ')
                    print(j ,end=' ')
            print()

obj = patterns(5)
# obj.lowerTriangle()
obj.upperTriangle()