# Crie um algoritmo que leia três vezes um texto no terminal e com um único print retorne: 
# O tamanho do texto;
# A junção do primeiro texto com o terceiro texto gerando um novo texto (quarto texto);
# Uma validação se existe o primeiro texto no quarto texto;
# Uma validação se existe o segundo texto no quarto texto;
# Primeiro caractere do quarto texto;
# Terceiro caractere do texto três;

texto = input('Digite um texto: ')
texto_2 = input('Digite o segundo texto: ')
texto_3 = input('Digite o terceiro texto: ')

texto_4 = texto + texto_3

print(f"""O tamanho do texto é 
{len(texto), len(texto_2), len(texto_3)}, \n a 
junção do primeiro texto com o terceiro é {texto_4} 
\n {texto in texto_4 } \n {texto_2 in texto_4} 
\n {texto_4[0]} \n {texto_3[2]}""")
