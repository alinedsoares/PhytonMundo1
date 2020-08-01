km = float(input('Qual a quantidade de km percorridos pelo carro? '))
dias = int(input('Qual a quantidade de dias de aluguel? '))
print ('O preço a pagar por {:.1f}km rodados e {} dias de aluguel é {:.2f}'.format(km, dias, (0.15 * km) + (60 * dias)))