# P.L.-projeto-final
Projeto final de programação linear do grupo 1 que busca otimizar as entregas de determinado centro de distribuição.

---
 # Projeto Final - Grupo 1 -> Localização

    m Cidades
    n Centros de Distribuição


## Parâmetros:

	C[i] 	-> Cidade i que pode ser centro de distribuição
	E[j] 	-> Número de entregas da cidade j, j = 1,...,m
	P[i] 	-> Coordenada da cidade i, i = 1,...,n
	D[i][j] -> Distnacia da cidade i para o centro j, i = 1,...,n, j = 1,...,m
	D[i][j]  = √((x[i]-x[j])^2 + (y[i]-y[j])^2)


## Variáveis de decisão:
			   | = 1,  Se i atende j, i ∈ C, j = 1,...,n
	x[i][j] -> |
			   | = 0,  Se não

			   | = 1, Se i é um CD, i ∈ C
	y[i]	-> |
			   | = 0, Se não
			   
## Função Objetivo:
			 m
    MIN	 Σ   Σ E[j] * D[i][j] * x[i][j]
	   	i∈C j=1
   
## Restrições:

	 Σ  x[i][j] = 1, j = 1,...m
    i∈C

	 Σ  y[i] = n
    i∈C

     m
	 Σ  x[i][j] <= m * y[i], i ∈ C
    j=1

