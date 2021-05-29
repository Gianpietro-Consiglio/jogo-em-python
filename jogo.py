import time
import random
import sys
while True:
    c = 0
    secret = ''
    print('Vou sortear um número entre 1 e 100. Você consegue acertar?')
    print('')
    time.sleep(1)
    print('Gerando número...')
    while c < 1:
        c += 1
        secret = random.randint(1, 101)
        
    time.sleep(2)
    tentativas = 0
    while True:
        tentativas += 1
        responda = int(input('Qual número eu gerei? '))
        if responda < secret:
            print('Chute mais alto!')
            print('')

        elif responda > secret:
            print('Chute mais baixo!')
            print('')

        else:
            print('Parabéns, você acertou!')
            print('')
            print(f'Foram necessárias {tentativas} tentativas até o acerto')
            time.sleep(2)
            again = int(input('Deseja jogar novamente?[1-sim,2-não] '))
            print('')
            if again == 1:
                print('Ok, retornando!')
                time.sleep(2)
                break
            elif again == 2:
                print('Obrigado por jogar!')
                time.sleep(2)
                sys.exit()
                
            


            

    
