# utilizando funções

def imc(altura, peso):
    return peso/((altura/100)*(altura/100))

def classificarPeso(imc):

    if imc < 20:
        return "subpeso"
        pass
    elif imc < 25:
        return "normal"
        pass
    elif imc < 30:
        return "sobre peso"
        pass
    elif imc < 35:
        return "obesidade tipo 1"
        pass
    elif imc < 40:
        return "obesidade tipo 2"
        pass
    else:
        return "obesidade morbida"

print(f"joão tem IMC {imc(170,75):,.2f}", "e sua classicação é", classificarPeso(imc(170,75)))

print(f"José tem IMC {imc(172,55):,.2f}", "e sua classicação é", classificarPeso(imc(172,55)))

print(f"Fulano tem IMC {imc(185,115):,.2f}", "e sua classicação é", classificarPeso(imc(185,115)))

print(f"Fulano tem IMC {imc(187,96):,.2f}", "e sua classicação é", classificarPeso(imc(187,96)))

print(f"FLora tem IMC {imc(165,56):,.2f}", "e sua classicação é", classificarPeso(imc(165,56)))

