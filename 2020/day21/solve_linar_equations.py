import numpy as np

A = np.array([[3, -9], [2, 4]])
b = np.array([-42, 2])
#print(A)
#print(b)
z = np.linalg.solve(A, b)
#print(z)

A = np.array([[1, -2, -1], [2,2, -1], [-1, -1, 2]])
b = np.array([6, 1, 1])
z = np.linalg.solve(A, b)
#print(z)




def solve_svd(A,b):
    # compute svd of A
    U,s,Vh = np.linalg.svd(A)

    # U diag(s) Vh x = b <=> diag(s) Vh x = U.T b = c
    c = np.dot(U.T,b)
    # diag(s) Vh x = c <=> Vh x = diag(1/s) c = w (trivial inversion of a diagonal matrix)
    print(s)
    for i in range(len(s)):
        if s[i] > 0:
            s[i] = 1/s[i]

    w = np.dot(np.diag(s),c)
    # Vh x = w <=> x = Vh.H w (where .H stands for hermitian = conjugate transpose)
    print(np.size(Vh.conj().T))
    print(np.size(w))
    x = np.dot(Vh.conj().T,w)
    return x


A = np.array([[1, -2, -1], [2,2, -1]])
b = np.array([6, 1, 1])
u, s, v = np.linalg.svd(A) #, b)
print(u)
print(v)

print(solve_svd(A, b))
