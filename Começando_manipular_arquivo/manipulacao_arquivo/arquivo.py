arquivo = open('C:\\Users\\PC\\Downloads\\python\\Começando_manipular_arquivo\\manipulacao_arquivo\\nomes.txt','w')
arquivo.write("Carlos")
arquivo.writelines(["\nTesus", "\nJoana","\nMaria"])
arquivo.close()

caminho_arquivo ='C:\\Users\\PC\\Downloads\\python\\Começando_manipular_arquivo\\manipulacao_arquivo\\nomes.txt'
arquivo = open (caminho_arquivo, 'r')
linhas = arquivo.readlines()
for i,linha in  enumerate(linhas, start=1):
    print(f'Linha{i}: {linha}')
