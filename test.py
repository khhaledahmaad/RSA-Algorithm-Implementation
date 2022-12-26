
# Test file
# Import rsa_algorithm.py as module
import rsa_algorithm as rsa
# Import additional libraries
from random import randint

# Create a selector for input options for p, q
selector = int(input('Enter 1 if you want to input p, q from the console, or enter 0 if you want to generate them randomly: '))

# If true the user can input p, q from the console
if selector==1:

    try:
        p = int(input('Enter prime number p: '))
        q = int(input('Enter prime number q: '))
        # Run the functions defined in rsa_algorithm.py file
    except:
        print('p and q must be integer numbers!')
        
# If false p, q will randomly be imported
else:
    p = randint(2, 20) # 1 < (p, q) < 20
    q = randint(2, 20)

    print('Randomly generated p: ', p)
    print('Randomly generated q: ', q)

# Call the functions from the rsa_algorithm.py file
rsa.rsa_encryption_decryption(p, q)