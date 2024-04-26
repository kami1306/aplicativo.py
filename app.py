import os

restaurantes=[{'nome':'restaurante xp','categoria':'alimento','ativo':False},
              {'nome':'santa','categoria':'carne','ativo':True},
              {'nome':'cwb','categoria':'sushi','ativo':False}]
   
def exibir_nome_do_programa():
 print("""Sabor Express
         """)
def exibir_opcoes():
 print('1. cadastrar restaurante')
 print('2. listar restaurante')
 print('3. ativar restaurante')
 print('4. sair')
 
def finaliza_app():
   exibir_subtitulo('finalizar app')

def voltar_ao_menu_principal():
   input('\n digite a tecla "enter"para voltar ao menu principal') 
   main()

def opcao_invalida():
  print('opcao invalida!\n')
  voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha='*'*(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurantes():
 exibir_subtitulo('cadastro de novos restaurantes:') 
nome_do_restaurante=input('digite o nome do novo restaurante:')
categoria=input(f'digite a categoria do restaurante{nome_do_restaurante}:')
dado_do_restaurante={'nome':nome_do_restaurante,'categoria':categoria,'ativo':False}
restaurantes.append(dado_do_restaurante)
print(f' o restaurante{nome_do_restaurante}foi cadastrado com sucesso!' )
voltar_ao_menu_principal()
      
def listar_restaurante():
        exibir_subtitulo('listando os restaurantes')
        
        print (f'{"nome do restaurante".ljust(22)}|{categoria.ljust(20)} |status')
        for restaurante in restaurantes:
         nome_do_restaurante=restaurantes['nome']
         categoria=restaurante['categoria']
         ativo = 'ativado'if restaurante['ativo'] else 'desativado'
         print(f'-{nome_do_restaurante.ljust(20)}|{categoria.ljust(20)}|{ativo}')

voltar_ao_menu_principal()

def alternar_estado_restaurante():
   exibir_subtitulo('alternado estado do restaurante')
   nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado:')
   restaurante_encontrado= False

   for restaurantes in restaurantes:
         if nome_do_restaurante==restaurantes['nome']:
         restaurantes_encontrado = True
         restaurantes['ativo']=not restaurantes['ativo']
         mensagem=f'o restaurante {nome_do_restaurante}foi ativado com sucesso'if restaurantes['ativo']else f'o restaurante{nome_do_restaurante}foi desativado com sucesso!' 

         print(mensagem)
         

      if not restaurante_encontrado:
            print('o restaurante não foi encontrado')
      voltar_ao_menu_principal()

def escolher_opcao():     
   try:     
       opcao_escolhida=int(input('escolha uma opção:'))

       if opcao_escolhida== 1:
          cadastrar_novo_restaurantes()
       elif opcao_escolhida==2:
          listar_restaurante()
       elif opcao_escolhida==3:
          alternar_estado_restaurante()
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


