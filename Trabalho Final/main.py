import csv
from collections import namedtuple
from getpass import getpass
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

# Constantes
ARQUIVO_USUARIOS = 'usuarios.csv'
ARQUIVO_PRODUTOS = 'produtos.csv'
USUARIO_LOGADO = None

console = Console()

##################### USUÁRIOS #####################

Usuario = namedtuple('Usuario', ['login', 'senha', 'tipo'])


def ler_usuarios(arquivo_csv):
    usuarios = {}
    with open(arquivo_csv, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            nome_usuario, senha, tipo = row
            usuarios[nome_usuario] = Usuario(login=nome_usuario, senha=senha, tipo=tipo)
    return usuarios


def fazer_login(usuarios):
    global USUARIO_LOGADO
    console.print(Panel('''🟢 [bold green]Login[/bold green] 🟢\n\nPor favor, insira suas credenciais.''', title="Tela de Login"))
    username = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    senha = getpass("Senha: ")
    user = usuarios.get(username, None)
    if user and user.senha == senha:
        console.print("\n[bold green]Login bem-sucedido![/bold green]")
        USUARIO_LOGADO = user
    else:
        console.print("[bold red]Erro: usuário ou senha incorretos!", style="red")


def cadastrar_usuario(usuarios, arquivo_csv):
    console.print(Panel('[bold green]Cadastro de Novo Usuário[/bold green]\nInsira os dados.', title="Novo Usuário"))
    nome_usuario = Prompt.ask("[bold cyan]Nome de Usuário[/bold cyan]")
    senha = getpass("Senha: ")
    tipo = 'cliente'
    if USUARIO_LOGADO and USUARIO_LOGADO.tipo == 'admin':
        tipo = Prompt.ask("Tipo de usuário (admin/funcionario/cliente)")
    if nome_usuario in usuarios:
        console.print("[red]Usuário já existe![/red]")
        return False
    with open(arquivo_csv, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome_usuario, senha, tipo])
    console.print("[green]Usuário cadastrado com sucesso![/green]")
    return nome_usuario


