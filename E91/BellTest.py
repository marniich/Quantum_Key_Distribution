def correlation(measured_bits):
    return sum([1 if a == b else -1 for a, b in measured_bits]) / len(measured_bits)


def BellTest(sequeance_leangh, Alice_basis, Bob_basis, measured_bits):
    
    settings = {
        'ab': [], 'ab_prime': [], 'a_prime_b': [], 'a_prime_b_prime': []
    }
    
    for i in range(sequeance_leangh):
        if Alice_basis[i] == 0 and Bob_basis[i] == 1:
            settings['ab'].append(i)
        elif Alice_basis[i] == 0 and Bob_basis[i] == 3:
            settings['ab_prime'].append(i)
        elif Alice_basis[i] == 2 and Bob_basis[i] == 1:
            settings['a_prime_b'].append(i)
        elif Alice_basis[i] == 2 and Bob_basis[i] == 3:
            settings['a_prime_b_prime'].append(i)

    E_ab = correlation(
        [measured_bits[i][1:3] for i in settings['ab']])
    E_ab_prime = correlation(
        [measured_bits[i][1:3] for i in settings['ab_prime']])
    E_a_prime_b = correlation(
        [measured_bits[i][1:3] for i in settings['a_prime_b']])
    E_a_prime_b_prime = correlation(
        [measured_bits[i][1:3] for i in settings['a_prime_b_prime']])

    S = abs(E_ab - E_ab_prime + E_a_prime_b + E_a_prime_b_prime)
    return S
            