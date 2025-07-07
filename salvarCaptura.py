import serial
import time


porta = 'COM27'  
baud_rate = 115200  

arquivo_saida = "dados_morse_O.csv"

with serial.Serial(porta, baud_rate, timeout=1) as ser, open(arquivo_saida, 'w') as f:
    print("Gravando dados... Pressione Ctrl+C para parar.")
    try:
        while True:
            linha = ser.readline().decode('utf-8').strip()
            if linha:
                print(linha)
                f.write(linha + "\n")
    except KeyboardInterrupt:
        print("Captura finalizada.")
