def calculatrice(operation):
    operation = operation.split()

    while "*" in operation:
        index = operation.index("*")
        result = str(float(operation[index-1]) * float(operation[index+1]))
        operation[index-1:index+2] = [result]
        
        
    while "/" in operation:
        index = operation.index("/")
        try:
            result = str(float(operation[index-1]) / float(operation[index+1]))
            operation[index-1:index+2] = [result]
        except ZeroDivisionError:
            print("Vous avez entrez une division par zéro")
            calcul()

    while "+" in operation:
        index = operation.index("+")
        result = str(float(operation[index-1]) + float(operation[index+1]))
        operation[index-1:index+2] = [result]

    while "-" in operation:
        index = operation.index("-")
        result = str(float(operation[index-1]) - float(operation[index+1]))
        operation[index-1:index+2] = [result]

    return operation[0]


def calcul():
    while True:
        operation = input("Entrez une opération : ")
    
        if operation == 'q':
            break
        
        while "(" in operation and ")" in operation:
            debut = operation.index("(")
            fin = operation.index(")")
            sous_operation = operation[debut+1:fin]
            result = calculatrice(sous_operation)
            operation = operation[:debut] + result + operation[fin+1:]
        
        operation = calculatrice(operation)
        print(operation)


def main():
    print("""
          Calculatrice en ligne de commande.
          Ecrivez la fonction en séparant tout correctement,
          c'est à dire les nombres et les caratères spéciaux ne doivent pas être accolés aux nombres
          A vos risques et périls!!!!!
          """)
    calcul()

if __name__ == "__main__":
    main()
