# Análise de um dataset de obras musicais
## A104445 - Alexandre Marques Miranda
### ![](../imagens/fotoRelatorio.webp)
### 20/2/2025

Para a resolução do TPC2 proposto, foram seguidas as etapas abaixo:
- Abertura do ficheiro com os dados de input;
- Validação dos dados;
- Armazenamento dos dados em estruturas de dados adequadas;
- Organização dos dados por ordem alfabética onde requisitado;
- Criação de novos ficheiros com os dados organizados, um para cada ponto pedido.

Para a validação dos dados, foram analisadas uma linha do ficheiro de cada vez, um caracter de cada vez, verificando se se tratava de '\n','"' ou ';'. 

No caso do delimitador, o campo era armazenado na estrutura de dados "fields" e a variável de armazenamento temporária voltava a ter o valor inicial.

No caso das aspas, apenas alterava o valor do booleano que permitia verificar se era um caracter dentro da descrição ou não.

No caso do newline, esse valor era ignorado se o valor de "in_quotes" fosse True, isto é, se estivesse dentro da descrição.

Para o armazenamento de dados, foi criado um conjunto de compositores para que não houvessem compositores repetidos.

Em relação à contagem de músicas e os títulos produzidos em cada período, foram criados dicionários, uma vez que permitia associar cada período à lista de músicas produzidos e os seus valores eram únicos.

Para organizar os dados por ordem alfabética, foi utilizado o método "sort()" no caso do dicionário de títulos e o método "sorted()" no caso dos períodos.

Ficheiro de compositores: [Compositores](compositores.txt)

Ficheiro de total de obras por período: [ObrasPorPeriodo](distribuicao_periodos.txt)

Ficheiro de títulos produzidos em cada período: [TitulosPorPeriodo](obras_por_periodo.txt)