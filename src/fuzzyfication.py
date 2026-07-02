class fuzzyfication():

    #initialize using ordinal or categorical dictionary and an input number
    def __init__(self, cats: dict, number):
        self.c = list(cats.values())
        self.n = number
        self.result = cats.copy()

    #left fuzzy function
    def f0(self):
        if self.n < self.c[0]:
            return 1
        b = -1/(self.c[1] - self.c[0])
        a = 0 - b*self.c[1]
        f = a + b*self.n
        f = np.clip(f, 0, 1)
        return f

    #last fuzzy function
    def fn(self):
        if self.n > self.c[-1]:
            return 1
        b = 1/(self.c[-1] - self.c[-2])
        a = 0 - b*self.c[-2]
        f = a + b*self.n
        f = np.clip(f, 0, 1)
        return f

    #triangle functions
    def fTri(self, i):
        if self.n <= self.c[i]:
            b = 1/(self.c[i] - self.c[i-1])
            a = 0 - b*self.c[i-1]
            f = a + b*self.n
            f = np.clip(f, 0, 1)
        else: 
            b = -1/(self.c[i+1] - self.c[i])
            a = 0 - b*self.c[i+1]
            f = a + b*self.n
            f = np.clip(f, 0, 1)
        return f

    #apply f to the dictionary 
    def fuzzy(self):
        r=self.f0()
        self.result[list(self.result)[0]] = r
        r=self.fn()
        self.result[list(self.result)[-1]] = r

        for ind in range(1, len(self.c)-1):
            r=self.fTri(ind)
            self.result[list(self.result)[ind]] = r
        return self.result   

    #defuzzifify using the reults across all fuzzyfications. Min of Max
    #Just  use if just one reult is desired
    @staticmethod
    def defuzzification(results: dict, values: list):
        """
            results: activations
            values: corresponding values
        """
        whereMaxima = np.where(np.array(list(result.values())) == np.max(np.array(list(result.values()))))[0]
        values = np.array(values)
        return values[whereMaxima]
