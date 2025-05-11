import operator
import os

def carregar_palavras(arquivo='palavras.txt'):
    palavras_com_frequencia = {}
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                palavra, frequencia = linha.strip().split()
                if len(palavra) == 5:
                    palavras_com_frequencia[palavra] = int(frequencia)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo}' não foi encontrado. Certifique-se de que ele está no mesmo diretório do script.")
        return None
    return palavras_com_frequencia

def obter_letras_certas(max_letras=5):
    letras_posicao_certa = {}
    print("\n--- Letras com Posição Certa ---")
    print("Digite a letra e a posição (1-5). Ex: 'a 1'. Digite '0' para parar.")
    while len(letras_posicao_certa) < max_letras:
        entrada = input(f"Letra e posição {len(letras_posicao_certa) + 1} (ou 0 para parar): ").lower().strip()
        if entrada == '0':
            break
        try:
            letra, pos_str = entrada.split()
            pos = int(pos_str)
            if not ('a' <= letra <= 'z' and len(letra) == 1 and 1 <= pos <= 5):
                raise ValueError
            if pos in letras_posicao_certa:
                print("Posição já informada. Tente novamente.")
                continue
            letras_posicao_certa[pos] = letra
        except ValueError:
            print("Entrada inválida. Use o formato 'letra posição' (ex: 'e 2') ou '0'.")
    return letras_posicao_certa

def obter_letras_presentes_posicoes_erradas():
    letras_erradas = {}
    print("\n--- Letras Presentes (Posição Errada) ---")
    print("Digite a letra e a posição (1-5) onde ela NÃO está. Ex: 'a 1'. Digite '0' para parar.")
    while True:
        entrada = input("Letra e posição (ou 0 para parar): ").lower().strip()
        if entrada == '0':
            break
        try:
            letra, pos_str = entrada.split()
            pos = int(pos_str)
            if not ('a' <= letra <= 'z' and len(letra) == 1 and 1 <= pos <= 5):
                raise ValueError
            if letra not in letras_erradas:
                letras_erradas[letra] = []
            if pos in letras_erradas[letra]:
                print("Posição já informada para essa letra. Tente novamente.")
                continue
            letras_erradas[letra].append(pos)
        except ValueError:
            print("Entrada inválida. Use o formato 'letra posição' (ex: 'a 1') ou '0'.")
    return letras_erradas

def obter_letras_ausentes():
    letras_ausentes = []
    print("\n--- Letras Ausentes ---")
    print("Digite as letras que NÃO estão na palavra. Ex: 'xyz'. Digite '0' para parar ou se não houver.")
    while True:
        entrada = input("Letras ausentes (ou 0 para parar): ").lower().strip()
        if entrada == '0':
            break
        if not entrada.isalpha() and entrada != '':
            print("Entrada inválida. Digite apenas letras ou '0'.")
            continue
        for letra in entrada:
            if letra not in letras_ausentes:
                letras_ausentes.append(letra)
        break  
    return letras_ausentes

def encontrar_solucoes(palavras_frequencia, certas, presentes_erradas, ausentes):
    solucoes = {}
    for palavra, freq in palavras_frequencia.items():
        valida = True

        for pos, letra in certas.items():
            if palavra[pos-1] != letra:
                valida = False
                break
        if not valida:
            continue

        for letra_a in ausentes:
            if letra_a in palavra:
                valida = False
                break
        if not valida:
            continue

        for letra, posicoes in presentes_erradas.items():
            if letra not in palavra:
                valida = False
                break
            for pos in posicoes:
                if palavra[pos-1] == letra:
                    valida = False
                    break
            if not valida:
                break

        if not valida:
            continue

        solucoes[palavra] = freq

    return dict(sorted(solucoes.items(), key=operator.itemgetter(1), reverse=True))

def main():

    sistema = os.name
    if sistema == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')

    print("Bem-vindo ao Solutor de Termo!")
    print("Quanto mais informação você fornecer, melhores serão as sugestões.")

    palavras_frequencia = carregar_palavras()
    if palavras_frequencia is None:
        return

    letras_certas = obter_letras_certas()
    letras_presentes_erradas_input = obter_letras_presentes_posicoes_erradas()
    letras_certinhas = list(letras_certas.values())
    letras_presentes_erradas = {l: posicoes for l, posicoes in letras_presentes_erradas_input.items() if l not in letras_certinhas}

    letras_ausentes_input = obter_letras_ausentes()
    letras_ausentes = [l for l in letras_ausentes_input if l not in letras_certinhas and l not in letras_presentes_erradas]

    for pos, letra in letras_certas.items():
        if letra in letras_ausentes:
            print(f"Aviso: Letra '{letra}' informada como certa na posição {pos} E ausente. Removendo de ausentes.")
            letras_ausentes.remove(letra)
    for letra in letras_presentes_erradas:
        if letra in letras_ausentes:
            print(f"Aviso: Letra '{letra}' informada como presente E ausente. Removendo de ausentes.")
            letras_ausentes.remove(letra)

    print("\n--- Buscando soluções ---")
    print(f"Certas (posição: letra): {letras_certas}")
    print(f"Presentes (não na posição informada): {letras_presentes_erradas}")
    print(f"Ausentes: {letras_ausentes}")

    solucoes_finais = encontrar_solucoes(palavras_frequencia, letras_certas, letras_presentes_erradas, letras_ausentes)

    if not solucoes_finais:
        print("\noops, nao consegui achar! me desculpe.")
    else:
        print("\nPossíveis respostas (em ordem de probabilidade):")
        for i, (palavra, freq) in enumerate(solucoes_finais.items()):
            print(f"{i+1}. {palavra.upper()} (freq: {freq})")

if __name__ == "__main__":
    main()
