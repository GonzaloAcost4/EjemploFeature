def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def main():
    print("Calculadora básica")
    print("Operaciones: suma, resta, multiplicación, división")
    
    op = input("Ingrese operación: ").lower()
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))

    if op == "suma":
        print("Resultado:", sumar(a, b))
    elif op == "resta":
        print("Resultado:", restar(a, b))
    elif op == "multiplicación":
        print("Resultado:", multiplicar(a, b))
    elif op == "división":
        print("Resultado:", dividir(a, b))
    else:
        print("Operación no válida.")

if __name__ == "__main__":
    main()
