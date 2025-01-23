import string

def affine_cipher(m,k,st):
    """Applies affine cipher with scaling factor m, shifting factor k to string st"""

    a_to_n=dict(zip(string.ascii_lowercase, range(0,26)))
    n_to_a={a_to_n[i] :i for i in a_to_n}

    st=str(st).lower()
    l=list(st)

    num_l=[a_to_n[n] if n in a_to_n else n for n in l]
    num_aff=[(m*i+k) % 26 if type(i)==int else i for i in num_l]
    code_w=[n_to_a[n] if type(n) == int else n for n in num_aff]

    st=''.join(code_w)
    return st