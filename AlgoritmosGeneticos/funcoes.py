import random 

#09/03
def gene_cb():
    '''Gera um gene válido para o problema das caixas binários 
    
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
        individuo.append(gene)
    return individuo
    
def funcao_objetivo(individuo):
    '''Computa a função objetivo para o problema cb.
    
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
    # nossa população agora vai corresponder aos melhores
    return populacao_selecionada

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
    
    gene = random. randint(0, valor_max_caixa)
    return gene

def individuo_cnb(numero_genes, valor_max_caixa):
    '''Gera um individuoválido para o problema das caixas não binárias
    
    Args:
        numero_genes: número de genes na lista que representa o indivíduo
        valor_max_caixa: valor máximo que a caixa pode assumir
        
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