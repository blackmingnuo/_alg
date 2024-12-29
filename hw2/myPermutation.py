def perm_swap(n):
    def generate(p, i):
        if i == n:
            print(p)
            return
        for j in range(i, n):  
            p[i], p[j] = p[j], p[i]  
            generate(p, i + 1)       
            p[i], p[j] = p[j], p[i]  

    generate(list(range(n)), 0)

perm_swap(2)  
perm_swap(3)  
perm_swap(4)  
perm_swap(5)  
