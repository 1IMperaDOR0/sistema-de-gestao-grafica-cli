produtos = {
    "Flyer": {
        "opcoes": {
            "Formato": {
                "A4": "21,0 x 29,7 cm",
                "A5": "14,8 x 21,0 cm",
                "A6": "10,5 x 14,8 cm",
                "A7": "7,4 x 10,5 cm"
            },
            "Impressao": {
                "1": "Frente e Verso",
                "2": "Frente"
            },
            "Papel": {
                "1": "Couché Brilho 90g",
                "2": "Couché Brilho 115g",
                "3": "Couché Fosco 150g"
            }
        }
    },
    "Pasta Personalizada": {
        "opcoes": {
            "Formato": {
                "1": "22,0 x 31,0 cm (Com Bolsa)",
                "2": "21,5 x 30,3 cm (Com Orelha)"
            },
            "Impressao": {
                "1": "Externa",
                "2": "Externa e Interna"
            },
            "Papel": {
                "1": "Cartão 300g",
                "2": "Kraft 240g"
            },
            "Serrilha": {
                "1": "Sem Serrilha Vertical (6 Páginas) - Carteira",
                "2": "Serrilha Vertical - Páginas 1 e 2 (6 Páginas) - Carteira",
                "3": "Serrilha Vertical - Páginas 4 e 5 (6 Páginas) - Carteira"
            }
        }
    },
    "Folder 2 Dobras": {
        "opcoes": {
            "Formato": {
                "1": "5 x 5 cm",
                "2": "3 x 3 cm",
                "3": "4 x 4 cm"
            },
            "Impressao": {
                "1": "4x0 (Colorido, Sem Branco)",
                "2": "5x0 (Com Branco Local)",
                "3": "5x0 (Com Branco Total)"
            },
            "Extras": {
                "1": "Couché Adesivo",
                "2": "Offset Adesivo",
                "3": "BOPP Branco Brilho"
            },
            "Auxiliares": {
                "1": "Especial",
                "2": "Redondo",
                "3": "Quadrado"
            }
        }
    }
}

precos = {
    "Flyer": {
        "Formato": {"A4": 0.80, "A5": 0.60, "A6": 0.50, "A7": 0.40},
        "Impressao": {"1": 0.30, "2": 0.20},
        "Papel": {"1": 0.10, "2": 0.12, "3": 0.15}
    },
    "Pasta Personalizada": {
        "Formato": {"1": 1.50, "2": 1.80},
        "Impressao": {"1": 0.50, "2": 0.80},
        "Papel": {"1": 0.60, "2": 0.55},
        "Serrilha": {"1": 0.00, "2": 0.08, "3": 0.08}
    },
    "Folder 2 Dobras": {
        "Formato": {"1": 0.20, "2": 0.15, "3": 0.18},
        "Impressao": {"1": 0.18, "2": 0.25, "3": 0.30},
        "Extras": {"1": 0.10, "2": 0.12, "3": 0.14},
        "Auxiliares": {"1": 0.05, "2": 0.04, "3": 0.03}
    }
}

def forca_opcao(msg, lista_opcoes):
    lista_opcoes = list(lista_opcoes)
    opcoes_text = '\n'.join(lista_opcoes)
    opcao = input(f"{msg}\n{opcoes_text}\n-> ").strip()
    while opcao not in lista_opcoes:
        print("Inválido! Digite exatamente uma das opções acima.")
        opcao = input(f"{msg}\n{opcoes_text}\n-> ").strip()
    return opcao

def input_num_int(msg):
    while True:
        v = input(msg).strip()
        if v.isdigit():
            return int(v)
        print("Precisa ser um número inteiro (ex: 10).")

def input_num_float(msg):
    while True:
        v = input(msg).strip().replace(',', '.')
        try:
            return float(v)
        except ValueError:
            print("Precisa ser um número (ex: 10.5). Use , ou . para separar decimais.")

