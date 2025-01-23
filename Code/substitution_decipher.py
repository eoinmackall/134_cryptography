import string

a_to_n=dict(zip(string.ascii_lowercase, range(0,26)))

with open("ciphertext.txt", "r") as cipher:
    encryption = cipher.read()
    encryption = encryption.lower()

m=list(a_to_n.keys())
encryption=list(encryption)

#encryption=[x for x in l if x in m]

with open("frequency_example.txt", "r") as sample:
    sample = sample.read()
    sample = sample.lower()

sample=list(sample)

#sample=[x for x in l if x in m]

cipher_counts = dict()
c=0
for i in encryption:
    cipher_counts[i] = cipher_counts.get(i, 0) + 1
    c+=1


for i in cipher_counts:
    cipher_counts[i]=(cipher_counts[i]/c)


frequency_counts = dict()
f=0
for i in sample:
    frequency_counts[i] = frequency_counts.get(i, 0) + 1
    f+=1

for i in frequency_counts:
    frequency_counts[i] = (frequency_counts[i]/f)

key = dict()
used_letters=set()

for i in cipher_counts:
    if i in a_to_n:
        initial = i
        token = 'a'
        min=10
        for j in a_to_n:
            if j not in used_letters:
                dist=abs(frequency_counts[j]-cipher_counts[i])
                if dist < min:
                    min = dist
                    token = j
        key[initial]=token
        used_letters.add(token)
    else:
        key[i]=i

swap=[key[n] if n in m else n for n in encryption]

st=''.join(swap)

cipher_counts = {i:cipher_counts[i] for i in cipher_counts if i in a_to_n}
frequency_counts = {i:frequency_counts[i] for i in frequency_counts if i in a_to_n}

with open("ciphertext_decrypted.txt", "w") as cipher_de:
    cipher_de.write(st)

with open("Extra_credit.txt", "w") as extra:
    extra.write("Here is the ciphertext:\n")
    extra.write(str(''.join(encryption))+"\n\n")

    extra.write("These are the frequencies for plaintext occurring in the cipher:\n")
    extra.write(str(cipher_counts)+"\n\n")

    extra.write("These are frequencies for letters appearing in some chosen wikipedia pages:\n")
    extra.write(str(frequency_counts))