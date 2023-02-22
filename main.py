import random

# Bezpieczenstwo algorytmu RSA jest oparte na trudno±ci rozkladu liczby n na czynniki (problem faktoryzacji).

f = open("dane.txt", "r")
n = int(f.readline())      # n jest to iloczyn 2 liczb pierwszych ktorych szukamy
wyk_d = int(f.readline())  # d jest wykladnikiem prywatnym
e = int(f.readline())      # e jest wykladnikiem publicznym
ed = e * wyk_d
print("n = ",n , "d  = ",wyk_d ,"e = ",e ,"ed = ", ed-1)

#1.Liczbe ed − 1 przedstawiamy w postaci (2^s)* t, gdzie t jest liczba nieparzysta
t = ed-1
s = 0
while t % 2 == 0:
            t = t/2
            s = s + 1
print("t = ",int(t),"s = ",s)
print("-------------------------")

def nwd(l, m):
    while m:
        k = m
        m = l % m
        l = k
    return l

test = False
while test == False:
    # 2. Wybieramy losowo liczbe a z przedzialu 1 < a < n.
    a = random.randint(2, n-1)

    # 3. Obliczamy d = NWD(a, n) poprzez algorytm Euklidesa
    d = nwd(a,n)
    print("a = ",a,"d = ",d)

    # 4. Jezeli d > 1, to zwroc d i STOP.
    if d == 1:
        # 5. Obliczamy b = a^t mod n.
        b = pow(a, int(t), n)
        print("b =", b)
        # 6. Jesli b = 1, to wracamy do 2
        ce = []
        x = 0
        ce.append(b)
        if b != 1:
            # 7. Obliczamy rekurencyjnie c[i] c0 = b, c[i+1] = c[i]^2 mod n az do uzyskania 1, wynika to z własności małego twierdzenia Fermata
            wynik1 = 0
            while wynik1 != 1:
                wynik1 = pow(ce[x], 2, n)
                ce.append(pow(ce[x], 2, n))
                x = x + 1

        # 8. Niech c bedzie ostatnim wyrazem powy»szego ciagu ró»nym od 1.
        c = ce[x-1]
        # 9. Je±li c = n − 1, to wracamy do 2.
        if c != (n-1) and c != 1:
            # 10. d = NWD(c − 1, n) jest dzielnikiem pierwszym n. zwróc d i STOP.
            d = nwd(ce[x - 1] - 1, n)
            print("Pierwszy pierwiastek ", d)
            print("p = ",d)
            print("q =  n/p")
            print ("q = ", int(n/d))
            test = True
        else:
            print("Losujemy ponownie a")
    else:
        print("p = ", d)
        print("q =  n/p")
        print("q = ", int(n / d))