##não funciona se tiver espaços antes... e não retorna True ou False, apenas a aposição da palavra SANTO
##cidade = input('Digite o nome da cidade: ')
##cidade = cidade.upper()
##print(cidade.find ('SANTO'))

cidade = str(input('Digite o nome da cidade: ')).strip()
cidade = cidade.upper()
print(cidade[:5] == ('SANTO'))
