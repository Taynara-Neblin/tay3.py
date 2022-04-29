primeiroNOME = input("digite o seu primeiro nome: ")
("Digite seu salário print do mês de abril: ")
salárioreais = input ("Reais: ")
saláriocentavos = input ("centavos: ")
salárioformatado = salárioreais + "," + saláriocentavos
primeiraletra = primeiroNOME [ 0:1].upper()
restantenome = primeiroNOME [ 1:].lower()
primeiroNOMEformatado = primeiraletra + restantenome
mensagem = " o salário de " + primeiroNOMEformatado + " no mês de abril foi " + salárioreais + "," + saláriocentavos + " reais:"
print ( mensagem )