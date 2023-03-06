# case_senai_ia
## Instruções para a execução da API:

1. Faça um clone do repositório:

```
git clone https://github.com/edisahd/case_senai_ia.git
```

2. Acesse o diretório *"case_senai_ia*:

```
cd case_senai_ia
```

3. Ative a env:

```
source env/bin/activate
```

4. Acesse o banco de dados PostgreSQL:

```
sudo -u postgres psql
```

5. Crie um database chamado *credit_card_fraud_detection*:

```
create database credit_card_fraud_detection;
```

6. Saia do PostgreSQL:

```
\q
```

7. Execute o comando makemigrations

```
python3 manage.py makemigrations
```
