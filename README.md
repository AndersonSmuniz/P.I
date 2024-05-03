# Sistema de Agendamento em Barbearias

Este é um sistema de agendamento desenvolvido em Django para barbearias. Ele permite que os clientes agendem horários online e que os funcionários gerenciem esses agendamentos.

## Requisitos

- Python 3.12 ou superior
- [Poetry](https://python-poetry.org/) para gerenciamento de dependências

## Configuração do Ambiente

Siga os passos abaixo para configurar e rodar o sistema em sua máquina local.

### 1. Clonar o Repositório

Clone este repositório em sua máquina:

```bash
git clone https://github.com/AndersonSmuniz/P.I.git
cd P.I
```

### 2. Criar e Ativar Ambiente Virtual

Recomendo o uso de um ambiente virtual para isolar as dependências do sistema.

Com poetry(recomendado):
```bash
poetry shell
```

Com venv:
```bash
python -m venv venv
source venv/bin/activate  # Para Linux/Mac
venv\Scripts\activate      # Para Windows
```

### 3. Instalar Dependências

Este projeto utiliza Poetry para gerenciamento de dependências. Certifique-se de ter o Poetry instalado (veja [aqui](https://python-poetry.org/docs/#installation) como instalar).

Dentro do diretório do projeto, instale as dependências com o Poetry:

```bash
poetry install
```

### 4. Configurar Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```plaintext
SECRET_KEY=seu_valor_secreto_aqui
DEBUG=True
```

Substitua `seu_valor_secreto_aqui` por uma chave secreta forte para o Django.

### 5. Aplicar Migrações

Aplique as migrações ao banco de dados:

```bash
python manage.py migrate
```

### 6. Criar um Superusuário

Para acessar a área administrativa do Django, crie um superusuário:

```bash
python manage.py createsuperuser
```

Siga as instruções no terminal para configurar o superusuário.

### 7. Executar o Servidor de Desenvolvimento

Finalmente, inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

O sistema estará disponível em `http://127.0.0.1:8000/`.

## Contribuição

```
```

## Licença

```
```