# CryptoHub
O projeto "CryptoHub" é uma aplicação Python que utiliza a CryptoCompare API para obter e exibir em tempo real os preços das principais criptomoedas. Essa ferramenta permite que os usuários acompanhem de maneira fácil e rápida as flutuações de preços das criptomoedas mais populares.

## Instalação

Primeiramente clone o projeto e entre na pasta principal com os comandos abaixo: 
```bash
   git clone https://github.com/ParsivalT/CryptoHub.git
   cd CryptoHub
```

Em seguida crie um ambiente virtual:

```bash
    python -m venv .venv
    source venv/bin/activate
```

Logo em seguida instale as dependencias do projeto
```bash
    pip install -r requirements.txt
```

## Como ultilizar ?

Após a instalação e configuração do ambiente rode o seguinte comando: 

```bash
    python main.py 
```
Após rodar o comando acima o programa ira pedir a sigla do cripto ativo que você deseja consultar. 
```bash
    Enter the asset you want to monitor(BTC: bitcoin):
```

Em seguida ele ira perguntar em qual formato de você deseja receber a cotação da moeda.

```bash
    Enter the format(BRL: brazilian coin):
```


