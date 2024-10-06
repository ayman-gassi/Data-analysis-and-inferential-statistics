import math
# Moyenne
def Moyenne(data):
    Somme = 0
    for nbr in data:
        Somme += nbr
    return round(Somme / len(data),2)

# Mediane
def Mediane(data):
    data = sorted(data) 
    Mlength = len(data) // 2  
    if Mlength % 2 == 0:  
        return (data[Mlength - 1] + data[Mlength + 1]) / 2
    else:  
        return data[Mlength]

# Mode
def Mode(data):
    result = []
    for i in range(len(data)):
        FixedNumber = data[i]
        for j in range(i+1,len(data)):
            if data[j]==FixedNumber and FixedNumber not in result :
                result.append(FixedNumber)
    return result

# Variance
def Variance(data):
    result = 0
    moyenne = Moyenne(data)
    for i in range(len(data)):
       result += pow(data[i] - moyenne, 2)
    return round(result / len(data),2)

# Ecart-Type
def EcartType(data):
    return round(math.sqrt(Variance(data)),2)

# Ecart-Type
def Etendu(data):
    return max(data) - min(data)

# Main
data_input = input("Entrez les éléments séparés par des espaces : ")
Data = list(map(int, data_input.split())) 
print("Data")
print(Data)
print("Sorted Data")
print(sorted(Data))
print("La moyenne = ",Moyenne(Data))
print("La mediane = ",Mediane(Data))
print("Le mode" , *Mode(Data))
print("La variance" , Variance(Data))
print("L'Ecart-Type" , EcartType(Data))
print("L'Etendu" , Etendu(Data))





