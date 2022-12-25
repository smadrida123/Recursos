#Imprimir lista de posibles posiciones de coordenadas segun x y z y n donde la suma de estos no es igual a n

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

ans = [[i, j, k] for i in range(x+1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(ans)