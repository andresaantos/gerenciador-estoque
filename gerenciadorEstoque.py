estoque = []

while True:
  opcao = int(input(
  "1. Adicionar Livro \n" \
  "2. Remover Livro \n" \
  "3. Atualizar Livro \n" \
  "4. Listar Livros \n" \
  "5. Procurar Livros \n" \
  "6. Sair \n" \
  "Escolha uma opção: "))

  if(opcao == 1):
    nomeLivro = ""

    while(nomeLivro == ""):
      nomeLivro = input("Nome do livro: ")
      if(nomeLivro == ""):
        print("Digite o nome do livro!")

    nomeAutor = input("Nome do autor: ")

    if(nomeAutor == ""):
      livroCadastrado = [nomeLivro, "Desconhecido"]
    else:
      livroCadastrado = [nomeLivro, nomeAutor]

    estoque.append(livroCadastrado)
    print("Livro cadastrado com sucesso!")
    print("------------------------------ \n")

  elif(opcao == 2):
    removerLivro = input("Digite o nome do livro para remover: ")
    removerAutor = input("Digite o nome do autor para remover: ")

    for i in range(len(estoque)):
      if(removerLivro == estoque[i][0] and removerAutor == estoque[i][1]):
        del estoque[i]
        print("Removido com sucesso!")
        print("------------------------------\n")
        break
    else:
      print("Não há livros ou autores com esse nome, tente novamente.")
      print("------------------------------\n")

  elif(opcao == 3):
    atualizarLivro = input("Qual nome do livro para atualizar? ")
    atualizarAutor = input("Qual nome do Autor para atualizar? ")

    if(atualizarAutor == "" or atualizarLivro== ""):
      print("Você precisa informar tanto o nome do livro quanto o autor.")
      print("------------------------------\n")

    else:
      for i in range(len(estoque)):
        if(atualizarLivro  == estoque[i][0] and atualizarAutor == estoque[i][1]):
          nomeLivroAntigo = estoque[i][0]
          nomeAutorAntigo = estoque[i][1]

          novoNome = input("Qual novo nome? ")
          novoAutor = input("Qual novo Autor? ")

          if(novoNome == ""):
            estoque[i][0] = nomeLivroAntigo
          else:
            estoque[i][0] = novoNome

          if(novoAutor == ""):
            estoque[i][1] = nomeAutorAntigo
          else:
            estoque[i][1] = novoAutor

          print("Editado com sucesso!")
          print("------------------------------\n")
          break

      else:
        print("Não existe livro ou autor com esse nome!")
        print("------------------------------\n")

  elif(opcao == 4):
    if(len(estoque) == 0):
      print("Não há livros cadastrados!")
      print("------------------------------")
      print("\n")

    else:
      for i in range(len(estoque)):
        print("Livro:", estoque[i][0], "|| Autor:", estoque[i][1])
        print("------------------------------")

  elif(opcao == 5):
    nome = input("Qual nome do livro desejado? ")
    encontrou = False

    for i in range(len(estoque)):
      if(nome == estoque[i][0]):
        print(estoque[i])
        print("------------------------------")
        print("\n")
        encontrou = True

    if(encontrou == False):
      print("Não existe livro com esse nome!")
      print("------------------------------")
      print("\n")

  elif(opcao == 6):
    break

  else:
    print("Opção inválida, tente novamente!")
    print("------------------------------\n")

print("Finalizando!")