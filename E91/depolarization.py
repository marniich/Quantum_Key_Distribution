import numpy as np

def pauli_i():
    return np.array([[1,0],[0,1]])
def pauli_x():
    return np.array([[0,1],[1,0]])

def pauli_y():
    return np.array([[0,-1j],[1j,0]])

def pauli_z():
    return np.array([[1,0],[0,-1]])

def apply_kraus(rho,k):
    return np.matmul(k,np.matmul(rho, np.conj(k.T)))

def channel(rho,kraus):
    ans = np.zeros(rho.shape,dtype=np.cdouble)
    for k in kraus:
        ans += apply_kraus(rho,k)
    return ans

def depolarizing_kraus(p):
    return [np.sqrt(1-3*p/4)*pauli_i(), np.sqrt(p/4)*pauli_x(),np.sqrt(p/4)*pauli_y(),np.sqrt(p/4)*pauli_z()]

def identity_kraus():
    return pauli_i()

def bipartite_gate(kraus1,kraus2):
    bipartite_kraus = []
    for k1 in kraus1:
        for k2 in kraus2:
            bipartite_kraus.append(np.kron(pauli_i(), np.kron(k1,k2)))
    return bipartite_kraus



'''
def apply_noise(rho, prob):
    return prob * rho + (1 - prob) * np.eye(2) / 2
'''


"""
def depolarization_noise(inital_rho, p, q, d = 3):
    basis = np.array([[1, 0], [0, 1]])
    final_rho = np.array([0 + 0j] * (2**d)*(2**d))
    final_rho = final_rho.reshape((2**d), (2**d))
    for i in range(2**d):
        for j in range(2**d):
            final_rho += inital_rho[i][j] * np.kron(np.kron(np.outer(basis[(i//4)%2], basis[(j//4)%2]), apply_noise(np.outer(basis[(i//2)%2], basis[(j//2)%2]), p)), apply_noise(np.outer(basis[i%2], basis[j%2]), q))


    return final_rho
"""