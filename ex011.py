larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print('Sua parede tem dimensão de {} x {} e sua área é de {}m² \nPara pintar essa parede, você precisará de {:.2f}l de tinta'.format(larg, alt, (larg * alt), ((larg * alt) / 2)))