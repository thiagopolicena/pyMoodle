#!/usr/bin/env python3
"""
Author: Marcelo Marcon - marconm.inf0@gmail.com
Versao 1.0.2 ### 08/2019
Gerador de Log para o portal Moodle
O log ira preservar apenas duas colunas, Como Nome e Conteudo
################################################################
para usar abra o terminal e tenha certeza que os pacotes de python como,
bs4 ou beautifulsoup4 e pandas estao instalados na maquina.

use o pip package manager do python para instalar.
abra o terminal e digite >>>
pip install -U --user pip
caso voce instale o python global para todos os usuarios voce tera que usar o terminal
com permissao de administrador.

################################################################
coloque o arquivo dentro da pasta que tenha todos os arquivos csv ou txt
python analise_dados.py e aguarde alguns minutos

"""
# -*- coding: utf-8 -*-
__author__ = 'mmaconm'
#

import csv
import os.path
import shutil
from glob import glob
from os import path, name

import pandas as pd

BASE_DIR = path.abspath(path.dirname(__file__))
del_data = path.join(BASE_DIR, 'del_data')
gen_data = path.join(BASE_DIR, 'gen_data')
rel_data = path.join(BASE_DIR, 'rel_data')


def get_os() -> str:
    # retorna o tipo de encoding
    # baseado no sitema operacional

    if 'posix' in os.name:
        return 'latin1'  # linux

    return 'mbcs'  # windows


def del_or_create():
    # verifica as pastas se existem e deleta a mesma e a recria de novo
    for folder in [del_data, gen_data, rel_data]:
        if os.path.isdir(folder):
            shutil.rmtree(folder, ignore_errors=True)
            os.makedirs(folder)
        else:
            # caso nao exista as pastas, apenas cria
            os.makedirs(folder)


def get_dir(ftype: str = 'csv') -> list:
    # lista todos os csv's no diretorio atual
    # vai retornar uma lista
    return [i for i in glob('*') if i.endswith(f'.{ftype}')] or None


def create_log():
    f_open = get_dir()

    for entry in f_open:
        file = entry
        # nesta secao vai pegar o arquivo.csv e concatenar com 'rel_', 'gen_' e 'del_'
        file_data = path.join(del_data, 'del_{}'.format(file))
        log_table = path.join(gen_data, 'gen_{}'.format(file))
        log_pivot = path.join(rel_data, 'rel_{}'.format(file))

        with open(file, encoding='utf-8') as file_parse:
            # abre os arquivos
            csv_reader = csv.reader(file_parse)

            with open(file_data, mode='w', newline='', encoding=get_os()) as new_file:
                csv_writer = csv.writer(new_file)

                csv_writer.writerow(('NOME', 'CONTEUDO'))

                next(csv_reader)
                for line in csv_reader:
                    l = [u.upper() for u in line][1]

                    csv_writer.writerow([l, line[4].upper()])

    print('Log 1 Gerado com Sucesso')
    print('Gerando Proximo Log, Aguarde...')

    for entry in f_open:
        file = entry
        file_data = path.join(del_data, 'del_{}'.format(file))
        log_table = path.join(gen_data, 'gen_{}'.format(file))
        log_pivot = path.join(rel_data, 'rel_{}'.format(file))

        with open(file_data, mode='r', encoding=get_os()) as pdf:
            pd_file = pd.read_csv(pdf)
            df = pd_file.groupby(['NOME', 'CONTEUDO'])['CONTEUDO'].count()

            df.to_csv(log_table, sep=',', encoding=get_os(), header=True)

    for entry in f_open:
        file = entry
        file_data = path.join(del_data, 'del_{}'.format(file))
        log_table = path.join(gen_data, 'gen_{}'.format(file))
        log_pivot = path.join(rel_data, 'rel_{}'.format(file))

        with open(log_table, mode='r', encoding=get_os()) as pdf:
            pivot = pd.read_csv(pdf)
            df = pivot.pivot_table(columns=['CONTEUDO'], index=['NOME'])
            df.to_csv(log_pivot, header=True, encoding=get_os())

    print('Logs para Moodle 2019/1 Terminados')
    print('Arquivos Gerados com Sucesso, Verifique a pasta {}'.format(rel_data))


if __name__ == '__main__':
    del_or_create()
    create_log()
