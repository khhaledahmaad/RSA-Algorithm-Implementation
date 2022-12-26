# Step 1
# Calculate n and Euler Totient

def calculate_n_totient(p, q):
    # Calculate n
    n = p * q

    # Calculate Euler Totient
    totient = (p-1)*(q-1)

    return n, totient
    

# Step 2 
# Calculate k, e

# Using Euclidean Algorithm to calculate the GCD
def gcd(x, y):
    while x:
        x, y = y%x, x
    return y

# List of values for e
def calculate_ke(totient):
    e_list = []
    for e in range(2, totient):  # 1 < e < Euler Totient (i.e., 1 < e < φ(n) )
        if gcd(totient, e)== 1: 
            e_list.append(e)

    # Calculate the best k, e
    for i in range(1,10):
        # Create a range of values for k 
        k = 1 + i*totient  # Evaluates to [k % totient == 1]
        for e in e_list:
            if k % e == 0:
                return k, e

# Step 3
# Calculate d
def calculate_d(k, e):
    d = int(k/e)
    return d
    
# Step 4
# Encrypt and decrypt

# Function to encrypt
def encrypt(p, q):
    M = int(input('Enter message (M) (in numeric form): '))
    n=calculate_n_totient(p, q)[0]
    totient = calculate_n_totient(p, q)[1]
    k, e= calculate_ke(totient)
    d = calculate_d(k, e)

    # Ciphertext: C = M^e (mod n)
    C= int((M**e)%n)

    print('n: ', n)
    print('Euler Totient: ', totient) 
    print('(k, e): ', (k, e))
    print('d: ', d)
    print('Public key KU:  {'+ str(e) +', '+ str(n)+'}')
    print('Private key KR: {'+ str(d) +', '+ str(n)+'}')
    print('The Encrypted Message (C): ', C)

# Function to decrypt
def decrypt(p, q):
    C = int(input('Enter a cipher (C) (in numeric form): '))
    n=calculate_n_totient(p, q)[0]
    totient = calculate_n_totient(p, q)[1]
    k, e= calculate_ke(totient)
    d = calculate_d(k, e)

    # Plaintext: M = C^d (mod n)
    M= int((C**d)%n)
    
    print('n: ', n)
    print('Euler Totient: ', totient) 
    print('(k, e): ', (k, e))
    print('d: ', d)
    print('Public key KU:  {'+ str(e) +', '+ str(n)+'}')
    print('Private key KR: {'+ str(d) +', '+ str(n)+'}')
    print('The Decrypted Message (M): ', M)

# Function to select Encryption or Decryption
def rsa_encryption_decryption(p, q):
# Create a selector for input options for encrypt or decrypt
    selector = int(input('Enter 1 if you want to encrypt, or enter 0 if you want to decrypt: '))

    # If true the user can input p, q from the console
    if selector==1:
        return encrypt(p, q)
    else:
        return decrypt(p, q)

