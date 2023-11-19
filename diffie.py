def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primitive_root(p):
    for g in range(2, p):
        if all(pow(g, i, p) != 1 for i in range(1, p - 1)):
            return g
    return None

while True:
    P = int(input("Enter a prime number (P): "))
    if is_prime(P):
        break
    print("Please enter a prime number.")

G = find_primitive_root(P)

x1 = int(input("Enter the private key of User 1: "))
x2 = int(input("Enter the private key of User 2: "))

while x1 >= P or x2 >= P:
    print(f"Private keys should be less than {P}.")
    x1 = int(input("Enter the private key of User 1: "))
    x2 = int(input("Enter the private key of User 2: "))

y1 = pow(G, x1, P)
y2 = pow(G, x2, P)

k1 = pow(y2, x1, P)
k2 = pow(y1, x2, P)

print(f"\nSecret Key for User 1: {k1}")
print(f"Secret Key for User 2: {k2}\n")

if k1 == k2:
    print("Keys have been exchanged successfully.")
else:
    print("Keys have not been exchanged successfully.")