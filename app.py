import os

restaurantes=[{'nome':'restaurante xp','categoria':'alimento','ativo':False},
              {'nome':'santa','categoria':'carne','ativo':True},
              {'nome':'cwb','categoria':'sushi','ativo':False}]#lista de nomes de restaurantes
   
def exibir_nome_do_programa():
 print("""Sabor Express
         """)
def exibir_opcoes():
 print('1. cadastrar restaurante')
 print('2. listar restaurante')
 print('3. ativar restaurante')
 print('4. sair')
 
def finaliza_app():
   exibir_subtitulo('finalizar aplicativo')

def voltar_ao_menu_principal():
   input('\n digite a tecla "enter"para voltar ao menu principal')
   main()

def opcao_invalida():
  print('opcao invalida\n')
  voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def cadastrar_novo_restaurantes():
      exibir_subtitulo('cadastro de novos restaurantes:')
      nome_do_restaurante=input('digite o nome do novo restaurante')
      restaurantes.append(nome_do_restaurante)
      print(f' o restaurante{nome_do_restaurante}foi cadastrado com sucesso' )
      voltar_ao_menu_principal()
      
def listar_restaurante():
        exibir_subtitulo('listando os restaurantes')

        for restaurante in restaurantes:
          print(f'*{restaurante}')

          voltar_ao_menu_principal

def escolher_opcao():     
   try:     
       opcao_escolhida=int(input('escolha uma opção:'))

       if opcao_escolhida== 1:
          cadastrar_novo_restaurantes()
       elif opcao_escolhida==2:
          listar_restaurante()
       elif opcao_escolhida==3:
          print('ativar restaurantes')
       elif opcao_escolhida==4:
          finaliza_app
       else:
          opcao_invalida()

   except:
    opcao_invalida()

def main():
      os.sistem('clear')
      exibir_nome_do_programa()
      exibir_opcoes()
      exibir_opcoes()

if __name__=='__main__':
  main()


