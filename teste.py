pos_prvimport openpyxl
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import webbrowser

# Caminho do arquivo Excel
arquivo_excel = 'Energy - Orçado x Realizado.xlsx'

# Abre o arquivo
wb = openpyxl.load_workbook(arquivo_excel,data_only=True)

# Seleciona a aba (sheet) desejada
aba = wb.active  # ou wb['NomeDaAba']

# Seleciona pela linha e coluna (linha 1, coluna 1)

ultima_linha = aba.max_row
ultima_coluna = aba.max_column

#print(ultima_coluna,ultima_linha)
Entradas_Realizadas =[]
Saidas_Realizadas = []       
Entradas_orcado =[0]
Saidas_orcado = [0]  
meses = []
posicoes =  []
def dados(pos_prv,pos_real):
    for i in range(ultima_coluna):
        celula = aba.cell(row=i+1, column=1).value
        posicoes.append(celula)
        posicoes.append(i+1)

    for i in range(ultima_linha):
        celula = aba.cell(row=1, column=i+1)    
        if celula.value == "Realizado":
            celula = aba.cell(row=pos_ent, column=i+1).value
            Entradas_Realizadas.append(int(celula))
            celula = aba.cell(row=pos_saida, column=i+1).value
            Saidas_Realizadas.append(int(celula)*-1)
            
            
    #print(Saidas_Realizadas)        
            
    for i in range(ultima_linha):
        celula = aba.cell(row=1, column=i+1)    
        if celula.value == "Orçado":
            celula = aba.cell(row=pos_ent, column=i+1).value
            Entradas_orcado.append(int(celula))
            celula = aba.cell(row=pos_saida, column=i+1).value
            Saidas_orcado.append(int(celula)*-1   )
    #print(Saidas_orcado)

descricoes = ['Entradas','Receitas','Aporte','Despesas','Opex','Capex','impostos']


for j in descricoes:
    linha = j
    for i in range(len(posicoes)):   
        if linha == posicoes[i]:
            POS = posicoes[i+1]    
            
            
print(POS)

Entradas = "Entradas"
Receitas = "Receitas"
Aporte = "Aporte"
Despesas = "Despesas"
Opex = "Opex"
Capex = "Capex"
impostos ="Impostos"        
    


   
# ...existing code...    

labels = []

for i in range(len(Entradas_Realizadas)):
    #print(i)
    if i <= 2:
        labels.append(f'{i+10}-24')
    if i > 2:
        labels.append(f'{i-2}-25')

x = range(len(labels))
largura = 0.35

plt.figure(figsize=(14,6))

# Gráfico 1: Entradas
plt.subplot(1, 2, 1)
plt.bar([i - largura/2 for i in x], Entradas_Realizadas, width=largura, label='Entradas Realizadas')
plt.bar([i + largura/2 for i in x], Entradas_orcado, width=largura, label='Entradas Orçadas')
plt.xticks(x, labels)
plt.xlabel('Meses')
plt.ylabel('Valores')
plt.title('Entradas: Realizadas x Orçadas')
plt.legend()

# Gráfico 2: Saídas
plt.subplot(1,2, 2)
plt.bar([i - largura/2 for i in x], Saidas_Realizadas, width=largura, label='Saídas Realizadas')
plt.bar([i + largura/2 for i in x], Saidas_orcado, width=largura, label='Saídas Orçadas')
plt.xticks(x, labels)
plt.xlabel('Meses')
plt.ylabel('Valores')
plt.title('Saídas: Realizadas x Orçadas')
plt.legend()


plt.tight_layout()
plt.savefig('graficos.png')  # Salva a imagem
plt.close()
webbrowser.open(f'file:///{'graficos.png'}')





            
'''
            if linha == 'Entradas':
                Entradas_Real = dados(pos)[0]
                Entradas_Orca = dados(pos)[1]                
            if linha == 'Receitas':
                Receitas_Real = dados(pos)[0]
                Receitas_Orca = dados(pos)[1]   
            if linha == 'Aporte':
                Aporte_Real = dados(pos)[0]
                Aporte_Orca = dados(pos)[1]
            if linha == 'Despesas':                
                Despesas_Real = dados(pos)[0]
                Despesas_Orca = dados(pos)[1]
            if linha == 'OPEX':
                OPEX_Real = dados(pos)[0]
                OPEX_Orca = dados(pos)[1]
            if linha == 'CAPEX':
                Capex_Real = dados(pos)[0]
                Capex_Orca = dados(pos)[1]
            if linha == 'Impostos':                
                Impostos_Real = dados(pos)[0]
                Impostos_Orca = dados(pos)[1]
                
                

            


 


def plot(Realizadas,Orcado,linha):
    labels = []

    for i in range(10):
        #print(i)
        if i <= 2:
            labels.append(f'{i+10}-24')
        if i > 2:
            labels.append(f'{i-2}-25')

    x = range(len(labels))
    largura = 0.35

    plt.figure(figsize=(14,6))

    # Gráfico 1: Entradas
    plt.subplot(4, 2, 1)
    plt.bar([i - largura/2 for i in x], Realizadas, width=largura, label=linha+ ' Realizadas')
    plt.bar([i + largura/2 for i in x], Orcado, width=largura, label= linha + ' Orçadas')
    plt.xticks(x, labels)
    plt.xlabel('Meses')
    plt.ylabel('Valores')
    plt.title('Entradas: Realizadas x Orçadas')
    plt.legend()

    # Gráfico 2: Saídas
    plt.subplot(1,2, 2)
    plt.bar([i - largura/2 for i in x], Saidas_Realizadas, width=largura, label='Saídas Realizadas')
    plt.bar([i + largura/2 for i in x], Saidas_orcado, width=largura, label='Saídas Orçadas')
    plt.xticks(x, labels)
    plt.xlabel('Meses')
    plt.ylabel('Valores')
    plt.title('Saídas: Realizadas x Orçadas')
    plt.legend()


    plt.tight_layout()
    plt.savefig('graficos.png')  # Salva a imagem
    plt.close()
    webbrowser.open(f'file:///{'graficos.png'}')

'''    