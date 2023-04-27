import random 

#09/03
def gene_cb():
    '''Gera um gene válido para o problema das caixas binárias 
    
    Return:
        Ou retorna zero ou retona um
    '''
    lista = [0, 1] # lá no início dissemos que os genes poderiam assumir dois valores
    gene = random.choice(lista) # pedirei que a função escolha aleatóriamnte um valor para o gene dentro da lista
    return gene # peço que ele retorne a escolha aleatória


def individuo_cb(n):
    '''Gera um indivíduo para o problema das caixas binárias (um indivíduo tem 4 genes)
    
    Argumentos:
        n: número de genes do indivíduo (ou seja, número de caixas)
        
    Return:
        Uma lista com n genes (caixas). Cada gene é um valor zero ou um.
    '''
    individuo = [] # importante lembrar: o indivíduo corresponde ao conjunto de 4 genes, ou seja, ele será uma lista desses 4 valores
    for i in range(n):
        gene = gene_cb()
        individuo.append(gene) # o append adiciona um elemento ao final de uma lista
    return individuo # ou seja, add um gene à lista que corresponde a um indivíduo
    
def funcao_objetivo(individuo):
    '''Computa a função objetivo para o problema das caixas binárias.
    
        Argumentos:
            Individuo: lista contendo os genes das caixas binárias
        
        Return:
            Um valor representando a soma dos genes do indivíduo
    '''
    return sum(individuo) + 1



# 16/03
def populacao_cb(tamanho, n):
    '''Cria uma população no problema das CB.
    
    Args:
        tamanho: tamanho da população.
        n: número de genes de um indivíduo.
        
    Returns:
        uma lista onde cada item é um indivíduo. Um individuo é um cromossomo ou uma lista com n genes.
    '''
    populacao = [] # nossa população ainda é uma lista vazia pois ainda não conhecemos os individuos
    for _ in range(tamanho):
        populacao.append(individuo_cb(n)) # a função dentro do parênteses foi feita em outra aula
        # basicamente, a população vai corresponder à uma lista dos indivíduos 
    return populacao # pedimos a lista, agora com os valores

def selecao_roleta_maxima(populacao, fitness):
    '''Seleciona indivíduos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Args: 
        população: lista com todos os individuos da população
        fitness: lista com os valores da função objetiva dos individuos.
        
    Returns:
        População dos indivíduos selecionados.
    '''
# cada item tem uma chance diferente de ser selecionado, não é a  mesma cance
# famosa lista ponderada
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao)) # k corresponde ao número de repetições
    # seleção é aleatória, mas tem influência dos fitness que são um peso
    # o número de repetições é igual ao tamanho da população (número de elementos da lista)
    return populacao_selecionada # nossa população agora vai corresponder aos melhores

def funcao_objetivo_populacao_cb(populacao):
    '''Calcula a função objetico para todos os membros de uma população.
    
    Argumento:
        população: lista com todos os indivíduos da população
        
    Return:
        Lista de valores representando a fitness de cada indivíduo da população.
    '''
    fitness = []
    for individuo in populacao: #calculando o fitness de cada individuo
        fobje = funcao_objetivo(individuo)
        fitness.append(fobje)
    return fitness

def cruzamento_ponto_simples(pai, mae):
    '''Operador de cruzamento de ponto simples.
    
    Args:
        Pai: uma lista representando um individuo
        Mãe: uma lista representando um outro individuo
        
    Return:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos. Ou seja, 2 filhos no total.
    '''
    
    ponto_de_corte = random.randint(1, len(pai) - 1) # cruzamento de ponto simples no consiste em separar o os genes do individuo em duas partes
    # metade vai para um filho e a outra metade para o outro
    # precisa ser um número inteiro, já que não tem metade de um gene
    # não pode ser zero, pq a intenção não é passar todos os genes de um só para o filho
    # filho tem pai e mãe
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:] #inicio do pai + final da mãe
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:] #inicio da mãe + final do pai
    
    return filho1, filho2 # vamos sempre considerar 2 reprodutores e 2 crias

def mutacao_cb(individuo): 
    '''Realiza a mutação de um gene no problema das CB
    
    Args:
        individuo: uma lista representando um individuo no problema das CB
    Return: 
        um individuo com um gene mutado.
    '''
    
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1) # qualquer gene pode ser mudado desde que ele exista em individuos
    individuo[gene_a_ser_mutado] = gene_cb() # função da aula passada
    return individuo

######## 23 MARÇO
def gene_cnb(valor_max_caixa): #arugumento pode ser só o máximo, pq o mínimo já é definido zero por padrão
    '''Gera um gene válido para o problema das caixas não binárias.
    
    Args:
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Returns:
        um valor entre 0 e 'valor_max_caixa' (incluso)
    '''
    
    gene = random. randint(0, valor_max_caixa) # valor máximo não é mais 1, passa a ser aquele deifnido pela constante
    return gene

