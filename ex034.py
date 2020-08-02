salario = float(input(('Digite o saláqio do funcionário: R$ ')))
if salario <= 1250:
    salario2 = (salario + ((salario / 100) * 15))
    print('O novo salário do funcíonário após 15% (R${:.2f}) de aumento será R${:.2f}'.format(((salario / 100) * 15), salario2))
else:
    salario2 = (salario + ((salario/ 100)* 10))
    print('O novo salário do funcíonário após 10% (R${:.2f}) de aumento será R${:.2f}'.format(((salario / 100) * 10), salario2))
