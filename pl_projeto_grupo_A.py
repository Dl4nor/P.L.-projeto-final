# -*- coding: utf-8 -*-
"""
PL Projeto Grupo

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jNGt6JK5ypfGGlKSKPX--qGS703mySO1

# instalação da biblioteca
pip install gurobipy    -> Rodar comando no terminal

"""

import gurobipy as gp
import math as mt

dados = ["inst_20_3", "inst_20_4", "inst_30_4", "inst_40_8", "inst_40_9", "inst_50_7", "inst_50_10", "inst_60_11", "inst_60_12"]
controle = 1
dataPath = ""

# Contruindo a tabela de escolha dos dados
while (controle > 0 and controle < 10):
  dataPath = "./data/"
  resPath = "./res/A/"

  print("| --------------------------------- |\n"
        "|         seleção de dados          |\n"
        "| --------------------------------- |")
  for i in range(len(dados)):
    if(len(dados[i])>9):
      print("|   {}.  |       {}          |".format(i+1, dados[i]))
    else:
      print("|   {}.  |       {}           |".format(i+1, dados[i]))
  print("| --------------------------------- |\n"
        "|   0.  |       Sair                |\n"
        "| --------------------------------- |")
  controle = int(input("| "))

# Definindo qual será o dado selecionado
  if (controle == 0):
    break

  dataPath += dados[controle-1] + ".txt"
  resPath += dados[controle-1] + ".txt"
  arquivo = open(dataPath, "r")

  #conteudo = arquivo.read()
  m = int(arquivo.readline())  # Número de Cidades
  n = int(arquivo.readline())  # Número de Centro de Distribuição

  C = []                       # Conjunto de cidades que devem ou não receber CD
  E = []                       # Nr total de entregas para cada cidade
  P = []                       # Coordenadas de cada cidade


  for i in range(m):
    aux = arquivo.readline().split()
    Px, Py = int(aux[0]), int(aux[1])
    P.append((Px, Py))
    E.append(int(aux[2]))
    if (int(aux[3])==1):
      C.append(i)

  arquivo.close()

  D = [[mt.sqrt((P[i][0] - P[j][0]) ** 2 + (P[i][1] - P[j][1]) ** 2) for j in range(m)] for i in range(m)]

  # print("P = ", P)
  # print("E = ", E)
  # print("C = ", C)
  # print("D = ", D)

  # Criando um modelo chamado modelo
  modelo = gp.Model()

  # Variável de decisão
  x = modelo.addVars(C, m, vtype = gp.GRB.BINARY)
  y = modelo.addVars(C, vtype = gp.GRB.BINARY)


  # Função Objetivo
  modelo.setObjective(sum(E[j] * D[i][j] * x[i,j] for i in C for j in range(m)), sense = gp.GRB.MINIMIZE)

  # Restrições
  C1 = modelo.addConstrs(
    sum(x[i, j] for i in C) == 1
    for j in range(m)
  )
  C2 = modelo.addConstr(
      sum(y[i] for i in C) == n
  )
  C3 = modelo.addConstrs(
      sum(x[i,j] for j in range(m)) <= m * y[i]
      for i in C
  )

  # Suprimindo terminal
  modelo.setParam("Outputflag", 0)

  # Resolvendo o modelo
  modelo.optimize()

  # Verificando o Status da solução
  status = modelo.Status

  # Resolvendo o modelo
  modelo.optimize()

 
  with open(resPath, "w") as arquivo:

    if(status == 3):
      print("Modelo Infactível!!!", file=arquivo)
    else:
      # Apresentando a solução
      for i in C:
        if(y[i].x > 0.5):
          Dtotal=0
          print("| ----------------------------------------------------------------", file=arquivo)
          print("| O CD {} Atende à:".format(i+1), file=arquivo)
          for j in range(m):
            if (x[i, j].x > 0.5):
              print("|\tCidade {}\t -> \t{:.3f} km \t -> {} Vezes ".format(j+1, D[i][j], E[j]), file=arquivo)
              Dtotal+=D[i][j]*E[j]
          print("|\n| Distancia Total percorrida pela cidade {}\t -> {:.3f} km".format(i+1, Dtotal), file=arquivo)
      print("| ----------------------------------------------------------------", file=arquivo)
      print("| Distância Total de todos os CDs: {:.2f} km".format(sum(E[j] * D[i][j] * x[i, j].X for i in C for j in range(m))), file=arquivo)
      print("| ________________________________________________________________\n", file=arquivo)
  
  arquivo.close()

  if(status == 3):
    print("Modelo Infactível!!!")
  else:
    # Apresentando a solução
    for i in C:
      if(y[i].x > 0.5):
        Dtotal=0
        print("| ----------------------------------------------------------------")
        print("| O CD {} Atende à:".format(i+1))
        for j in range(m):
          if (x[i, j].x > 0.5):
            print("|\tCidade {}\t -> \t{:.3f} km \t -> {} Vezes ".format(j+1, D[i][j], E[j]))
            Dtotal+=D[i][j]*E[j]
        print("|\n| Distancia Total percorrida pela cidade {}\t -> {:.3f} km".format(i+1, Dtotal))
    print("| ----------------------------------------------------------------")
    print("| Valor ótimo: {:.2f} km".format(modelo.ObjVal))
    print("| ________________________________________________________________\n")