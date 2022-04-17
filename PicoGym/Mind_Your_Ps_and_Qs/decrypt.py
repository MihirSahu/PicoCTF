# https://www.geeksforgeeks.org/how-to-solve-rsa-algorithm-problems/
# https://pycryptodome.readthedocs.io/en/latest/index.html

from Crypto.Util.number import inverse, long_to_bytes

c = 843044897663847841476319711639772861390329326681532977209935413827620909782846667
n = 1422450808944701344261903748621562998784243662042303391362692043823716783771691667
e = 65537
# Use http://factordb.com/ to find the prime factors of n
p = 2159947535959146091116171018558446546179
q = 658558036833541874645521278345168572231473
phi = (p - 1) * (q - 1)

d = pow(e, -1, phi)
#d = inverse(e, phi)
#t = (c ** d) % n
t = pow(c, d, n)

print(t)
print(long_to_bytes(t))
