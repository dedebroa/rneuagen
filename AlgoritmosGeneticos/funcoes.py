def funcao_objetivo(individuo):
    '''Computa a função objetivo para o problema cb.
    
        Argumentos:
            Individuo: lista contendo os genes das caixas binárias
        
        Return:
            Um valor representando a soma dos genes do indivíduo
    '''
    return sum(individuo) 

# lembrar que aqui não tem célula de texto, comentários precisam ter hashtag
