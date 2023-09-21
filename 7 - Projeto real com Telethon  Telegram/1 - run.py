import TelegramBot1
obj_telegram = TelegramBot1.TelegramBot1()
grupo_alvo = obj_telegram.get_groups()
membros = obj_telegram.get_numbers_of_group(grupo_alvo)

print("%s membros encontrados no grupo" % len(membros))
print("Escolha o grupo que voce quer adicionar os novos membros")

meu_grupo = obj_telegram.get_groups()

for membro  in membros:
    adicionado = obj_telegram.add_menber_of_group(membro,meu_grupo )
