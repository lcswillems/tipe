import random
import math
import decimal

# u_n = random
def random_1d(nbs):
    set = []
    for i in range(nbs):
        set.append(random.random())
    return [[0, 1], set]

# u_n = (random, random)
def random_2d(nbs):
    set = []
    for i in range(nbs):
        set.append([random.random(), random.random()])
    return [[0, 1], [0, 1], set]

# u_n = n*a mod 1
# où a est irrationnel
def nb1_mult_mod_1(nbs, num, den):
    set = []
    for i in range(nbs):
        set.append(((i*num)/den)%1)
    return [[0, 1], set]

# u_n = (n*a mod 1, n*b mod 1)
# où a et b sont irrationnels
def nbs2_mult_mod_1(nbs, num1, den1, num2, den2):
    set = []
    for i in range(nbs):
        set.append([((i*num1)/den1)%1, ((i*num2)/den2)%1])
    return [[0, 1], [0, 1], set]

# u_n = abs(cos(n))
def abs_cos_n(nbs):
    set = []
    for i in range(nbs):
        set.append(abs(math.cos(i)) % 1)
    return [[0, 1], set]

# z_(n+1) = A*z_n
# où z_n = (x_n, y_n) et A est une matrice 2x2
def gen_alea_plan(nbs, A, z):
    set = []
    for i in range(nbs):
        set.append([z[0]%1, z[1]%1])
        z = [A[0][0]*z[0] + A[0][1]*z[1], A[1][0]*z[0] + A[1][1]*z[1]] 
    return [[0, 1], [0, 1], set]

# x_(n+1) = a*x_n+c
# où a et c sont des entiers
def gen_alea_lin(nbs, a, c, m, x):
    set = []
    y = 0
    for i in range(nbs):
        set.append(y%m)
        y = y*a+c
    return [[0, m], set]

# u_n = (a^n mod 10^k)/10^k
# où a et k sont des entiers
def last_power_digits(nbs, a, k):
    set = []
    seq = 1
    for i in range(nbs):
        set.append(seq/(10**k))
        seq = (seq*a)%(10**k)
    return [[0, 1], set]

# u_n = (p/q)^n
# où p, q et k sont des entiers
def power_mod_1(nbs, p, q):
    set = []
    p2, q2 = p, q
    for i in range(nbs):
        set.append((p2%q2)/q2)
        p2 *= p
        q2 *= q
    return [[0, 1], set]

# u_n = (n % 2pi) / 2pi
def n_mod_2pi_sur_2pi(nbs):
    set = []
    for i in range(nbs):
        set.append((i % (2*math.pi))/(2*math.pi))
    return [[0, 1], set]
