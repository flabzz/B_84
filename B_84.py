from bitcoin import random_key, privtopub, pubtoaddr, decode_privkey


# PRIVATE KEY

PRIVATE_KEY = random_key()
print(f'\n Private key =  \"{PRIVATE_KEY}\"')


# PUBLIC KEY

PUBLIC_KEY = privtopub(PRIVATE_KEY)
print(f'\n Public key =  \"{PUBLIC_KEY}\"')

# BITCOIN ADRESS

ADRESS = pubtoaddr(PUBLIC_KEY)
print(f'\n Adress =  \"{ADRESS}\"')


