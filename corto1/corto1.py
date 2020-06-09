#! /usr/bin/python3.8
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False

def collatz(N):
    sec = [N]
    while N != 1:
        if par(N):
            N //= 2
        else:
            N = 3*N + 1
        sec.append(N)
    return sec

#mi numero de carnet es 201700804 por lo tanto mis secuencias generadas son de 2 a 804archivo = open('collatz.txt', 'w')
archivo = open('corto1/collatz.txt', 'w')
for i in range(2, 805):
    archivo.write(str(str(collatz(i))+'\n'))
    print(collatz(i))
archivo.close()
    