def individuo_cnb(numero_genes, valor_max_caixa):
    '''Gera um individuo válido para o problema das caixas não binárias.
    
    Args:
        numero_genes: número de genes na lista que representa o indivíduo;
        valor_max_caixa: valor máximo que a caixa pode assumir.
        
    Returns:
        Uma lista que representa um indivíduo válido para o problema das caixas não-binárias 
    '''
    
    individuo = []
    for _ in range(numero_genes): 
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo 

def populacao_cnb(tamanho_populacao, numero_genes, valor_max_caixa):
    '''Cria uma população de indivíduos para o problema das caixas não binárias.
    
    Args:
        tamanho_populacao: número de individuos da população
        numero_genes: número de egenes do individuo
        valor_max_caixa: valor máximo que a caixa pode assumir
        
    Returns:
        uma lista onde cada item representa indivíduo
    '''
    
    populacao = []
    for _ in range (tamanho_populacao):
        individuo = individuo_cnb(numero_genes, valor_max_caixa)
        populacao.append(individuo)
    return populacao 

def funcao_objetivo_cnb(individuo):
    '''Calcula o fitness do individuo para o problema CNB
    
    Args:
        individuo: lista que representa um individuo 
        
    Returns:
        um valor que representa o fitness do indivíduo
    '''
    fitness = sum(individuo)
    return fitness

def funcao_objetivo_pop_cnb(populacao):
    '''Calcula o fitness da populacao completa
    
    Args:
        populacao = lista com todos os ind. da populacao
        
    Returns:
        uma lista com o fitness de cada individuo de cada individuo em ordem
    '''
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop

