# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 18:49:01 2023

@author: paula_cc_felix
"""

# Exercício 1: Criador de Perfil de Personagem
# Objetivo: O seu desafio é desenvolver um programa Python que permita ao utilizador criar e
# personalizar perfis de personagens fictícios. Para cada perfil, deve incluir, pelo menos, as
# seguintes informações: nome, idade, profissão, hobbies e uma breve descrição.


print("\n= Olá! Vamos ser criativos. Vamos criar perfis de personagens. = \n= Conto consigo! = ")

# Neste scrip optou-se por dar uma tabela inicialmente preenchida com 4 personagens
lista_personagens = [{'nome': 'Ana', 'idade': 19, 'profissão': 'Ambientalista', 'hobbies': ['Acupuntura', 'Pintura'], 'descrição': 'Descrição:A'},
                     {'nome': 'Bruno', 'idade': 32, 'profissão': 'Barbeiro', 'hobbies': ['Comer bitoques', 'Dormir'], 'descrição': 'Descrição:B'},
                     {'nome': 'Carla', 'idade': 49, 'profissão': 'Cantora', 'hobbies': ['Leitura'], 'descrição': 'Descrição:C'},
                     {'nome': 'Duarte', 'idade': 74, 'profissão': 'Reformado da função publica', 'hobbies': ['Viajar', 'Cinema'], 'descrição': 'Descrição:D'}]

def adicionar_personagem(lista_personagens):
    print("\n===> Vamos adicional uma nova personagem")
    nome = input("  => Qual o nome da personagem? ")
    idade = int(input("  => Que idade tem a personagem? "))
    profissao = input("  => Qual a profissão da personagem? ")
    hobbies = input("  => Digite os hobbies do personagem separados por vírgula: ").split(",")
    descricao = input("  => Digite uma breve descrição do personagem: ")
    personagem = {
        "nome": nome,
        "idade": idade,
        "profissão": profissao,
        "hobbies": hobbies,
        "descrição": descricao,
    }
    lista_personagens.append(personagem)
    
    
def modificar_personagem(lista_personagens): 
    modifica_personagem = input("\n====> Indique o nome da personagem que pretende modificar: ")
    for personagem in lista_personagens:
        if personagem["nome"]==modifica_personagem:
            print("===> Vamos modificar um perfil: "+modifica_personagem)
            personagem.update({"nome": input("  => Introduza o novo nome da personagem para "+personagem["nome"] + ": ")})
            personagem.update({"idade": input("  => Introduza a nova idade da personagem para "+personagem["nome"] + ": ")})
            personagem.update({"profissão": input("  => Introduza a nova profissão da personagem para "+personagem["nome"] + ": ")})
            personagem.update({"hobbies": input("  => Introduza o novos hobbies da personagem para "+personagem["nome"] + ": ").split(",")})
            personagem.update({"descrição": input("  => Introduza o nova descrição da personagem para "+personagem["nome"] + ": ")})
            
    
def remover_personagem(lista_personagens):
      remove_personagem = input("\n===> Indique o nome da personagem que pretende remover: ") 
      for i in range(len(lista_personagens)): 
          if lista_personagens[i]['nome'] == remove_personagem: 
              del lista_personagens[i] 
              
              break

def visualizar_personagens(lista_personagens):
     for personagem in lista_personagens:
        print("---------------------------")
        print("Nome:", personagem["nome"])
        print("Idade:", personagem["idade"])
        print("Profissão:", personagem["profissão"])
        print("Hobbies:", ", ".join(personagem["hobbies"]))
        print("Descrição:", personagem["descrição"])
    

def pesquisar_personagem(lista_personagens):
      pesquisa_personagem = input("\n===> Indique o nome da personagem que pretende pesquisar: ")
      for personagem in lista_personagens:
          if personagem["nome"]==pesquisa_personagem:
               print("---------------------------")
               print("Nome:", personagem["nome"])
               print("Idade:", personagem["idade"])
               print("Profissão:", personagem["profissão"])
               print("Hobbies:", ", ".join(personagem["hobbies"]))
               print("Descrição:", personagem["descrição"])
     
    

while True:
    print(" ")
    print("1. Adicionar um novo perfil de personagem")
    print("2. Modificar um perfil de personagem existente")
    print("3. Remover um perfil de personagem")
    print("4. Visualizar a lista completa de personagens")
    print("5. Pesquisar um personagem específico pelo nome")
    print("6. Sair")
    opcao = int(input("Escolha uma das opções indicadas de 1 a 6: "))
    
    if opcao == 1:
        adicionar_personagem(lista_personagens)
    elif opcao == 2:
         modificar_personagem(lista_personagens)
    elif opcao == 3:
         remover_personagem(lista_personagens)     
    elif opcao == 4:
        visualizar_personagens(lista_personagens)
    elif opcao == 5:
        pesquisar_personagem(lista_personagens)    
    elif opcao == 6:
        break
    else:
        print("\n===> "+str(opcao)+" é uma opção inválida! Tente novamente. <===")