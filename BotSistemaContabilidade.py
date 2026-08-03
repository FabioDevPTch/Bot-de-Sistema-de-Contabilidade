from playwright.sync_api import sync_playwright
from openpyxl import *
import re
import random

with sync_playwright() as pw: 
    browser = pw.chromium.launch(headless=False)
    
    context = browser.new_context( 
        viewport={"width": 1920, "height": 1080},
        accept_downloads=True,
        locale="pt-BR",
    )

    page = context.new_page()
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(60000)
    
    page.goto('https://simulacontabil.netlify.app/?_gl=1*10gaw9l*_ga*NTYwNzg1NjY1LjE3MjcyMjMzMDk.*_ga_37GXT4VGQK*czE3ODQyMTUzNTYkbzQ3MiRnMSR0MTc4NDIxNTQyNyRqNDkkbDAkaDA.#/login',wait_until='domcontentloaded')

    page.wait_for_timeout(1500)
    
    campo_email = page.get_by_role('textbox', name = 'Email')

    campo_email.click()
    page.wait_for_timeout(1000)

    campo_email.type('admin@simulacontabil.com.br', delay = random.randint(50, 100))
    page.wait_for_timeout(800)

    campo_senha = page.get_by_role('textbox', name = 'Senha')
    page.wait_for_timeout(1000)

    campo_senha.click()

    campo_senha.type('admin', delay = random.randint(100, 200))
    page.wait_for_timeout(1000)

    botao_entrar = page.get_by_role('button', name = 'Entrar')

    botao_entrar.click()

    page.wait_for_timeout(2000)

    lancamentos = page.get_by_role('link', name = 'Lançamentos')

    lancamentos.click()

    planilha = load_workbook('lancamentos.xlsx')
    pagina_lancamentos = planilha['Lançamentos']

    for linha in pagina_lancamentos.iter_rows(min_row= 2, values_only = True):
        
        descricao = linha[0]
        valor = str(linha[1])
        data = linha[2]
        tipo = linha[3]
        categoria = linha[4]
        status = linha[5]

        novo_lancamento = page.get_by_role('button', name = 'Novo Lançamento')

        novo_lancamento.click()

        campo_descricao = page.get_by_test_id("input-description")

        campo_descricao.click()

        campo_descricao.type(descricao, delay = random.randint(50, 100))

        campo_valor = page.get_by_test_id("input-amount")

        campo_valor.click()

        campo_valor.type(valor, delay = random.randint(50, 100))

        campo_data = page.get_by_test_id("input-date")

        campo_data.click()

        campo_data.clear()

        campo_data.type(data, delay = random.randint(50, 100))

        if tipo == 'Despesa':
            page.get_by_test_id("select-type").select_option("DESPESA")
        else:
            page.get_by_test_id("select-type").select_option("RECEITA")

        page.get_by_test_id("select-category").select_option(categoria)

        page.locator("div").filter(has_text=re.compile(r"^StatusPendentePagoAtrasado$")).get_by_role("combobox").select_option(status.upper())

        page.get_by_test_id("btn-save").click()

        page.wait_for_timeout(1000)

    input('Digite ENTER para encerrar a automação: ')

    browser.close()