import unicodedata

def tratar_texto(txt):
    txt = txt.strip().lower()
    txt = unicodedata.normalize("NFD", txt)
    txt = "".join(c for c in txt if unicodedata.category(c) != "Mn")
    return txt

produtos = {
    "Flyer": {
        "opcoes": {
            "Formato": {
                "1": "A4 (21,0 x 29,7 cm)",
                "2": "A5 (14,8 x 21,0 cm)",
                "3": "A6 (10,5 x 14,8 cm)",
                "4": "A7 (7,4 x 10,5 cm)"
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
            "Formato (fechado)": {
                "1": "DL (10 x 20 cm)",
                "2": "A4 (21,0 x 29,7 cm)",
                "3": "A6 (10,5 x 14,8 cm)"
            },
            "Formato (aberto)": {
                "1": "6 Páginas - Vertical",
                "2": "8 Páginas - Vertical"
            },
            "Papel": {
                "1": "Couché Fosco 90g",
                "2": "Couché Brilho 115g",
                "3": "Offset 90g"
            },
            "Serrilha": {
                "1": "Sem Serrilha Vertical (6 Páginas) - Carteira",
                "2": "Serrilha Vertical - Páginas 1 e 2 (6 Páginas) - Carteira",
                "3": "Serrilha Vertical - Páginas 4 e 5 (6 Páginas) - Carteira"
            }
        }
    },
    "Adesivo Personalizado": {
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
        "Formato": {"1": 0.80, "2": 0.60, "3": 0.50, "4": 0.40},
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
        "Formato (fechado)": {"1": 0.20, "2": 0.15, "3": 0.18},
        "Formato (aberto)": {"1": 0.18, "2": 0.25},
        "Papel": {"1": 0.10, "2": 0.12, "3": 0.14},
        "Serrilha": {"1": 0.05, "2": 0.04, "3": 0.03}
    },
    "Adesivo Personalizado": {
        "Formato": {"1": 0.20, "2": 0.15, "3": 0.18},
        "Impressao": {"1": 0.18, "2": 0.25, "3": 0.30},
        "Extras": {"1": 0.10, "2": 0.12, "3": 0.14},
        "Auxiliares": {"1": 0.05, "2": 0.04, "3": 0.03}
    }
}

def forca_opcao(msg, lista_opcoes):
    lista_original = list(lista_opcoes)
    lista_norm = [tratar_texto(x) for x in lista_original]
    while True:
        entrada = tratar_texto(input(f"{msg}" + "\n" + "\n".join(lista_original) + "\n-> "))
        if entrada in lista_norm:
            return lista_original[lista_norm.index(entrada)]
        print("Opção inválida.\n")

def input_num_int(msg):
    while True:
        v = input(msg).strip()
        if v.isdigit():
            return int(v)
        print("Precisa ser número inteiro.")

def input_num_float(msg):
    while True:
        v = input(msg).replace(",", ".").strip()
        try:
            return float(v)
        except ValueError:
            print("Número inválido.")

def mostrar_produtos():
    print("\nProdutos disponíveis:")
    i = 1
    for nome in produtos:
        print(f"{i}. {nome}")
        i += 1
    print()
    return

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
            chave = input(f" - Chave da opção (ex: '1') (Enter para terminar '{cat}'): ").strip()
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
    nome = forca_opcao("Digite o nome do produto a remover: ", list(produtos.keys()))
    confirmar = forca_opcao(f"Tem certeza que quer remover '{nome}'? ", ['sim', 'nao'])
    if confirmar == 'sim':
        produtos.pop(nome, None)
        precos.pop(nome, None)
        print(f"Produto '{nome}' removido.")
    else:
        print("Operação cancelada.")
    return

def atualizar_produto():
    nome = forca_opcao("Nome do produto a atualizar: ", list(produtos.keys()))

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

def listar_tudo():
    print("\n---------------- PRODUTOS ----------------")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for prod, dados in produtos.items():
        print(f"\n>>> {prod}")
        for categoria, itens in dados["opcoes"].items():
            print(f"  - {categoria}")
            for chave, descricao in itens.items():
                preco = precos.get(prod, {}).get(categoria, {}).get(chave, "---")
                preco = f"R$ {preco:.2f}" if preco != "---" else "---"
                print(f"      {chave} -> {descricao} | {preco}")
    print("-------------------------------------------\n")

def escolher_produto_cliente():
    mostrar_produtos()
    entrada = tratar_texto(input("Digite o nome (ou sair): "))
    if entrada == "sair":
        return None
    for k in produtos.keys():
        if tratar_texto(k) == entrada:
            return k
    print("Produto não encontrado.\n")
    return escolher_produto_cliente()

def simular_orcamento(produto_nome):
    produto = produtos[produto_nome]
    preco_ref = precos.get(produto_nome, {})
    escolhas = {}
    custo_unitario = 0.0

    print(f"\n--- {produto_nome} ---")
    for categoria, opcs in produto["opcoes"].items():
        print(f"\n{categoria}:")
        for chave, desc in opcs.items():
            preco = preco_ref.get(categoria, {}).get(chave, 0)
            print(f"  {chave} - {desc} | R$ {preco:.2f}")
        while True:
            inp = tratar_texto(input(f"Escolha ({categoria}): "))
            mapa = {tratar_texto(k): k for k in opcs.keys()}
            if inp in mapa:
                escolha_real = mapa[inp]
                break
            print("Opção inválida.")
        escolhas[categoria] = escolha_real
        custo_unitario += preco_ref.get(categoria, {}).get(escolha_real, 0)

    custos_extras = {}
    print()
    add_extra = forca_opcao("Adicionar custos extras?", ["sim", "nao"])
    if add_extra == "sim":
        while True:
            nome = input("Nome do custo extra (Enter para terminar): ").strip()
            if nome == "":
                break
            valor = input_num_float("Valor por unidade: R$ ")
            custos_extras[nome] = valor
            custo_unitario += valor

    quantidade = input_num_int("Quantidade: ")
    markup = input_num_float("Markup (%): ")

    custo_total = custo_unitario * quantidade
    preco_unitario = custo_unitario * (1 + markup/100)
    preco_total = preco_unitario * quantidade
    lucro_total = preco_total - custo_total

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
    print()

while True:
    print()
    print("BEM VINDO AO SISTEMA DE GESTÃO GRÁFICA (CLI)\n")
    usuario = forca_opcao("Você é:", ["cliente", "funcionario", "sair"])
    if usuario == "sair":
        print("Encerrando...")
        break
    if usuario == "funcionario":
        while True:
            print()
            acao = forca_opcao("Operação:", ["cadastrar", "remover", "atualizar", "listar", "voltar"])
            if acao == "voltar":
                break
            if acao == "cadastrar":
                cadastrar_produto()
            if acao == "remover":
                remover_produto()
            if acao == "atualizar":
                atualizar_produto()
            if acao == "listar":
                listar_tudo()
    if usuario == "cliente":
        while True:
            esc = escolher_produto_cliente()
            if esc is None:
                break
            simular_orcamento(esc)
            prox = forca_opcao("Continuar, voltar ou sair?", ["continuar", "voltar", "sair"])
            if prox != "continuar":
                break