reais = int(input('What do you have left in reais?'))
pesos = int(input('What do you have left in pesos?'))
sol = int(input('What do you have left in sol?'))
euro = int(input('What do you have left in euro?'))

Dollar_Reais = reais * 0.18 
Dollar_Pesos = pesos * 0.00025
Dollar_Sol = sol * 0.28
Dollar_Euro = euro * 0.85

print('In Reais you have', Dollar_Reais)
print('In Pesos you have', Dollar_Pesos)
print('In Sol you have', Dollar_Sol)
print('In Euro you have', Dollar_Euro)


total = Dollar_Reais + Dollar_Pesos + Dollar_Sol + Dollar_Euro

print('The total is', total)