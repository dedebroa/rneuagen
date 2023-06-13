import random
from itertools import permutations # itertools = método que cria 'iterators' para loop eficiente 

# algumas funções aqui também podem ser encontradas no arquivo 'funcoes.py'S

#### 30/03: - A.05: Problrma das Senhas
#### 06/04 - A.06: O caixeiro viajante
### 05/06: - GA.03: O caixeiro viajante com gasolina infinita e sem consciência ambiental
def distancia_entre_dois_pontos(a, b):
    """Computa a distância Euclidiana entre dois pontos em R^2
    Args:
      a: lista contendo as coordenadas x e y de um ponto.
      b: lista contendo as coordenadas x e y de um ponto.
    Returns:
      Distância entre as coordenadas dos pontos `a` e `b`.
    """

    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return dist


def cria_cidades(n): # criamos diferentes opções de cidade para quais o caixeiro pode viajar
    """Cria um dicionário aleatório de cidades com suas posições (x,y).
    Args:
      n: inteiro positivo definido nas constantes. Para esse problema, posso dizer que estamos trabalhando com 7.
        Número de cidades que serão visitadas pelo caixeiro.
    Returns:
      Dicionário contendo o nome das cidades como chaves e a coordenada no plano
      cartesiano das cidades como valores.
    """

    cidades = {}

    for i in range(n):
        cidades[f"Cidade {i}"] = (random.random(), random.random()) # tupla: imutável: cidades não saem do lugar # não cabe alterações

    return cidades

def individuo_cv(cidades):
    """Sorteia um caminho possível no problema do caixeiro viajante
    Args:
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as coordenadas das cidades.
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos cada cidade apenas uma vez.
    """
    nomes = list(cidades.keys()) # o método 'keys()' reotorna 'a view object', esse objeto contém as chaves do dicionário
    random.shuffle(nomes) # embaralha todos os nomes
    return nomes 

def populacao_inicial_cv(tamanho, cidades): # a ideia geral de população não muda
    """Cria população inicial no problema do caixeiro viajante.
    Args
      tamanho:
        Tamanho da população.
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista com todos os indivíduos da população no problema do caixeiro
      viajante.
    """
    populacao = []
    for _ in range(tamanho): #range do tamanho da população
        populacao.append(individuo_cv(cidades)) # add na lista o indivíduo gerado
    return populacao

def selecao_torneio_max(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: a implementação aqui vai diferir da implementação encontrada no arquivo 'funcoes.py', pois utilizaremos ele para minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos individuos 
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo tamanho do argumento `populacao`.
    """
    selecionados = [] # tem os individuos que foram selecionados com maior fitness a cada combate (prob. de maximização)

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness)) # zip navega duas listas de ponto a ponto
    # cada item é um par, sendo o primeiro item o indivíduo e o segundo item o fitness desse indivíduo

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)): # for roda o número de vezes da população 
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio) 

        maior_fitness = - float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de maior fitness
            if fit > maior_fitness: 
                selecionado = individuo # passamos por todos os combatentes e pegamos o com maior fitness
                maior_fitness = fit

        selecionados.append(selecionado)

    return selecionados # ninguém morre, só não é selecionado
                        # um individuo pode ser selecionado mais de uma vez 
                        # isso não é um problema pq 1) já sabemos que ele é bom 2) haverá cruzamento 3) haverá mutação

def cruzamento_ordenado(pai, mae):
    """Operador de cruzamento ordenado.
    Neste cruzamento, os filhos mantém os mesmos genes que seus pais tinham,
    porém em uma outra ordem. Trata-se de um tipo de cruzamento útil para
    problemas onde a ordem dos genes é importante e não podemos alterar os genes
    em si. É um cruzamento que pode ser usado no problema do caixeiro viajante.
    Ver pág. 37 do livro do Wirsansky.
    
    Args:
      pai: uma lista representando um individuo
      mae : uma lista representando um individuo
    Returns:
      Duas listas, sendo que cada uma representa um filho dos pais que foram os
      argumentos. Estas listas mantém os genes originais dos pais, porém altera
      a ordem deles.
    """
    
    corte1 = random.randint(0, len(pai) -2) # garantimos que ele nunca vai chegar no final
    corte2 = random.randint(corte1 + 1, len(pai) -1) # se fazemos o corte 2 com base no 1, garantimos que ele não vai chegar no final também
    
    filho1 = pai[corte1:corte2] # cortes definindo a construção do filho # começa pelo pai
    for gene in mae: # precisamos considerar a mãe também
        if gene not in filho1:
            filho1.append(gene)
            
    filho2 = pai[corte1:corte2] # cortes definindo a construção do filho # começa pelo pai
    for gene in pai: # precisamos considerar a mãe também
        if gene not in filho2:
            filho2.append(gene)
             
    return filho1, filho2

def mutacao_de_troca(individuo):
    """Troca o valor de dois genes.
    
    Args:
      Indivíduo: uma lista representado um individuo.
    Return:
      O indivíduo recebido como argumento, porém com dois dos seus genes trocados de posição.
    """
    
    # primeiro passo: selecionar dois individuos
    indices =list(range(len(individuo))) # vamos sortear a posição de genes dentro dos individuos 
    lista_sorteada = random.sample(indices, k = 2) # sorteamos dois índices 
    
    indice1 = lista_sorteada[0]
    indice2 = lista_sorteada[1]
    
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    
    return individuo  
    
    # outro jeito seria:
    # depois de definir os indices
    # gene1 = lista_sorteada[0]
    # gene 2 = lista_sorteada[1]
    # individuo[indice1] = gene2
    # individuo[indice2] = gene1

def funcao_objetivo_cv(individuo, cidades):
    """Computa a funcao objetivo de um individuo no problema do caixeiro viajante.
    
    Args:
      individiuo:
        Lista contendo a ordem das cidades que serão visitadas
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as coordenadas das cidades.
    Returns:
      A distância percorrida pelo caixeiro seguindo o caminho contido no `individuo`. Lembrando que após percorrer todas as cidades em ordem, o
      caixeiro retorna para a cidade original de onde começou sua viagem.
    """

    distancia = 0
    
    for posicao in range(len(individuo) - 1):
                         
        partida = cidades[individuo[posicao]]
        chegada = cidades[individuo[posicao + 1]]
                         
        percurso = distancia_entre_dois_pontos(partida, chegada)
        distancia = distancia + percurso
                         
    # calculando o caminho de volta para a cidade inicial
    partida = cidades[individuo[-1]]
    chegada = cidades[individuo[0]]
                         
    percurso = distancia_entre_dois_pontos(partida, chegada)
    distancia = distancia + percurso
                         
    return distancia

def funcao_objetivo_pop_cv(populacao, cidades):
    """Computa a funcao objetivo de uma população no problema do caixeiro viajante.
    
    Args:
      populacao:
        Lista com todos os indivíduos da população
      cidades:
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Returns:
      Lista contendo a distância percorrida pelo caixeiro para todos os indivíduos da população.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(funcao_objetivo_cv(individuo, cidades))

    return resultado