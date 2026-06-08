mochila = 0
contador = 0

while contador < 5:
    itens = input('adicione intens na mochila (ou sair):')
    
    if itens =="sair":
        break 
mochila += (itens)
print (mochila)