def mostrar_produtos():
    print("\nProdutos disponíveis:")
    for i, nome in enumerate(produtos, start=1):
        print(f"{i}. {nome}")
    print()

def cadastrar_produto():
    print("\n--- CADASTRAR PRODUTO ---")
    nome = input("Nome do produto: ").strip()
    if not nome:
        print("Nome inválido.")
        return
    if nome in produtos:
        print("Produto já existe.")
        return

    produtos[nome] = {"opcoes": {}}
    precos[nome] = {}

    categorias_padrao = ["Formato", "Impressao", "Papel", "Extras", "Auxiliares", "Serrilha"]
    print("Categorias padrão disponíveis (você pode escolher quais adicionar):")
    print(", ".join(categorias_padrao))
    adicionar = input("Quais categorias adicionar? (separe por vírgula ou digite 'todas'): ").strip()
    if adicionar.lower() == 'todas':
        categorias = categorias_padrao
    else:
        categorias = [c.strip() for c in adicionar.split(',') if c.strip()]

    if not categorias:
        print("Nenhuma categoria selecionada. Produto criado sem opções.")
        return

    for cat in categorias:
        produtos[nome]["opcoes"][cat] = {}
        precos[nome][cat] = {}
        print(f"\nAdicionando opções para a categoria '{cat}'.")
        print("Digite as opções uma a uma. Para encerrar esta categoria, deixe o nome vazio e tecle Enter.")
        while True:
            chave = input(f" - Chave da opção (ex: 'A4' ou '1') (Enter para terminar '{cat}'): ").strip()
            if chave == "":
                break
            descricao = input("   Descrição (texto mostrável pro cliente): ").strip()
            preco = input_num_float("   Preço desta opção por unidade (ex: 0.50): R$ ")
            produtos[nome]["opcoes"][cat][chave] = descricao if descricao else chave
            precos[nome][cat][chave] = float(preco)
        if not produtos[nome]["opcoes"][cat]:
            produtos[nome]["opcoes"].pop(cat, None)
            precos[nome].pop(cat, None)
    print(f"Produto '{nome}' cadastrado com sucesso.")

def remover_produto():
    mostrar_produtos()
    nome = input("Digite o nome do produto a remover: ").strip()
    if nome not in produtos:
        print("Produto não encontrado.")
        return
    confirmar = forca_opcao(f"Tem certeza que quer remover '{nome}'? ", ['sim', 'nao'])
    if confirmar == 'sim':
        produtos.pop(nome, None)
        precos.pop(nome, None)
        print(f"Produto '{nome}' removido.")
    else:
        print("Operação cancelada.")

