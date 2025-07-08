import time
import datetime
import pygame



def definir_alarme(tempo_alarme):
        print(f"O alarme foi definido para {tempo_alarme}")
        #Para mudar o som do alarme, basta importar um arquivo de som (.mp3) e substituir o valor da variável arquivo_som pelo caminho do arquivo de som desejado
        arquivo_som = "C:\\Users\\Furukawa\\PycharmProjects\\PythonProject001\\Alarme\\Area Zero (Cinematic Arrangement) - Pokémon Scarlet _ Violet(MP3_70K).mp3"

        programa_Rodando = True

        while programa_Rodando:
            tempo_atual = datetime.datetime.now().strftime("%H:%M:%S")
            print(tempo_atual)

            if tempo_alarme == tempo_atual:
                print("Tempo esgotado !")

                pygame.mixer.init()
                pygame.mixer.music.load(arquivo_som)
                pygame.mixer.music.play()

                hit_snooze = False

                while not hit_snooze:
                    acao = input("Aperte 'S' para parar a música: ").upper()


                    if acao != "S":
                        print("Por favor, aperte 'S' para parar a música: ")

                    else:
                        hit_snooze = True

                programa_Rodando = False

            time.sleep(1)

if __name__ == "__main__":
    print("****Despertador do Henrique****")
    programa_principal_rodando = True

    while programa_principal_rodando:
        tempo_alarme = input("Digite o seu horário (HH:MM:SS):")
        try:
            datetime.datetime.strptime(tempo_alarme,"%H:%M:%S")

            definir_alarme(tempo_alarme)
            escolha = input("Deseja programar outro despertador (S/N)?").upper()

            while escolha != "S" and escolha != "N":
                escolha = input("Por favor, escolha uma das opções (S/N): ")

            if escolha == "N":
                programa_principal_rodando = False

        except ValueError:
            print("Por favor, verifique o formato do horário inserido !")


print("Você saiu do programa, volte sempre !")
