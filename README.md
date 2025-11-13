# Sistema de Gestão Gráfica CLI

## 🧠 1. Descrição

Simulador **CLI em Python** que permite **gerenciar produtos gráficos** (Flyers, Pastas Personalizadas e Folders), cadastrar novas opções e calcular **orçamentos com base em materiais, impressão e lucro definido pelo usuário**.
O objetivo é **representar a lógica de cálculo de custos e precificação de produtos gráficos**, simulando o funcionamento básico de um sistema de gestão de pedidos.

---

## 🛠️ 2. Tecnologias

* Linguagem: **Python**
* Dependências: **nenhuma** (somente recursos nativos)
* Interface: **terminal/CLI**
* Estrutura de dados: **dicionários e listas**

---

## 🎯 3. Funcionalidades principais

### 🔹 Cadastro e consulta

* Exibe produtos disponíveis: Flyer, Pasta Personalizada e Folder 2 Dobras
* Permite adicionar **novos produtos** com categorias e opções personalizadas
* Cada produto contém:

  * Formato
  * Tipo de Impressão
  * Tipo de Papel (ou extras auxiliares, conforme o produto)

### 💰 Orçamento e precificação

* Solicita ao usuário:

  * Escolha do produto
  * Escolha das opções (formato, impressão, papel etc.)
  * Quantidade
  * Porcentagem de lucro desejada
* Calcula automaticamente:

  * Custo unitário
  * Custo total
  * Preço final com lucro
* Exibe um **relatório de orçamento detalhado** no terminal.

---

## ⚙️ 4. Estrutura do código

### Dicionários principais

* `produtos` — contém os produtos e suas opções (formato, impressão, papel etc.)
* `precos` — associa valores de custo a cada uma das opções disponíveis

### Funções principais

* `adicionar_produto()` — permite criar um novo produto dinamicamente no dicionário
* `listar_produtos()` — exibe todos os produtos disponíveis
* `gerar_orcamento()` — coleta as escolhas do usuário, soma os preços e calcula o lucro
* `menu()` — interface principal, com opções de ação

---

## ▶️ 5. Como executar

1. Salve o arquivo como `main.py`
2. No terminal, execute:

```bash
python main.py
```

3. Siga o menu exibido:
```
Você é:
cliente
funcionário
-> cliente ou funcionario
```

Nenhuma biblioteca externa é necessária.

---

## 📈 6. Exemplo de uso

```
Produtos disponíveis:
1. Flyer
2. Pasta Personalizada
3. Folder 2 Dobras

Digite o nome (ou sair): flyer

--- Flyer ---

Formato:
  A4 - 21,0 x 29,7 cm | R$ 0.80
  A5 - 14,8 x 21,0 cm | R$ 0.60
  A6 - 10,5 x 14,8 cm | R$ 0.50
  A7 - 7,4 x 10,5 cm | R$ 0.40
Escolha (Formato): a4

Impressao:
  1 - Frente e Verso | R$ 0.30
  2 - Frente | R$ 0.20
Escolha (Impressao): 1

Papel:
  1 - Couché Brilho 90g | R$ 0.10
  2 - Couché Brilho 115g | R$ 0.12
  3 - Couché Fosco 150g | R$ 0.15
Escolha (Papel): 2
Adicionar custos extras?
sim
nao
-> nao
Quantidade: 12
Markup (%): 25
```

Saída:

```
----- ORÇAMENTO -----
Produto: Flyer
Formato: 21,0 x 29,7 cm (chave: A4) - R$ 0.80
Impressao: Frente e Verso (chave: 1) - R$ 0.30
Papel: Couché Brilho 115g (chave: 2) - R$ 0.12

Custo por unidade: R$ 1.22
Quantidade: 12
Custo total: R$ 14.64
Markup aplicado: 25.00%
Preço por unidade (com markup): R$ 1.53
Preço total (com markup): R$ 18.30
Lucro total estimado: R$ 3.66
----------------------
```

---

## 👥 Integrantes A-Z

* Gabriel Alexandre Fukushima Sakura
* Lucas Henrique Viana Estevam Sena

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Consulte [MIT License](https://mit-license.org/) para o texto completo.