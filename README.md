# 🍽️ Cardápio Universitário

Uma aplicação web desenvolvida para facilitar a visualização de produtos e a organização de pedidos em um ambiente universitário.

O projeto utiliza **Python e Django** no backend, com uma interface construída em HTML, CSS e JavaScript, oferecendo uma experiência simples e prática para os usuários.

---

## 📖 Sobre o projeto

O **Cardápio Universitário** nasceu com a proposta de digitalizar e simplificar o acesso ao cardápio de estabelecimentos alimentícios no ambiente universitário.

Por meio da aplicação, os usuários podem visualizar os produtos disponíveis, consultar informações e preços e selecionar itens em um carrinho de compras.

Além disso, o projeto utiliza os recursos administrativos do Django para facilitar o gerenciamento dos produtos cadastrados.

## ✨ Funcionalidades

- 🍔 **Cardápio digital:** visualização dos produtos disponíveis.
- 🛒 **Carrinho de compras:** seleção e organização dos itens desejados.
- 💰 **Informações dos produtos:** exibição de nomes, preços e imagens.
- ⚙️ **Painel administrativo:** gerenciamento dos produtos pelo Django Admin.
- 🗄️ **Banco de dados:** armazenamento das informações utilizadas pela aplicação.

## 🛠️ Tecnologias utilizadas

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal do backend |
| Django | Framework web e gerenciamento administrativo |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização da interface |
| JavaScript | Interatividade no frontend |
| SQLite | Banco de dados para desenvolvimento local |
| Git e GitHub | Versionamento de código |
| Vercel | Plataforma escolhida para hospedagem |

## 📂 Estrutura do projeto

Alguns arquivos importantes da aplicação:

```text
cardapioUniversitario/
├── cardapio/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

- `settings.py`: configurações gerais do Django.
- `urls.py`: definição das rotas principais.
- `manage.py`: comandos de gerenciamento.
- `requirements.txt`: dependências necessárias para executar o projeto.

## 🚀 Como executar localmente

### 1. Pré-requisitos

Antes de começar, tenha instalado:

- Python 3.12 ou superior
- Git
- pip

### 2. Clone o repositório

```bash
git clone https://github.com/gabriel-galleg0/cardapioUniversitario.git
cd cardapioUniversitario
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual:

**Windows:**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```dotenv
DJANGO_ENV=development
DJANGO_SECRET_KEY=sua-chave-secreta-local
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

Substitua o valor de `DJANGO_SECRET_KEY` por uma chave gerada para seu ambiente.

**Importante:** não publique o arquivo `.env` no GitHub. Inclua-o no `.gitignore`.

### 6. Execute as migrações

```bash
python manage.py migrate
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

A aplicação estará disponível em:

**http://127.0.0.1:8000/**

## 🔐 Painel administrativo

Para acessar o Django Admin, crie um superusuário:

```bash
python manage.py createsuperuser
```

Depois, acesse:

**http://127.0.0.1:8000/admin/**

Utilize as credenciais criadas para gerenciar os dados da aplicação.

## ☁️ Deploy

O projeto está sendo preparado para hospedagem na **Vercel**.

Para executar a aplicação em produção, é necessário configurar as variáveis de ambiente, utilizar um banco de dados persistente e garantir que os arquivos estáticos e as imagens sejam servidos corretamente.

O endereço público da aplicação será adicionado quando o deploy estiver funcionando.

## 🔮 Próximos passos

- [ ] Finalizar o deploy na Vercel.
- [ ] Configurar um banco PostgreSQL para produção.
- [ ] Implementar armazenamento persistente de imagens.
- [ ] Adicionar testes automatizados.
- [ ] Aperfeiçoar a experiência de navegação.

## 🤝 Contribuições

Sugestões e melhorias são bem-vindas!

Para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para sua alteração.
3. Implemente suas melhorias.
4. Abra um Pull Request descrevendo as mudanças.

## 👨‍💻 Desenvolvedores e colaboradores

### 🚀 Idealização e desenvolvimento inicial

**[Rodrigo Hernandes](https://github.com/RodrigoHernandes31415)**

Responsável pela idealização, criação e desenvolvimento inicial do **Cardápio Universitário**, dando origem ao projeto e à sua proposta de facilitar o acesso a cardápios e a organização de pedidos no ambiente universitário.

### 🤝 Desenvolvimento colaborativo

**[Gabriel Gallego](https://github.com/gabriel-galleg0)**

Colaborador no desenvolvimento e aprimoramento da aplicação, além de disponibilizar seu GitHub para hospedagem e versionamento do repositório.

### 📌 Repositório

O projeto é desenvolvido de forma colaborativa e está disponível publicamente no GitHub:

🔗 [Cardápio Universitário — GitHub](https://github.com/gabriel-galleg0/cardapioUniversitario)

---

⭐ Se este projeto foi útil ou interessante para você, considere deixar uma estrela no repositório!
