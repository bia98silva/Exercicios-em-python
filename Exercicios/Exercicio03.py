def inverter_string(string):
    string_invertida = ""
    for caracter in string:
        string_invertida = caracter + string_invertida
    return string_invertida

string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)
