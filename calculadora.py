nome = input("Digite o nome completo do astronauta: ")
distancia = float(input("Digite a distância da viagem em quilômetros: "))
velocidade = float(input("Digite a velocidade média da nave em km/h: "))

tempo_horas = distancia / velocidade #calcula o tempo em horas
tempo_dias = tempo_horas / 24 #Calcula o tempo em dias

print(f"\nAstronauta {nome}, bem-vindo à simulação!")
print(f"A viagem terá uma distância de {distancia:g} km (até a Lua).")
print(f"Com velocidade média de {velocidade:g} km/h, o tempo estimado é:")
print(f"{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).")
print("Boa sorte na missão!")