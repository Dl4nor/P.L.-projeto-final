# Prog. Linear - Projeto Final
<h2>
	<img style="transform: rotateY(180deg)" src="./src/caminhao.png" title="Fôô Fôô" alt="Simbolo de um caminhão" width="5%"/>
 	Problema de Distribuição
</h2>


Uma empresa deseja instalar m centros de distribuição de produtos para atender a n localidades representadas por L1, L2, . . . , Ln. Inicialmente a empresa determinou dentre as n localidades a serem atendidas, um conjunto C contendo aquelas que estariam aptas a receber os centros de distribuição, levando em conta fatores econômicos e estruturais das cidades envolvidas. A empresa estima o número de viagens que serão feitas para cada uma das n localidades a cada semana.
	
	a. Determine quais localidades devem ser escolhidas para abrigar os centros de 
 	   distribuição, associando a cada uma delas os clientes que devem ser atendidos 
	   pelas mesmas, de modo que se minimize a distância total percorrida para as 
	   entregas semanais.

	b. Determine as localidades para os centros de distribuição supondo agora que a 
 	   empresa deseja escolher tais localidades de maneira que as distâncias semanais 
	   percorridas pelos veículos de cada centro sejam as mais próximas possíveis, ou 
	   seja, de modo que haja equilíbrio entre as distâncias percorridas pelas frotas 
	   de cada centro de distribuição.

Utilize distância euclidiana (em linha reta) entre as localidades 

$\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$

---
<h2>
	<a href="https://www.gurobi.com/">
  		<img src="./src/gurobi.png" Title="Gurobi" alt="Símbolo do Gurobi" width="3%"/>
	</a>
  	Projeto Final - Grupo 1 -> Modelo Algébrico:
</h2>

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