def atualizar_produto():
    mostrar_produtos()
    nome = input("Nome do produto a atualizar: ").strip()
    if nome not in produtos:
        print("Produto não encontrado.")
        return

    while True:
        print(f"\nAtualizando '{nome}' - escolha a ação:")
        acoes = ['renomear', 'adicionar_categoria', 'remover_categoria', 'gerir_opcoes', 'sair']
        acao = forca_opcao("Ação:", acoes)
        if acao == 'renomear':
            novo = input("Novo nome do produto: ").strip()
            if not novo:
                print("Nome inválido.")
            elif novo in produtos:
                print("Já existe um produto com esse nome.")
            else:
                produtos[novo] = produtos.pop(nome)
                precos[novo] = precos.pop(nome)
                nome = novo
                print("Renomeado com sucesso.")
        elif acao == 'adicionar_categoria':
            cat = input("Nome da nova categoria (ex: 'Acabamento'): ").strip()
            if not cat:
                print("Categoria inválida.")
            elif cat in produtos[nome]['opcoes']:
                print("Categoria já existe.")
            else:
                produtos[nome]['opcoes'][cat] = {}
                precos[nome][cat] = {}
                print(f"Categoria '{cat}' adicionada.")
        elif acao == 'remover_categoria':
            cats = list(produtos[nome]['opcoes'].keys())
            if not cats:
                print("Não há categorias para remover.")
            else:
                cat = forca_opcao("Qual categoria remover?", cats)
                produtos[nome]['opcoes'].pop(cat, None)
                precos[nome].pop(cat, None)
                print(f"Categoria '{cat}' removida.")
        elif acao == 'gerir_opcoes':
            cats = list(produtos[nome]['opcoes'].keys())
            if not cats:
                print("Produto não tem categorias. Adicione primeiro.")
                continue
            cat = forca_opcao("Escolha categoria para gerir opções:", cats)
            while True:
                sub = forca_opcao("Ação na categoria:", ['adicionar', 'atualizar', 'remover', 'sair'])
                if sub == 'adicionar':
                    chave = input("Chave da opção: ").strip()
                    if not chave:
                        print("Chave inválida.")
                        continue
                    descricao = input("Descrição a mostrar pro cliente: ").strip() or chave
                    preco = input_num_float("Preço por unidade: R$ ")
                    produtos[nome]['opcoes'][cat][chave] = descricao
                    precos[nome].setdefault(cat, {})[chave] = float(preco)
                    print("Opção adicionada.")
                elif sub == 'atualizar':
                    chaves = list(produtos[nome]['opcoes'][cat].keys())
                    if not chaves:
                        print("Não há opções nessa categoria.")
                        continue
                    chave = forca_opcao("Escolha a chave a atualizar:", chaves)
                    print("1. Atualizar descrição\n2. Atualizar preço\n3. Atualizar ambas")
                    opt = forca_opcao("Opção:", ['1','2','3'])
                    if opt in ('1','3'):
                        nova_desc = input("Nova descrição: ").strip()
                        if nova_desc:
                            produtos[nome]['opcoes'][cat][chave] = nova_desc
                    if opt in ('2','3'):
                        novo_preco = input_num_float("Novo preço por unidade: R$ ")
                        precos[nome].setdefault(cat, {})[chave] = float(novo_preco)
                    print("Atualização realizada.")
                elif sub == 'remover':
                    chaves = list(produtos[nome]['opcoes'][cat].keys())
                    if not chaves:
                        print("Não há opções nessa categoria.")
                        continue
                    chave = forca_opcao("Escolha a chave a remover:", chaves)
                    produtos[nome]['opcoes'][cat].pop(chave, None)
                    precos[nome].get(cat, {}).pop(chave, None)
                    print("Opção removida.")
                else:  
                    break
        else:  
            break

def listar_detalhes():
    mostrar_produtos()
    nome = input("Digite o nome do produto para ver detalhes (ou 'sair'): ").strip()
    if nome.lower() == 'sair':
        return
    if nome not in produtos:
        print("Produto não encontrado.")
        return
    print("\n--- DETALHES DO PRODUTO ---")
    print(f"Produto: {nome}")
    for cat, opcs in produtos[nome]['opcoes'].items():
        print(f"\nCategoria: {cat}")
        for k, v in opcs.items():
            preco = precos.get(nome, {}).get(cat, {}).get(k, '---')
            print(f"  {k} - {v}  |  R$ {preco if preco == '---' else f'{preco:.2f}'}")
    print("---------------------------")

def escolher_produto_cliente():
    mostrar_produtos()
    nome = input("Digite o nome do produto que deseja (ou 'sair'): ").strip()
    if nome.lower() == 'sair':
        return None
    if nome not in produtos:
        print("Produto não encontrado.")
        return None
    return nome

