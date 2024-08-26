import os
import shutil
import time

# Definindo a pasta que terá os seus arquivos excluídos
pasta_alvo = r"C:\Users\Elias Victor\Desktop\bomba logica\exemplo"
tempo_espera = 10  # segundos

# Remove a pasta e todo o seu conteúdo
def apagar_arquivos(pasta):
    try:
        shutil.rmtree(pasta)
        print(f"Pasta removida com sucesso")
    except Exception as e:
        print(f"Erro ao apagar a pasta")

def bomba_logica():
    tempo_inicio = time.time()
    tempo_fim = tempo_inicio + tempo_espera

    # Realizando a contagem regressiva
    while time.time() < tempo_fim:
        tempo_restante = int(tempo_fim - time.time())
        print(f"Faltam {tempo_restante} segundos")
        time.sleep(1)
    
    print("Remvendo os arquivos...")
    if os.path.exists(pasta_alvo):
        apagar_arquivos(pasta_alvo)
    else:
        print(f"A pasta'{pasta_alvo}' não existe.")

if __name__ == "__main__":
    bomba_logica()
