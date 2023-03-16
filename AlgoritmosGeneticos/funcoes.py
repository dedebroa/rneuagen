import random 

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
    return sum(individuo)

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
    return populacao

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
    return populacao_selecionada

def funcao_objetivo_populacao_cb(populacao):
    '''Calcula a função objetico para todos os membros de uma população.
    
    Argumento:
        população: lista com todos os indivíduos da população
        
    Return:
        Lista de valores representando a fitness de cada indivíduo da população.
    '''
    fitness = []
    for individuo in populacao:
        fobje = funcao_objetivo(individuo)
        fitness.append(fobje)
        return fitness