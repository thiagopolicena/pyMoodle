# Projeto UAB Moodle - Python

PyMoodle

## Authors

* **Marcelo Marcon** - *Initial work* - [mmarconm](https://github.com/mmarconm/pyMoodle)

##Getting Started

use o pip package manager do python para instalar.
abra o terminal e digite.

```
pip install -U --user pip
pip install -U --user beautifulsoup4 pandas
```

caso voce instale o python global para todos os usuarios voce tera que usar o terminal
com permissao de administrador.
Python 3 para Windows
```
https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64-webinstall.exe
```

Python 3 para Linux
```
sudo apt install python3 python3-pip python3-virtualenv
```
### Prerequisites

Muito importante o arquivo requirements.txt contem as bibliotecas que deveram ser instaladas, para instalar use o pip com a flag -r

```
pip install -r requirements.txt
```

### Installing

Para usar coloque todos os arquivos .csv dentro da pasta do arquivo analise_dados.py

```
python3 analise_dados.py
```

ou se estiver usando ambiente virtual como o virualenv

```
python analise_dados.py
```

Dependendo da quantidade de arquivo e tamanho e velocidade do seu processador isso pode levar alguns minutos, ele irá criar algumas pastas com os logs separados


## Deployment

Author: Marcelo Marcon - marconm.inf0@gmail.com

## Built With

* [Marcelo Marcon](https://github.com/mmarconm/pyMoodle) - Python Dev


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Moodle
* Python Devs
