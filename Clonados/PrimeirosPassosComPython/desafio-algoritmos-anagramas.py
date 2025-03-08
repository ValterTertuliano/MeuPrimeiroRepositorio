def sao_anagramas(p1, p2):
    
    p1 = p1.replace(' ', '').lower()
    p2 = p2.replace(' ', '').lower()

    if len(p1) != len(p2):
        return False
    
    return sorted(p1) == sorted(p2)

palavra1 = 'amor'
palavra2 = 'romas'

if sao_anagramas(palavra1, palavra2):
    print('São anagramas')
else:
    print('Não são anagramas')