def excluir_usuario(usuarios, arquivo_csv):
    nome_usuario = Prompt.ask("Nome do usuário a excluir")
    if nome_usuario not in usuarios:
        console.print("[yellow]Usuário não encontrado![/yellow]")
        return False
    with open(arquivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        for usuario in usuarios.values():
            if usuario.login != nome_usuario:
                writer.writerow([usuario.login, usuario.senha, usuario.tipo])
    console.print(f"[green]Usuário '{nome_usuario}' excluído com sucesso![/green]")
    return True


def atualiza_senha(usuarios, arquivo_csv):
    global USUARIO_LOGADO
    nome_usuario = USUARIO_LOGADO.login if USUARIO_LOGADO.tipo != 'admin' else Prompt.ask("Nome do usuário")
    nova_senha = getpass("Nova senha: ")
    if nome_usuario not in usuarios:
        console.print("[yellow]Usuário não encontrado![/yellow]")
        return False
    with open(arquivo_csv, mode='w', newline='') as file:
        writer = csv.writer(file)
        for usuario in usuarios.values():
            if usuario.login == nome_usuario:
                writer.writerow([usuario.login, nova_senha, usuario.tipo])
            else:
                writer.writerow([usuario.login, usuario.senha, usuario.tipo])
    console.print("[green]Senha atualizada com sucesso![/green]")
    return True


##################### PRODUTOS #####################

Produto = namedtuple('Produto', ['codigo', 'nome', 'preco', 'quantidade'])


def ler_produtos(arquivo_csv):
    produtos = {}
    with open(arquivo_csv, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            codigo, nome, preco, quantidade = row
            produtos[codigo] = Produto(codigo, nome, float(preco), int(quantidade))
    return produtos


def salvar_produtos(produtos, arquivo_csv):
    with open(arquivo_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for p in produtos.values():
            writer.writerow([p.codigo, p.nome, p.preco, p.quantidade])


def cadastrar_produto(produtos, arquivo_csv):
    codigo = Prompt.ask("Código")
    if codigo in produtos:
        console.print("[red]Produto já cadastrado![/red]")
        return
    nome = Prompt.ask("Nome")
    preco = float(Prompt.ask("Preço"))
    quantidade = int(Prompt.ask("Quantidade"))
    with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([codigo, nome, preco, quantidade])
    console.print("[green]Produto cadastrado com sucesso![/green]")


def atualizar_produto(produtos, arquivo_csv):
    codigo = Prompt.ask("Código do produto")
    if codigo not in produtos:
        console.print("[red]Produto não encontrado![/red]")
        return
    nome = Prompt.ask("Novo nome", default=produtos[codigo].nome)
    preco = float(Prompt.ask("Novo preço", default=str(produtos[codigo].preco)))
    quantidade = int(Prompt.ask("Nova quantidade", default=str(produtos[codigo].quantidade)))
    produtos[codigo] = Produto(codigo, nome, preco, quantidade)
    salvar_produtos(produtos, arquivo_csv)
    console.print("[green]Produto atualizado com sucesso![/green]")


def excluir_produto(produtos, arquivo_csv):
    codigo = Prompt.ask("Código do produto")
    if codigo not in produtos:
        console.print("[red]Produto não encontrado![/red]")
        return
    del produtos[codigo]
    salvar_produtos(produtos, arquivo_csv)
    console.print("[green]Produto excluído com sucesso![/green]")


def listar_por_nome(produtos):
    for p in sorted(produtos.values(), key=lambda p: p.nome):
        console.print(f"{p.codigo} - {p.nome} - R${p.preco:.2f} - Estoque: {p.quantidade}")


def listar_por_preco(produtos):
    for p in sorted(produtos.values(), key=lambda p: p.preco):
        console.print(f"{p.codigo} - {p.nome} - R${p.preco:.2f} - Estoque: {p.quantidade}")


def comprar_livro(produtos, arquivo_csv):
    codigo = Prompt.ask("Código do livro que deseja comprar")
    if codigo not in produtos:
        console.print("[red]Livro não encontrado![/red]")
        return
    livro = produtos[codigo]
    if livro.quantidade <= 0:
        console.print("[yellow]Livro esgotado![/yellow]")
        return
    produtos[codigo] = livro._replace(quantidade=livro.quantidade - 1)
    salvar_produtos(produtos, arquivo_csv)
    console.print(f"[green]Você comprou '{livro.nome}' com sucesso![/green]")

##################### MENUS #####################

def menu_inicial():
    console.print(Panel("[bold green]Sistema Livros & Letras[/bold green]", title="Menu Inicial"))
    console.print("1. Fazer Login")
    console.print("2. Cadastro")
    console.print("3. Sair")
    return Prompt.ask("Escolha uma opção", choices=["1", "2", "3"])


def menu_admin():
    console.print("\n1. Atualizar senha")
    console.print("2. Excluir usuário")
    console.print("3. Cadastrar produto")
    console.print("4. Atualizar produto")
    console.print("5. Excluir produto")
    console.print("6. Listar por nome")
    console.print("7. Listar por preço")
    console.print("8. Logout")
    return Prompt.ask("Escolha", choices=[str(i) for i in range(1,9)])


def menu_cliente():
    console.print("\n1. Atualizar senha")
    console.print("2. Ver livros por nome")
    console.print("3. Ver livros por preço")
    console.print("4. Comprar livro")
    console.print("5. Logout")
    return Prompt.ask("Escolha", choices=[str(i) for i in range(1,6)])

##################### LOOP PRINCIPAL #####################

usuarios = ler_usuarios(ARQUIVO_USUARIOS)
produtos = ler_produtos(ARQUIVO_PRODUTOS)

while True:
    opcao = menu_inicial()
    if opcao == '1':
        fazer_login(usuarios)
    elif opcao == '2':
        novo = cadastrar_usuario(usuarios, ARQUIVO_USUARIOS)
        if novo:
            usuarios = ler_usuarios(ARQUIVO_USUARIOS)
    elif opcao == '3':
        break

    while USUARIO_LOGADO:
        if USUARIO_LOGADO.tipo == 'admin':
            op = menu_admin()
            if op == '1': atualiza_senha(usuarios, ARQUIVO_USUARIOS)
            elif op == '2': excluir_usuario(usuarios, ARQUIVO_USUARIOS)
            elif op == '3': cadastrar_produto(produtos, ARQUIVO_PRODUTOS)
            elif op == '4': atualizar_produto(produtos, ARQUIVO_PRODUTOS)
            elif op == '5': excluir_produto(produtos, ARQUIVO_PRODUTOS)
            elif op == '6': listar_por_nome(produtos)
            elif op == '7': listar_por_preco(produtos)
            elif op == '8': USUARIO_LOGADO = None
        else:
            op = menu_cliente()
            if op == '1': atualiza_senha(usuarios, ARQUIVO_USUARIOS)
            elif op == '2': listar_por_nome(produtos)
            elif op == '3': listar_por_preco(produtos)
            elif op == '4': comprar_livro(produtos, ARQUIVO_PRODUTOS)
            elif op == '5': USUARIO_LOGADO = None
        usuarios = ler_usuarios(ARQUIVO_USUARIOS)
        produtos = ler_produtos(ARQUIVO_PRODUTOS)