# Projeto UAB Moodle - Python

PyMoodle

## Authors

- **Marcelo Marcon** - _Initial work_ - [mmarconm](https://github.com/mmarconm/pyMoodle)

## Getting Started

Use o pip package manager do python para instalar.

Abra o terminal e digite:

```
pip install -U --user pip
```

Caso você instale o python global para todos os usuários voce terá que usar o terminal
com permissão de administrador.

Python 3 para Windows:

```
https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64-webinstall.exe
```

Python 3 para Linux:

```
sudo apt install python3 python3-pip python3-virtualenv
```

### System rsequirements

Muito importante o arquivo "requirements.txt" contem as bibliotecas que deverão ser instaladas.

Para instalar use o pip com a flag -r, conforme comando a seguir:

```
pip install -r requirements.txt
```

### Installing

Para usar coloque todos os arquivos ".csv" dentro da pasta do arquivo "analise_dados.py".

```
python3 analise_dados.py
```

Ou se estiver usando o ambiente virtual como o virtualenv

```
python analise_dados.py
```

Dependendo da quantidade de arquivo, tamanho e velocidade do seu processador isso pode levar alguns minutos, ele irá criar algumas pastas com os logs separados.

## Deployment

Author: Marcelo Marcon - marconm.inf0@gmail.com

## Built With

- [Marcelo Marcon](https://github.com/mmarconm/pyMoodle) - Python Dev

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- Moodle
- Python Devs
