import requests


url_base = "https://pokeapi.co/api/v2/"

def pokemon_info(name):
    url = f"{url_base}/pokemon/{name}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        pokemon = resposta.json()
        return pokemon


    elif resposta.status_code == 404:
        print(f"Erro, esse pokemón não existe, por favor, insira um pokemón válido")


    else:
        print("Um erro inesperado ocorreu")


def main():
    programa_Rodando = True

    while programa_Rodando:
        nome = input("Digite o nome de um pokemón: ").lower()
        while not nome:
         nome = input("Por favor, digite o nome de um pokemón: ").lower()

        dados = pokemon_info(nome)

        if dados:
            print(f"O pokemón {dados["name"]} pesa {dados["weight"]/10}kg ( ou {dados["weight"]*100}g ) e mede {dados["height"]/10}m ( ou {dados["height"]*10}cm )")

        escolha = input("Deseja escolher um novo pokemón (S/N) ?: ").upper()

        if escolha != "S" and escolha != "N":
            print("Por favor, insira uma opção válida !")
            escolha = input("Deseja escolher um novo pokemón (S/N) ?: ").upper()

        if escolha == "N":
            programa_Rodando = False

    print("Você saiu do programa, volte sempre !")


if __name__ == "__main__":
    main()


