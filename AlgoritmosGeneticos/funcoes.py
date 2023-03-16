def funcao_objetivo(individuo):
    '''Computa a função objetivo para o problema cb.
    
        Argumentos:
            Individuo: lista contendo os genes das caixas binárias
        
        Return:
            Um valor representando a soma dos genes do indivíduo
    '''
    return sum(individuo) 

#lembrar que aqui não tem célula de texto, comentários precisam ter hashtag

def gene_cb():
    '''Gera um gene válido para o problema das caixas binários 
    
    Return:
        Ou retorna zero ou retona um
    '''
    lista = [0, 1] # lá no início dissemos que os genes poderiam assumir dois valores
    gene = random.choice(lista) # pedirei que a função escolha aleatóriamnte um valor para o gene dentro da lista
    return gene # peço que ele retorne a escolha aleatória
