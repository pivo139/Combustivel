markdown
# Calculadora Álcool ou Gasolina ⛽

Desenvolvi uma aplicação simples de linha de comando (CLI) desenvolvida em **Python** para ajudar motoristas a decidirem qual combustível é mais vantajoso financeiramente na hora de abastecer.

## 📋 Como funciona

O cálculo é baseado na regra de rendimento padrão: o álcool (etanol) rende, em média, **70%** do que rende a gasolina. 

O programa divide o valor do litro do álcool pelo valor do litro da gasolina (`alcool / gasolina`):
* Se o resultado for **menor ou igual a 0,70**, o **álcool** compensa mais.
* Se o resultado for **maior que 0,70**, a **gasolina** compensa mais.

## 🚀 Funcionalidades

* Entrada de valores decimais (float) para o preço do álcool e da gasolina.
* Cálculo automático da proporção entre os preços.
* Loop interativo que permite realizar múltiplos cálculos sem precisar reiniciar o programa.

## 🛠️ Pré-requisitos

Para rodar este projeto, você só precisa ter o **Python 3** instalado na sua máquina.

## 💻 Como executar

1. Clone este repositório:
```bash
git clone https://github.com/pivo139/Combustivel.git
```

2. Acesse a pasta do projeto:
```bash
cd Combustivel
```

3. Execute o script:
```bash
python main.py
```
*(Substitua `main.py` pelo nome do arquivo em que você salvou o código).*

## 📝 Exemplo de uso

```text
Digite o valor do alcool: 3.89
Digite o valor da gasolina: 5.79
Vale a pena colocar alcool
Deseja refazer a aplicação? (s/n) n
Obrigado, volte sempre!
```