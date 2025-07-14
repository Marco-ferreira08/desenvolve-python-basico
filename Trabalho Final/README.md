# Trabalho Prático – Sistema de Gerenciamento

## Introdução

Este sistema simula o gerenciamento de uma livraria chamada **Livros & Letras**, com controle de usuários e produtos (livros). Os tipos de usuário são: admin, funcionário e cliente. O admin tem todas as permissões de CRUD, enquanto os clientes apenas podem atualizar seus dados. Os produtos registrados são livros, com nome, preço e quantidade em estoque.

## Implementação

### Usuários
- Estrutura: dicionário de `Usuario` (tupla nomeada)
- Arquivo: `usuarios.csv`
- Funcionalidades:
  - Create: cadastro de usuário
  - Read: leitura e login
  - Update: alteração de senha
  - Delete: exclusão de usuário

### Produtos
- Estrutura: dicionário de `Produto` (tupla nomeada)
- Arquivo: `produtos.csv`
- Funcionalidades:
  - Create: cadastro de novo livro
  - Read: listagem e busca
  - Update: atualização de dados
  - Delete: exclusão de livro
  - Listagem ordenada por nome e por preço

## Conclusão

Durante o desenvolvimento, desafios como manipulação de arquivos e atualização seletiva de registros foram superados com o uso de dicionários e regravação de arquivos. A estrutura final é funcional, clara e modular. Faria diferente talvez o uso de `pandas` para simplificar leitura e ordenação, mas optei por manter tudo com bibliotecas padrão.
