from itertools import combinations_with_replacement as combwr

def sum_platonic(n: int, notation_limit: int, f):
    numbers = list(range(f(n)))
    for i in range(notation_limit + 1):
        for j in combwr(map(f, range(1, n)), i):
            if sum(j) in numbers:
                numbers.remove(sum(j))
    return numbers

def sum_tetrahedral(n):
    return sum_platonic(n, 5, lambda x: (x*(x+1)*(x+2))//6)

def sum_octahedral(n):
    return sum_platonic(n, 7, lambda x: (x*((2*x*x)+1))//3)

def sum_cube(n):
    return sum_platonic(n, 9, lambda x: x**3)

def sum_icosahedral(n):
    return sum_platonic(n, 13, lambda x: (x*((5*x*x)-5*x+2))//2)

def sum_dodecahedral(n):
    return sum_platonic(n, 21, lambda x: (x*((3*x) -1)*((3*x)-2))//2)

