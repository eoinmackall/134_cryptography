import string

def shift_cipher(k,st):
    """Implements a shift cipher with shift k on string st"""

    a_to_n=dict(zip(string.ascii_lowercase, range(0,26)))
    n_to_a={a_to_n[i]:i for i in a_to_n}

    l=list(st.lower())

    num_l=[a_to_n[n] if n in a_to_n else n for n in l]
    num_shift=[(i+k) % 26 if type(i)==int else i for i in num_l]
    code_w=[n_to_a[n] if type(n) == int else n for n in num_shift]

    st=''.join(code_w)
    return st

def shift_decipher(st):
    """"Brute force check of all shifts of string st"""

    a_to_n=dict(zip(string.ascii_lowercase, range(0,26)))
    n_to_a={a_to_n[i] :i for i in a_to_n}

    l=list(st.lower())

    num_l=[a_to_n[n] if n in a_to_n else n for n in l]

    for m in range(26):
    
        st=''

        decode_t=[(i+m) % 26 if type(i)==int else i for i in num_l]
        decode_w=[n_to_a[n] if type(n) == int else n for n in decode_t]
        
        st=''.join(decode_w)
        print(st)
    return