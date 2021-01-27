#converter metro para Km, hm,dam,dm,cm,mm

'''

1 decímetro (dm) = 0,1 metros
1 centímetro (cm) = 0,01 metros
1 milímetro (mm) = 0,001 metros

1 decâmetro (dam) = 10 metrosb
1 hectômetro (hm) = 100 metros
1 quilômetro (km) = 1000 metros
'''
n = float(input('Digite um valor em metros: '))
print('{} metros é igual a: \n{} km \n{} hm \n{} dam \n{} m \n{} dm \n{} cm \n{} mm'.format(n ,n/1000 ,n/100 ,n/10 ,n ,n*10 , n*100, n*1000))