def mutacao_cnb(individuo, valor_max_caixa):
    '''Realiza a mutação do individuo
    
    Args:
        individuo: individuo que deve sofrer a mutação
        valor_max_caixa: valor máximo que a caixa pode assumir
    Returns:
        individuo mutado
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo) -1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo 

#### 30/03 - E5: Problema das Senhas
# começando do início: genes, indidividuo e população
# GENES
def gene_letra(letras): # nossas opções já não são mais de 0 a 100 ou 0 e 1, trabalhamos agora com letras 
    """Sorteia uma letra.
    Args:
      letras: letras possíveis de serem sorteadas.
    Return:
      Retorna uma letra dentro das possíveis de serem sorteadas.
    """
    letra = random.choice(letras)
    return letra

# INDIVIDUO
def individuo_senha(tamanho_senha, letras):
    """Cria um candidato para o problema da senha
    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Return:
      Lista com n letras
    """

    candidato = []

    for n in range(tamanho_senha):
        candidato.append(gene_letra(letras))

    return candidato

# POPULAÇÃO
def populacao_inicial_senha(tamanho, tamanho_senha, letras):
    """Cria população inicial no problema da senha
    Args
      tamanho: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras: letras possíveis de serem sorteadas.
    Returns:
      Lista com todos os indivíduos da população no problema da senha.
    """
    populacao = []
    for n in range(tamanho):
        populacao.append(individuo_senha(tamanho_senha, letras))
    return populacao

# roleta não serve mais, ela só serve para maximização (da maneira como fizemos até aqui)
# código para seleção por sorteio
def selecao_torneio_min(populacao, fitness, tamanho_torneio=3):
    """Faz a seleção de uma população usando torneio.
    Nota: da forma que está implementada, só funciona em problemas de
    minimização.
    Args:
      populacao: população do problema
      fitness: lista com os valores de fitness dos individuos 
      tamanho_torneio: quantidade de invidiuos que batalham entre si
    Returns:
      Individuos selecionados. Lista com os individuos selecionados com mesmo
      tamanho do argumento `populacao`.
    """
    selecionados = [] # tem os individuos que foram selecionados com menor fitness a cada combate (prob. de minimização)

    # criamos essa variável para associar cada individuo com seu valor de fitness
    par_populacao_fitness = list(zip(populacao, fitness)) # zip navega duas listas de ponto a ponto
    # cada item é um par, sendo o primeiro item o indivíduo e o segundo item o fitness desse indivíduo

    # vamos fazer len(populacao) torneios! Que comecem os jogos!
    for _ in range(len(populacao)): # for roda o número de vezes da população 
        combatentes = random.sample(par_populacao_fitness, tamanho_torneio) # problema de minimização = queremos o menor fitness

        # é assim que se escreve infinito em python
        minimo_fitness = float("inf")

        for par_individuo_fitness in combatentes:
            individuo = par_individuo_fitness[0]
            fit = par_individuo_fitness[1]

            # queremos o individuo de menor fitness
            if fit < minimo_fitness: 
                selecionado = individuo # passamos por todos os combatentes e pegamos o com menor fitness
                minimo_fitness = fit

        selecionados.append(selecionado)

    return selecionados # ninguém morre, só não é selecionado
                        # um individuo pode ser selecionado mais de uma vez 
                        # isso não é um problema pq 1) já sabemos que ele é bom 2) haverá cruzamento 3) haverá mutação

# mutação
def mutacao_senha(individuo, letras): # a mutação não muda mais números, muda letras 
    """Realiza a mutação de um gene no problema da senha.
    Args:
      individuo: uma lista representado um individuo no problema da senha
      letras: letras possíveis de serem sorteadas.
    Return:
      Um individuo (senha) com um gene mutado.
    """
    gene = random.randint(0, len(individuo) - 1)
    individuo[gene] = gene_letra(letras)
    return individuo

# função objetivo/fitness
# professor acha que essa função é a mais difícil
def funcao_objetivo_senha(individuo, senha_verdadeira):
    """Computa a funcao objetivo de um individuo no problema da senha
    Args:
      individiuo: lista contendo as letras da senha
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      A "distância" entre a senha proposta e a senha verdadeira. Essa distância
      é medida letra por letra. Quanto mais distante uma letra for da que
      deveria ser, maior é essa distância.
    """
    diferenca = 0

    for letra_candidato, letra_oficial in zip(individuo, senha_verdadeira): # zip permite interar em mais de uma lista ao mesmo tempo
        diferenca = diferenca + abs(ord(letra_candidato) - ord(letra_oficial)) # ord está permitindo converter a letra em um número
                                                                               # é sempre o mesmo número, n se atribui valores aleatórios
                                                                            # há diferença entre maísculo e minúsculo

    return diferenca

# func. objetivo população
def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado

### 30/05 - GA.06: Himmenblau


#### 06/04 - A.06: O caixeiro viajante
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
      n: inteiro positivo
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
        Dicionário onde as chaves são os nomes das cidades e os valores são as
        coordenadas das cidades.
    Return:
      Retorna uma lista de nomes de cidades formando um caminho onde visitamos
      cada cidade apenas uma vez.
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


################# 13/04 - A.07: Aplicando restrições na busca ########################
def computa_mochila(individuo, objetos, ordem_dos_nomes):
    """Computa o valor total e peso total de uma mochila
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      valor_total: valor total dos itens da mochila em unidades de dinheiros.
      peso_total: peso total dos itens da mochila em unidades de massa.
    """

    "vamos preencher aqui"
    valor_total = 0
    peso_total = 0
    
    for pegou_o_item_ou_nao, nome_do_item in zip(individuo, ordem_dos_nomes): 
        if pegou_o_item_ou_nao == 1:  # quer dizer que o item já está na mochila
            valor_do_item = objetos[nome_do_item]["valor"] # queremos somente o valor, não o peso, por isso se especifica 
            peso_do_item = objetos[nome_do_item]["peso"] # aqui, não queremos o valor, apenas o peso
            valor_total = valor_total + valor_do_item
            peso_total = peso_total + peso_do_item
            
    return valor_total, peso_total


def funcao_objetivo_mochila(individuo, objetos, limite, ordem_dos_nomes):
    """Computa a funcao objetivo de um candidato no problema da mochila.
    Args:
      individiuo:
        Lista binária contendo a informação de quais objetos serão selecionados.
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são
        dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Valor total dos itens inseridos na mochila considerando a penalidade para quando o peso excede o limite.
    """
    valor_mochila, peso_mochila = computa_mochila(individuo, objetos, ordem_dos_nomes)
      
    # estamos escrevendo aqui o que está como texto na introdução do notebook
    if peso_mochila > limite: 
        return 0.01
    else:
        return valor_mochila

def funcao_objetivo_pop_mochila(populacao, objetos, limite, ordem_dos_nomes):
    """Computa a fun. objetivo de uma populacao no problema da mochila
    Args:
      populacao:
        Lista com todos os individuos da população
      objetos:
        Dicionário onde as chaves são os nomes dos objetos e os valores são dicionários com a informação do peso e valor.
      limite:
        Número indicando o limite de peso que a mochila aguenta.
      ordem_dos_nomes:
        Lista contendo a ordem dos nomes dos objetos.
    Returns:
      Lista contendo o valor dos itens da mochila de cada indivíduo.
    """

    resultado = []
    for individuo in populacao:
        resultado.append(
            funcao_objetivo_mochila(
                individuo, objetos, limite, ordem_dos_nomes
            )
        )

    return resultado

