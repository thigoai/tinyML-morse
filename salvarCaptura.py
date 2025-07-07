import serial
import time

# Substitua pela sua porta serial
porta = 'COM27'       # No Linux/Mac pode ser /dev/ttyUSB0 ou /dev/ttyS0
baud_rate = 115200   # Igual ao Serial.begin no Arduino

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
