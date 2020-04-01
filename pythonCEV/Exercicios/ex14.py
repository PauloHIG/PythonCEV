#Converta ºC para ºF
#formula  (°C × 9/5) + 32 = °F
cel = float(input('Digite uma temperatura em graus celsius °C'))
fah = (cel * 9 / 5) + 32
print('{}°C = {}°F'.format(cel,fah))