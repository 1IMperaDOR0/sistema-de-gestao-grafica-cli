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

Digite o nome do produto: Flyer

Formato:
  A4 - 21,0 x 29,7 cm
  A5 - 14,8 x 21,0 cm
Escolha Formato: A5

Impressão:
  1 - Frente e Verso
  2 - Frente
Escolha Impressão: 1

Papel:
  1 - Couché Brilho 90g
  2 - Couché Brilho 115g
  3 - Couché Fosco 150g
Escolha Papel: 2

Quantidade desejada: 100
Porcentagem de lucro (%): 25
```

Saída:

```
----- ORÇAMENTO -----
Produto: Flyer
Formato: 14,8 x 21,0 cm
Impressão: Frente e Verso
Papel: Couché Brilho 115g

Custo por unidade: R$ 0.92
Custo total: R$ 92.00
Lucro aplicado: 25%
Preço final (com lucro): R$ 115.00
----------------------
```

---

## 👥 Integrantes A-Z

* Gabriel Alexandre Fukushima Sakura
* Lucas Henrique Viana Estevam Sena

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Consulte [MIT License](https://mit-license.org/) para o texto completo.