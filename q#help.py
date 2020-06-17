import numpy as np

np.set_printoptions(precision=4)


# LinAlg shortings
def mul(*args):
    r = args[0]
    for mat in args[1:]:
        r = np.matmul(r, mat)
    return r


mat = lambda a, b, c, d: np.array([[a, b], [c, d]])
inv = np.linalg.inv
eig = lambda x: np.linalg.eig(x)[0]
eigv = lambda x: np.linalg.eig(x)[1]


# Print functions
def prpr(vec):
    a = np.abs(vec[0]) ** 2
    b = np.abs(vec[1]) ** 2
    print("{} |0> + {} |1>   =>   Zero: {}  One: {}".format(vec[0], vec[1], a, b))


# Logic gate declatrations
r2 = 1 / np.sqrt(2)
zero = np.array([1, 0])
one = np.array([0, 1])
I = mat(1, 0, 0, 1)
X = mat(0, 1, 1, 0)
Y = mat(0, -1j, 1j, 0)
Z = mat(1, 0, 0, -1)
Xrot = r2 * mat(1, -1j, -1j, 1)
Xrotr = r2 * mat(1, 1j, 1j, 1)
Yrot = r2 * mat(1, -1, 1, 1)
Yrotr = r2 * mat(1, 1, -1, 1)
S = mat(1, 0, 0, 1j)

H = r2 * mat(1, 1, 1, -1)

a = mat(1, 0, 0, 1)
b = mat(0, 1, 1, 0)

res = mul(zero, H, -Z)
prpr(res)
