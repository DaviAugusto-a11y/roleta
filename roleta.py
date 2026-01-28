import random
import time

Flag = True

tentativas = ["10", "100", "1000", "lost", "max win 10x"]
probabilidades = [0.5, 0.25, 0.15, 0.09, 0.01]

while Flag == True:
    
    opcao = input('deseja roletar? (s/n)').lower()

    if opcao == 's' :
        print("roletando......")
        time.sleep(3)


        resultado = random.choices(tentativas, probabilidades)[0]

        #aqui ele retorna a lista resusltao que vira apenas 1 indice por isso o 0 no final
        #random.choice criou uma lista com a probabilidade em cima, puxando e faazendo uma lista com apenas 1 item de indice 0
        #o random.choice faz a lista analalisando as opções que são as 'tentativas' e as suas proobabilidades e forma assim

        print(f"SEU PRÊMIO É: {resultado}")

    elif opcao == 'n':
        print('obrigado e adeus')
        Flag = False
    
    else:
        print('obrigado e adeus')
        Flag = False

    










    
    
    
    

