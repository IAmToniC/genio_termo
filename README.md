# O que é isso?
> Tá com medo de perder sua sequência no Termo?

Esse projeto é um assistente que te ajuda a resolver o jogo Termo, usando informações das letras certas, letras que estão na palavra mas estão fora de posição, e letras ausentes. Ele ordena as possíveis soluções por frequência de uso na língua portuguesa, te dando sugestões cada vez mais precisas.

## Como funciona?
Você roda o script, preenche o que já sabe sobre a palavra, e ele te mostra as palavras mais prováveis com base nas informações que você forneceu. Quanto mais pistas você der, mais certeiro ele fica.

## Sobre o arquivo palavras.txt
O arquivo palavras.txt contém uma lista com todas as palavras de 5 letras da língua portuguesa, junto com uma frequência de uso. Isso permite que o programa sugira palavras mais comuns primeiro, o que aumenta a chance de acertar logo.

## Pra montar esse arquivo:

- Eu usei a lista de palavras com frequência do GitHub: [FrequencyWords](https://github.com/hermitdave/FrequencyWords)

- Depois, filtrei usando o repositório [fserb/pt-br](https://github.com/fserb/pt-br), que tem um vocabulário confiável em português, pra eliminar palavras que não existem na nossa língua.

