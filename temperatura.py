class Temperatura:

    def __init__(self, c, f, k):
        self.c = c
        self.f = f
        self.k = k

    def c_para_f(self):
        return (self.c * 1.8) + 32

    def f_para_c(self):
        return (self.f - 32) / 1.8

    def c_para_k(self):
        return self.c + 273.15

    def k_para_c(self):
        return self.k - 273.15