# 📊 Bot de Automação de Lançamentos Contábeis

Automação desenvolvida em Python para importar transações financeiras de uma planilha Excel e cadastrá-las automaticamente em um sistema contábil.

## 🎯 Objetivo

O projeto tem como objetivo reduzir o trabalho manual necessário para cadastrar lançamentos financeiros em sistemas de contabilidade.

A automação lê uma planilha contendo descrição, valor, data, tipo, categoria e status de cada transação. Em seguida, utiliza o Playwright para acessar o sistema, realizar o login e cadastrar automaticamente cada lançamento.

## ✨ Funcionalidades

- Login automático no sistema contábil;
- Leitura de lançamentos em uma planilha Excel;
- Cadastro automático de receitas e despesas;
- Preenchimento de descrição, valor e data;
- Seleção automática de tipo, categoria e status;
- Processamento de múltiplas transações;
- Uso de intervalos variáveis durante a digitação;
- Encerramento controlado após a conclusão.

## 🛠️ Tecnologias

- Python
- Playwright
- OpenPyXL
- Regex

## 📊 Formato da planilha

A planilha deve possuir uma aba chamada `Lançamentos` e as colunas:

| Descrição | Valor | Data | Tipo | Categoria | Status |
|---|---:|---|---|---|---|

## ▶️ Execução

```bash
python -m pip install -r requirements.txt
python -m playwright install chromium
python BotSistemaContabilidade.py
