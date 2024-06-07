"""
Osu é jogo de ritmo criado por Dean Herbert em 2007. No modo standart a Jogabilidade dele foi baseada em um outro jogo Osu! Tatakae! Ouendan de nintendo DS.
O jogo Osu! Tatakae! Ouendan basicamente é um jogo de ritmo aonde um circulo aparece na tela e ao mesmo tempo outro circulo com interior translucido chamado "circulo de aproximação" (segundo Osu!Wiki) encolhe ao redor circulo principal no momento que o contorno dos dois circulos se intersecionam o jogador deve clica-lo.

Como se trata de jogo de "Ritmo" geralmente os círculos aparecem na tela em intervalo ritmicos entre os mais comums usados atualmente estão 1/4 (125 ms) e 1/8 (62.5 ms) e os mais raramente utilizados 1/3 (167 ms) e 1/6 (83.3 ms)
No Osu! Tatakae! Ouendan era usado caneta do Nintendo DS para clicar nos circulos, já no Osu! de Dean Herbert pode ser utilizado Mouse, Mesa Digitalizadora, e Touch Screen(Existe uma tabela de classificação de jogadores no Osu! um jogador chamado freedomdiver's quebrou todos recordes em 2017 depois disso ouve uma decisão de separar tabela de classificação dos jogadores de touchscreen da demais.)

Média de vezes jogadas por usuário/m | Performance
1480 | 62 - Brazil
1066 | 98 - Rússia
965 | 119 - EUA
605 | 199 - Singapura
1234 | 47 - China

Se calcularmos Performance / Por quantidade Jogada
China = 0.038
Brazil = 0.041
Russia = 0.091
EUA = 0.123
Singapura = 0.328

O jogador tem uma janela de tempo para clicar o circulo durante a interseção que dura uma mínima fração de tempo definida por uma valor de 1-10 chamada OD (Overall Dificulty) existe 4 possiveis resultados jogador consegue pontos 50, 100, 300 ou erra completamente. Vale lembrar que no jogo apenas "300" é considerado um acerto definitivo já os demais são indesejados, a formula de milissegundos para cada OD segue:

300 : ±-6*(OD-13.25)/Speed
100 : ±-8*(OD-17.4375)/Speed
50 : ±-10*(OD-19.95)/Speed

A Speed é um multiplicador que é relativa a velocidade do mapa da qual um mapa sem modificador (Existem modificadores no jogo que deixam mapa com velocidade x1,5) geralmente tem o valor de 1, uma das OD mais "fáceis" possíveis é o OD 0 pela formula que para acertar uma nota precisamente em OD0 tem porta de tempo de +-199.5 milissegundos, e com OD10 temos uma porta de tempo de 79.5 ms.

(Osu! e o Tempo de Resposta)

A questão é como é que mesmo nos ODs mais fáceis os jogadores conseguem acertar precisamente a nota mesmo que seu tempo de reação do ser humano em média é em torno de 200ms?
A resposta é simples do momento que jogador percebe um círculo dada seu tempo de reação "chamamos de tr" a memória motora do jogador se ativa e temos uma resposta motora com um atraso e chamamos esse atraso de "alpha", o jogador memoriza esse tempo de atraso de acordo com sua capacidades biológica, sabemos que "tr + alpha" deve estar dentro do intervalo de tempo para clicar naquele círculo.

Eu tenho como hipótese que jogadores com melhor tempo de reação tem mais dificuldades inicialmente para ter uma boa precisão ao clicar no circulo, pois como o jogador pode usar tempo de reação de forma a poder clicar o circulo com uma "técnica de força bruta" tendo falsos estímulos falsos positivos do que um jogador que erra constantemente e portanto repara com mais facilidade a necessidade de uma resposta motora automática.

Deve ser levantado a hipótese se jogador acaba de fato "generalizando" esse intervalo de tempo para outras atividades, o que é necessariamente é algo negativo já que esse comportamento atrasa resposta a um estimulo em "alpha", enquanto alguns jogadores dizem que Osu! ajuda na mira e no tempo de reação a casos de jogadores que após aprender jogar Osu! passaram a ter dificuldade.

(Osu! e estado de Atenção)

Existe uma pesquisa interessante que correlaciona Osu! com modificação do estado de atenção e frequência ondas no cérebro, demonstrando que jogar Osu! aumenta velocidade de processamento para atividades complexas.\
"""
