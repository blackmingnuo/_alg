# 方法 a
def power2n_a(n):
    pass
    #return 2**n

# 方法 b：用遞迴 （慢）
def power2n_b(n):
    pass
    #f n == 0: return 1
    #return power2n_b(n-1)+power2n_b(n-1)

# 方法 c：用遞迴 (快)
def power2n_c(n):
     pass
    #if n == 0: return 1
    #return 2*power2n_c(n-1)

# 方法 d：用遞迴+查表
def power2n_d(n):
    #pass
    def ntable (nmax):
        table = [1]
        for i in range (1,nmax+1):
            table.append(table[-1]*2)
        return table
    def power2n1(n,table):
        return table[n]

    max = nmax(40)

print('2^40 =', power2n1(40, nmax))