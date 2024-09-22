import random
import numpy

def getParity(string):
    ans = 0
    for s in string:
        ans = ans ^ int(s)
    return ans


def biconf(string1, string2, l):
    n = len(string2)
    if(n == 1):
        return l


    first_half_string1_parity = getParity(string1[0: n//2])
    first_half_string2_parity = getParity(string2[0: n//2])
    
    if(first_half_string1_parity != first_half_string2_parity):
        return biconf(string1[0: n//2], string2[0: n//2], l)
    else:
        return biconf(string1[n//2: n], string2[n//2: n], l+n//2)
                                          
def shuffle_two_strings(string1, string2):
    indices = list(range(len(string1)))
    random.shuffle(indices)
    shuffled_string1 = [string1[i] for i in indices]
    shuffled_string2 = [string2[i] for i in indices]

    return shuffled_string1, shuffled_string2

def shell_protocol(string1, string2, k, s):
    for i in range(s):
        idx = k
        while(idx  < len(string1)):
            string1_parity = getParity(string1[idx-k: idx])
            string2_parity = getParity(string2[idx-k: idx])
            if(string1_parity != string2_parity):
                index_to_change = biconf(string1[idx-k: idx], string2[idx-k: idx], idx-k)
                string2[index_to_change] = str(1 - int(string2[index_to_change]))
            idx += k
            
        string1_parity = getParity(string1[idx-k: len(string1)])
        string2_parity = getParity(string2[idx-k: len(string1)])
        if(string1_parity != string2_parity):
            index_to_change = biconf(string1[idx-k: len(string1)], string2[idx-k: len(string1)], idx-k)
            string2[index_to_change] = str(1 - int(string2[index_to_change]))

        #-----------------------------------------------------------------------------------------------------#
    
        string1, string2 = shuffle_two_strings(string1, string2)

    return string1, string2