

 
    
 
import os 

# Adquiri o ID do processo do processo atual 
pid = os.getpid() 
  
# Printa o ID do processo atual  
print(pid) 

# cria um contador com inicio em zero com função de exibir uma mensagem
# "I am alive" a cada vez que o loop é executado. Foi configurado um delay
# de 2 segundos entre cada execução do loop. Após a terceira interação,
# o código sai do loop e exibe a mensagem "I gonna die now, bye."
  
count = 0
while count < 3:
    print("I am alive")
    count += 1  # This is the same as count = count + 1
    import time
    time.sleep(2)

else:
    print("I gonna die now, bye.")
