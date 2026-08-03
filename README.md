# 📊 Bot de Automação de Lançamentos Contábeis

Bot desenvolvido em Python para importar transações financeiras de uma planilha Excel e cadastrá-las automaticamente em um sistema contábil.

## 📋 Sobre o projeto

Este projeto utiliza o Playwright para controlar um navegador Chromium, acessar um sistema contábil, realizar o login e cadastrar automaticamente transações financeiras.

Os dados dos lançamentos são obtidos de uma planilha Excel por meio da biblioteca OpenPyXL. Cada linha da planilha representa uma transação que deverá ser cadastrada no sistema.

A automação lê informações como descrição, valor, data, tipo, categoria e status. Em seguida, preenche os campos correspondentes no sistema e salva cada lançamento automaticamente.

## 🎯 Objetivo

Automatizar o cadastro de transações financeiras e evitar que o usuário precise inserir manualmente cada lançamento no sistema contábil.

O projeto busca reduzir o tempo gasto em tarefas repetitivas, diminuir erros de digitação, padronizar o preenchimento das informações e aumentar a produtividade durante o processamento de múltiplos lançamentos.

## ✨ Funcionalidades

- Abertura automática do navegador Chromium;
- Acesso automático ao sistema contábil;
- Preenchimento automático de e-mail e senha;
- Login automático no sistema;
- Acesso ao módulo de lançamentos;
- Leitura de transações em uma planilha Excel;
- Processamento de múltiplos lançamentos;
- Cadastro automático de receitas e despesas;
- Preenchimento automático da descrição;
- Preenchimento automático do valor;
- Preenchimento automático da data;
- Seleção automática do tipo da transação;
- Seleção automática da categoria;
- Seleção automática do status;
- Salvamento automático de cada lançamento;
- Uso de intervalos variáveis durante a digitação;
- Encerramento controlado após a conclusão.

## 🛠️ Tecnologias utilizadas

- Python
- Playwright
- OpenPyXL
- Regex
- Chromium

## 📊 Formato da planilha

A planilha deve possuir o nome:

```text
lancamentos.xlsx
```

Também deve conter uma aba chamada:

```text
Lançamentos
```

As colunas precisam estar organizadas na seguinte ordem:

| Descrição | Valor | Data | Tipo | Categoria | Status |
|---|---:|---|---|---|---|
| Conta de energia | 250.50 | 10/08/2026 | Despesa | Utilidades | Pendente |
| Venda de produto | 1500.00 | 11/08/2026 | Receita | Vendas | Pago |
| Serviço de internet | 120.90 | 12/08/2026 | Despesa | Utilidades | Atrasado |

A primeira linha da planilha deve conter os nomes das colunas.

A leitura das transações começa a partir da segunda linha.

## 📁 Estrutura do projeto

```text
bot-sistema-de-contabilidade/
├── BotSistemaContabilidade.py
├── lancamentos.xlsx
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

### Arquivos do projeto

- `BotSistemaContabilidade.py`: arquivo principal da automação;
- `lancamentos.xlsx`: planilha contendo as transações financeiras;
- `README.md`: documentação do projeto;
- `requirements.txt`: dependências necessárias para executar o programa;
- `.gitignore`: arquivos e pastas que não devem ser enviados ao GitHub;
- `LICENSE`: termos de uso e proteção autoral do projeto.

## ⚙️ Pré-requisitos

Antes de executar o projeto, tenha instalado:

- Python;
- Git;
- Visual Studio Code ou outro editor de código;
- As bibliotecas presentes no arquivo `requirements.txt`;
- O navegador Chromium utilizado pelo Playwright;
- Uma planilha chamada `lancamentos.xlsx`;
- Acesso à internet.

## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/bot-sistema-de-contabilidade.git
```

Entre na pasta:

```bash
cd bot-sistema-de-contabilidade
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Instale o navegador Chromium do Playwright:

```bash
python -m playwright install chromium
```

## ▶️ Como executar

Confirme que os arquivos abaixo estão na mesma pasta:

```text
BotSistemaContabilidade.py
lancamentos.xlsx
```

Execute a automação:

```bash
python BotSistemaContabilidade.py
```

O navegador será aberto e a automação começará a processar os lançamentos existentes na planilha.

Após concluir todos os cadastros, o programa exibirá a seguinte mensagem:

```text
Digite ENTER para encerrar a automação:
```

Pressione Enter para fechar o navegador e finalizar o programa.

## 🔄 Fluxo da automação

1. O Playwright inicia o navegador Chromium.
2. O programa acessa a página do sistema contábil.
3. Os campos de e-mail e senha são preenchidos.
4. A automação realiza o login.
5. O módulo de lançamentos é aberto.
6. O arquivo `lancamentos.xlsx` é carregado.
7. A aba `Lançamentos` é selecionada.
8. O programa começa a leitura a partir da segunda linha.
9. Os dados da transação são armazenados em variáveis.
10. O formulário de novo lançamento é aberto.
11. A descrição, o valor e a data são preenchidos.
12. O tipo da transação é selecionado.
13. A categoria e o status são selecionados.
14. O lançamento é salvo.
15. O processo é repetido para todas as linhas da planilha.
16. Ao final, o programa aguarda o usuário pressionar Enter.
17. O navegador é fechado.

## ⚠️ Limitações atuais

- O programa precisa permanecer aberto durante a execução;
- A planilha precisa estar na mesma pasta do código;
- O arquivo precisa se chamar `lancamentos.xlsx`;
- A aba da planilha precisa se chamar exatamente `Lançamentos`;
- As colunas precisam estar na ordem esperada pelo programa;
- O formato da data precisa ser aceito pelo sistema;
- As categorias precisam corresponder às opções disponíveis no site;
- Os status precisam corresponder às opções disponíveis no site;
- Qualquer tipo diferente de `Despesa` será tratado como `Receita`;
- Alterações na estrutura HTML podem exigir atualização dos localizadores;
- Alterações nos atributos `data-testid` podem interromper a automação;
- O projeto ainda não registra quais lançamentos foram concluídos;
- O projeto ainda não gera relatório de erros;
- O projeto não verifica lançamentos duplicados;
- Não existe interface gráfica nesta versão.

## 👨‍💻 Autor

Desenvolvido por **FabioDevPTch** como projeto de estudo em Python, automação web, Playwright, manipulação de planilhas e automatização de processos administrativos.

## 📄 Licença

Copyright © 2026 FabioDevPTch. Todos os direitos reservados.

Este projeto possui uma licença proprietária e está disponível publicamente apenas para fins de estudo, demonstração técnica e apresentação de portfólio.

Não é permitida a reprodução, modificação, distribuição, comercialização, sublicenciamento ou utilização total ou parcial deste projeto sem autorização prévia e expressa do autor.

A disponibilização pública deste repositório não concede automaticamente permissão para copiar, modificar, distribuir ou utilizar comercialmente o código.

Consulte o arquivo [`LICENSE`](LICENSE) para conhecer os termos completos.
