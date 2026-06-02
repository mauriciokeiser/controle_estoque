# Controle de Estoque - Loja
# Agora com funcionalidades bônus

nomes = []
quantidades = []
precos = []
minimos = []

def localizar_produto(chave):
    chave = chave.lower()
    for i in range(len(nomes)):
        if nomes[i].lower() == chave or str(i) == chave:
            return i
    return -1

while True:
    print("\n--- MENU ---")
    print("1. Cadastrar produto")
    print("2. Registrar entrada")
    print("3. Registrar saída/venda")
    print("4. Listar produtos")
    print("5. Relatório de valorização")
    print("6. Produtos em alerta")
    print("7. Editar produto")
    print("8. Reposição automática (Bônus)")
    print("9. Simulador de promoção (Bônus)")
    print("0. Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        qtde = int(input("Quantidade inicial: "))
        preco = float(input("Preço unitário: "))
        minimo = int(input("Quantidade mínima: "))
        nomes.append(nome)
        quantidades.append(qtde)
        precos.append(preco)
        minimos.append(minimo)

    elif opcao == "2":
        chave = input("Informe índice ou nome: ")
        idx = localizar_produto(chave)
        if idx != -1:
            add = int(input("Quantidade a adicionar: "))
            if add > 0:
                quantidades[idx] += add
            else:
                print("Quantidade inválida.")
        else:
            print("Produto não encontrado.")

    elif opcao == "3":
        chave = input("Informe índice ou nome: ")
        idx = localizar_produto(chave)
        if idx != -1:
            saida = int(input("Quantidade a vender: "))
            if saida > 0 and saida <= quantidades[idx]:
                quantidades[idx] -= saida
                if quantidades[idx] <= minimos[idx]:
                    print(f"ALERTA: {nomes[idx]} em baixa quantidade!")
            else:
                print("Operação inválida.")
        else:
            print("Produto não encontrado.")

    elif opcao == "4":
        for i in range(len(nomes)):
            valor_total = quantidades[i] * precos[i]
            status = "OK" if quantidades[i] > minimos[i] else "BAIXO"
            print(f"{i} - {nomes[i]} | Qtde: {quantidades[i]} | Preço: {precos[i]:.2f} | Total: {valor_total:.2f} | {status}")

    elif opcao == "5":
        n = len(nomes)
        valores = [quantidades[i] * precos[i] for i in range(n)]
        for j in range(n-1):
            for k in range(n-1-j):
                if valores[k] < valores[k+1]:
                    valores[k], valores[k+1] = valores[k+1], valores[k]
                    nomes[k], nomes[k+1] = nomes[k+1], nomes[k]
                    quantidades[k], quantidades[k+1] = quantidades[k+1], quantidades[k]
                    precos[k], precos[k+1] = precos[k+1], precos[k]
                    minimos[k], minimos[k+1] = minimos[k+1], minimos[k]
        total_loja = sum(valores)
        print(f"Valor total do estoque: {total_loja:.2f}")
        for i in range(len(nomes)):
            print(f"{nomes[i]} - {quantidades[i]} un - R${valores[i]:.2f}")

    elif opcao == "6":
        for i in range(len(nomes)):
            if quantidades[i] <= minimos[i]:
                print(f"{i} - {nomes[i]} | Qtde: {quantidades[i]} | Mínimo: {minimos[i]}")

    elif opcao == "7":
        chave = input("Informe índice ou nome: ")
        idx = localizar_produto(chave)
        if idx != -1:
            print("1. Alterar nome\n2. Alterar preço\n3. Alterar mínimo")
            escolha = input("Opção: ")
            if escolha == "1":
                nomes[idx] = input("Novo nome: ")
            elif escolha == "2":
                precos[idx] = float(input("Novo preço: "))
            elif escolha == "3":
                minimos[idx] = int(input("Novo mínimo: "))
        else:
            print("Produto não encontrado.")

    elif opcao == "8":  # Reposição automática
        investimento_total = 0
        for i in range(len(nomes)):
            if quantidades[i] <= minimos[i]:
                alvo = minimos[i] * 2
                comprar = alvo - quantidades[i]
                custo = comprar * precos[i]
                investimento_total += custo
                print(f"{nomes[i]}: comprar {comprar} unidades (R${custo:.2f})")
        print(f"Investimento total sugerido: R${investimento_total:.2f}")

    elif opcao == "9":  # Simulador de promoção
        desconto = float(input("Informe % de desconto: "))
        fator = (100 - desconto) / 100
        valor_original = sum([quantidades[i] * precos[i] for i in range(len(nomes))])
        novos_precos = [precos[i] * fator for i in range(len(nomes))]
        valor_com_desconto = sum([quantidades[i] * novos_precos[i] for i in range(len(nomes))])
        print(f"Valor original: R${valor_original:.2f}")
        print(f"Valor com desconto: R${valor_com_desconto:.2f}")
        print("Novos preços aplicados temporariamente:")
        for i in range(len(nomes)):
            print(f"{nomes[i]} - Preço promocional: R${novos_precos[i]:.2f}")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
