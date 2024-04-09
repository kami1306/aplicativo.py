import os

restaurantes=['pizza','xp']#Lista dos nomes de restaurante
   
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


   
opcao_escolhida=int(input('escolha uma opção:'))
#print('você escolheu a opção', opcao_escolhida)
#print(f'você escolheu a opção(opcao_ecolhida)')

def exibir_subtitulo(texto):
 os.system('clear') #os system('clear')
 print(texto)
 print()

def escolher_opcao():
   
 if opcao_escolhida==1:
    print('cadastrar restaurante')
 elif opcao_escolhida==2:
    print('listar retaurantes')
 elif opcao_escolhida==3:
    print('listar restaurantes')
 else:
    finaliza_app()

def main():
   os.system('clear')
   exibir_nome_do_programa()
   exibir_opcoes()
   escolher_opcao()

   if __name__=='__main':
