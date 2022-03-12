def conversao (quantidade_euro: float, nova_moeda: str)-> float:
    """ Traduzir para 'dollar', 'pound', 'swiss', 'canada', 'japan', 'hongkong'

    Args:
        quantidade_euro (float): quantidade em euros
        nova_moeda (str): moeda para converter
        
    Returns:
        float: quantidade na nova moeda
    """
    if nova_moeda not in ["dollar", "pound", "swiss", "canada", "japan","hongkong"]:
        raise ValueError("Input mal feito")

    #conversao = 0

    if nova_moeda == "dollar":
        conversao = quantidade_euro * 1.09
    
    if nova_moeda == "pound":
        conversao = quantidade_euro * 0.84
    
    if nova_moeda == "swiss":
        conversao = quantidade_euro * 1.02
    
    if nova_moeda == "canada":
        conversao = quantidade_euro * 1.39
    
    if nova_moeda == "japan":
        conversao = quantidade_euro * 127.98
    
    if nova_moeda == "hongkong":
        conversao = quantidade_euro * 8.54
    
    
    return ('%.3f' %conversao)

# Made with love <3 by: TOMAS TEIXEIRA