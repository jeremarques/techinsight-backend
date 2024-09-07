
# TechInsight - Backend

Este repositório contém o backend do projeto TechInsight, um site focado na comunidade tech. Seu objetivo é promover a livre disseminação de conhecimento por meio de publicações, comentários e outras interações.


## Stack utilizada

**Back-end:** Python, Django, Django Rest Framework


## Rodando localmente

Rodar o TechInsight localmente em sua máquina é super simples.

Clone o repositório e entre dentro da pasta

```bash
git clone git@github.com:jeremarques/techinsight-backend.git
cd techinsight-backend
```

Crie o ambiente virtual ou utilize o Docker, com o Dokerfile na raiz do projeto,

```bash
# Utilizando o virtual-env
python -m venv venv
source ./venv/bin/activate
  
# Instale as dependências do projeto
pip install -r requirements.txt
```

Crie o arquivo .env a partir do .env.example e preencha com suas respectivas informações.

Após isso, inicie o servidor de desenvolvimento

```bash
# Somente localhost (127.0.0.1) na porta 8000
python manage.py runserver

# localhost e IP na porta 8000
python manage.py runserver 0.0.0.0:8000cha
```

É isso, agora o projeto estará rodando localmente em sua máquina.


    
## Contribuindo

Contribuições são bem-vindas e altamente encorajadas! Se você deseja ajudar a melhorar o TechInsight, siga as etapas abaixo para começar:

Veja `CONTRIBUTING.md` para saber como começar.

Por favor, siga o `código de conduta` desse projeto.


## História e motivações

Jeremias Marques, autor do projeto, movido por sua grande vontade de aprender coisas novas e inovadoras, decidiu criar um projeto durante suas férias do trabalho e da escola. Ele escolheu explorar, de forma autodidata, os processos de idealização, modelagem e execução do projeto. Em pouco mais de dois meses, trabalhou intensamente nesse projeto. Durante a criação do TechInsight, Jeremias enfrentou diversos desafios, especialmente na modelagem e estruturação, já que se tratava de uma "rede social". No entanto, ao final, obteve um resultado satisfatório.

O TechInsight é, inicialmente, um projeto de estudo, pois ainda faltam diversas funcionalidades para que possa ser considerado uma "rede social" completa. No entanto, já atendeu ao objetivo principal de seu criador: absorver o máximo de conhecimento sobre idealização, modelagem e execução de uma aplicação do zero, utilizando diversos padrões como DDD, Clean Architecture e TDD.

## Autor

- [@jeremarques](https://www.github.com/jeremarques)

## Licença

[GPL-3.0](https://choosealicense.com/licenses/gpl-3.0/)
