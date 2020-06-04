### Requisitos para executar a aplicação:
    1. Docker
    2. Docker Compose
    3. Git

### Clone do repositório:
```shell
git clone https://github.com/victorsls/cherryit_challenge.git
```

### Entrar no diretório do projeto:
```
cd cherryit_challenge
```

### Executar o docker:
```
docker-compose up
```

### Criando um usuário admin:
```
docker-compose exec backend python manage.py createsuperuser
```


### URL's:
**Backend**: [http://localhost:8000](http://localhost:8000)

**Frontend**: [http://localhost:4200](http://localhost:4200)
