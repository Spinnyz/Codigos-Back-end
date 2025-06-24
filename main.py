saldo = 1000
saque_dia = 500
limite_saque = 200

x = saque_dia <= saldo and saque_dia >=limite_saque
print (x)
y =  limite_saque >= saque_dia or saque_dia <= saldo
print (y)