import sys



def rotate(g, x):

    rotation=[]

    for i in range(x):
        a=[]
        for j in range(x):
            a.append(g[j][i]) # Transformation de colonne en ligne

        rotation.append(a[::-1]) # inversion

    return g == rotation # 1 si vrai 0 si faux
    
    

sys.stdin=open("matrix.in", "r")

n , x = map(int,input().split())

matrix=[]

for _ in range(n): matrix.append(input().split())

resultat = 0

for i in range(n-x+1):

    for j in range(n-x+1):

        mat=[]

        for k in range(x):

            mat.append(matrix[i+k][j:j+x])
        
        resultat += rotate(mat,x)


print(resultat)