def simular_orcamento(produto_nome):
    produto = produtos[produto_nome]
    preco_ref = precos.get(produto_nome, {})
    escolhas = {}
    custo_unitario = 0.0

    print(f"\nVocê escolheu: {produto_nome}")
    print("Selecione as opções abaixo:\n")

    for categoria, opcoes in produto['opcoes'].items():
        print(f"{categoria}:")
        for chave, descricao in opcoes.items():
            preco_str = ""
            preco_val = preco_ref.get(categoria, {}).get(chave)
            if preco_val is not None:
                preco_str = f"R$ {preco_val:.2f}"
            print(f"  {chave} - {descricao} {(' | ' + preco_str) if preco_str else ''}")
        escolha = input(f"Escolha {categoria} (digite a chave): ").strip()
        while escolha not in opcoes:
            print("Opção inválida.")
            escolha = input(f"Escolha {categoria} (digite a chave): ").strip()
        escolhas[categoria] = escolha
        preco_escolha = preco_ref.get(categoria, {}).get(escolha)
        if preco_escolha is None:
            print(f"Atenção: não há preço cadastrado para {categoria} -> {escolha}. Será usado R$ 0.00.")
            preco_escolha = 0.0
        custo_unitario += float(preco_escolha)

    adicionar_custos = forca_opcao("Quer adicionar custo unitário extra (ex: embalagem)?", ['sim', 'nao'])
    custos_extras = {}
    if adicionar_custos == 'sim':
        while True:
            nome_custo = input("Nome do custo extra (ou Enter para terminar): ").strip()
            if nome_custo == "":
                break
            valor = input_num_float("Valor por unidade (R$): ")
            custos_extras[nome_custo] = float(valor)
            custo_unitario += float(valor)

    quantidade = input_num_int("\nQuantidade desejada: ")
    markup = input_num_float("Porcentagem de lucro desejada (%): ")

    custo_total = custo_unitario * quantidade
    preco_unitario = custo_unitario * (1 + markup / 100)
    preco_total = preco_unitario * quantidade
    lucro_unit = preco_unitario - custo_unitario
    lucro_total = lucro_unit * quantidade

    print("\n----- ORÇAMENTO -----")
    print(f"Produto: {produto_nome}")
    for cat, chave in escolhas.items():
        descricao = produto['opcoes'][cat][chave]
        preco_item = preco_ref.get(cat, {}).get(chave, 0.0)
        print(f"{cat}: {descricao} (chave: {chave}) - R$ {preco_item:.2f}")
    if custos_extras:
        print("\nCustos extras por unidade:")
        for k, v in custos_extras.items():
            print(f"  {k}: R$ {v:.2f}")
    print(f"\nCusto por unidade: R$ {custo_unitario:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Custo total: R$ {custo_total:.2f}")
    print(f"Markup aplicado: {markup:.2f}%")
    print(f"Preço por unidade (com markup): R$ {preco_unitario:.2f}")
    print(f"Preço total (com markup): R$ {preco_total:.2f}")
    print(f"Lucro total estimado: R$ {lucro_total:.2f}")
    print("----------------------")

def main():
    print("BEM VINDO AO SISTEMA DE GESTÃO GRÁFICA (CLI)\n")
    usuario = forca_opcao("Você é:", ['cliente', 'funcionário'])
    if usuario == 'funcionário':
        while True:
            operacao = forca_opcao("Qual operação será realizada?", ['cadastrar', 'remover', 'atualizar', 'listar', 'sair'])
            if operacao == 'cadastrar':
                cadastrar_produto()
            elif operacao == 'remover':
                remover_produto()
            elif operacao == 'atualizar':
                atualizar_produto()
            elif operacao == 'listar':
                listar_detalhes()
            elif operacao == 'sair':
                print("Saindo do modo funcionário.")
                break
            cont = forca_opcao("Deseja realizar outra operação?", ['sim', 'nao'])
            if cont == 'nao':
                break
    else:
        while True:
            escolha = escolher_produto_cliente()
            if escolha is None:
                break
            simular_orcamento(escolha)
            cont = forca_opcao("Fazer outro orçamento ou sair?", ['continuar', 'sair'])
            if cont == 'sair':
                print("Obrigado. Até mais.")
                break

main()