# DESAFIO 3 - DICIONÁRIOS COM 30 PRODUTOS
produtos = {
    "Smartphone X Pro": 3500.00,
    "Notebook Ultra Fino": 6200.00,
    "Smart TV 55 polegadas": 2800.00,
    "Fone de Ouvido Bluetooth": 450.00,
    "Caixa de Som Portátil": 300.00,
    "Webcam HD": 180.00,
    "Mouse Sem Fio": 75.00,
    "Teclado Mecânico Gamer": 550.00,
    "Monitor Gamer 27 polegadas": 1700.00,
    "Impressora Multifuncional": 900.00,
    "Roteador Wi-Fi 6": 320.00,
    "HD Externo 1TB": 400.00,
    "SSD Interno 500GB": 380.00,
    "Console de Videogame Última Geração": 4999.00,
    "Controle Sem Fio para Console": 300.00,
    "Câmera Digital Profissional": 7800.00,
    "Lente para Câmera (50mm)": 1500.00,
    "Tripé para Câmera": 120.00,
    "Drone com Câmera 4K": 2500.00,
    "Smartwatch Fitness": 800.00,
    "Bicicleta Ergométrica": 1200.00,
    "Esteira Elétrica": 3000.00,
    "Robô Aspirador de Pó": 1100.00,
    "Máquina de Café Espresso": 1300.00,
    "Forno Elétrico de Bancada": 650.00,
    "Liquidificador de Alta Potência": 220.00,
    "Fritadeira Elétrica sem Óleo": 480.00,
    "Panela de Pressão Elétrica": 350.00,
    "Conjunto de Panelas Antiaderente": 600.00,
    "Ferro de Passar a Vapor": 150.00
}

l= []

def extrair_dados():
    for chave, valor in produtos.items():
        print(f"{chave}: {valor}")
        l.append(valor)
        print(l)   
    return l
    
    
n = extrair_dados()

print(" ")
print(" ")


# MÉDIA
media_ = modulo.media(n)
print('Média Produtos: ', media_)

# MEDIANA
med = modulo.mediana(n)
print('Mediana Produtos: ', med)

# MODA
moda = modulo.moda(n)
print('Moda Produtos: ', moda)

print(" ")

# VARIÂNCA
variancia = std.variance(n)
print("Variânca Produtos:", variancia)

# DESVIO PADRÃO
desvio = std.stdev(n)
print("Desvio Padrão Produtos:", desvio)

# AMPLITUDE
amplitude = max(n) - min(n)
print("Amplitude Produtos:", amplitude)


# Perguntas
# 1. Qual é a diferença entre média e mediana?
    # A média é a soma de todos os números divididos pela sua quantidade, enquanto a mediana é o número que fica no meio de numéros pares.
# 2. Por que a moda é importante?
    # A moda é importante para análisar o valor que mais se repete dentre os outros, se tiver um número de reclamações em determinado departamento, a moda indica o tipo de natureza.
# 3. Qual é o significado da variância?
    # A variânca ira medir as dispersões dos dados em relação à sua média.
# 4. Como o desvio padrão relaciona-se com a variância?
    # Eles se relacionam pois o próprio desvio padrão mede a quantidade de dispersões e variâncas presentes no conjunto de dados.
