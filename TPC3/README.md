# Conversor de MarkDown para HTML
## A104445 - Alexandre Marques Miranda
### ![](../imagens/fotoRelatorio.webp)
### 27/2/2025

Para a resolução deste TPC, foi criado um ficheiro TPC3.py onde foi definida uma função para processar as linhas em MarkDown e convertê-las para o formato HTML. Também foi testado com os exemplos mencionados no fichero da Blackboard para este TPC.

Nesta função, estão definidas as substituições dos cabeçalhos, introduzindo o texto após os "#" dentro de "<hn></hn>" em que "n" representa o número de "#" na linha.

Após isso, estão definidas as expressões para o negrito e o itálico por esta ordem para que os "*" que 2 seguidos representando o negrito não sejam identificados como abertura e fecho de texto em itálico. Estas expressões foram introduzidas entre "<b></b>" ou "<i></i>" respetivamente.

O bloco seguinte seleciona o texto que aparece numerado e, para cada uma dessas linhas numeradas, insere a informação dentro de "<li></li>". Após fazer isso para todas as linhas numeradas, insere "<ol>" antes dessas linhas e "</ol>" após as linhas modificadas.

Em relação às imagens e aos links, foram identificados os padrões de cada um dos casos e substituidos para a respetiva notação em HTML.

Para todos esses campos, a informação foi armazenada em grupos para depois poder ser colocada nos campos indicados.