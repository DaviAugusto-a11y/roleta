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

        print(f"SEU PRÊMIO É: {resultado}")

    elif opcao == 'n':
        print('obrigado e adeus')
        Flag = False
    
    else:
        print('obrigado e adeus')
        Flag = False

    










    
    
    
    


