"""
Versao 1.0.1 ### 01/2018
Gerador de Log para o portal Moodle
O log ira preservar apenas duas colunas, Como Nome e Conteudo
################################################################
para usar abra o terminal e tenha certeza que os pacotes de python como,
bs4 ou beautifulsoup4 e pandas estao instalados na maquina.

use o pip package manager do python para instalar.
abra o terminal e digite >>>
pip install -U --user pip
pip install -U --user beautifulsoup4 pandas
caso voce instale o python global para todos os usuarios voce tera que usar o terminal
com permissao de administrador.

################################################################
coloque o arquivo dentro da pasta que tenha todos os arquivos csv ou txt
python analise_dados.py e aguarde alguns minutos

"""
# ^[ \t\v]*#.*?coding[:=][ \t]*([-_.a-zA-Z0-9]+)

import csv
import os.path
import shutil
import subprocess
from glob import glob
from os import path, makedirs

import pandas as pd
from bs4 import BeautifulSoup as bs

BASE_DIR = path.dirname(path.abspath(__file__))
del_data = path.join(BASE_DIR, 'del_data')
gen_data = path.join(BASE_DIR, 'gen_data')
rel_data = path.join(BASE_DIR, 'rel_data')

folder_base = [
path.join(BASE_DIR, 'rel_data'),
path.join(BASE_DIR, 'rel_log'),
path.join(BASE_DIR, 'clean_data')
]

def del_create():
    if os.path.isdir(gen_data):
        shutil.rmtree(gen_data)
    else:
        makedirs('gen_data')

    if os.path.isdir(del_data):
        shutil.rmtree(del_data)
    else:
        makedirs('del_data')

    if os.path.isdir(rel_data):
        shutil.rmtree(rel_data)
    else:
        makedirs('rel_data')


def get_dir():
    del_create()
    # Getting the list of file in directory
    dired = []
    for item in glob('*'):
        if item.endswith('.csv') or item.endswith('.txt'):
            dired.append(item)

    return dired


f_open = get_dir()

for entry in f_open:
    file = entry
    file_data = path.join(del_data, 'del_{}'.format(file))
    log_table = path.join(gen_data, 'gen_{}'.format(file))
    log_pivot = path.join(rel_data, 'rel_{}'.format(file))

    with open(file, encoding='utf-8') as file_parse:
        csv_reader = csv.reader(file_parse)

        with open(file_data, mode='w', newline='', encoding='mbcs') as new_file:
            csv_writer = csv.writer(new_file)

            csv_writer.writerow(('NOME', 'CONTEUDO'))

            next(csv_reader)
            for line in csv_reader:
                soup = bs(line[2], 'html.parser')
                item = [u.string for u in soup.find_all('a')]
                l = [u.upper() for u in item][0]

                csv_writer.writerow([l, line[4].upper()])


print('Log 1 Gerado com Sucesso')
print('Gerando Proximo Log, Aguarde...')


for entry in f_open:
    file = entry
    file_data = path.join(del_data, 'del_{}'.format(file))
    log_table = path.join(gen_data, 'gen_{}'.format(file))
    log_pivot = path.join(rel_data, 'rel_{}'.format(file))

    with open(file_data, mode='r' ,encoding='mbcs') as pdf:
        pd_file = pd.read_csv(pdf)
        df = pd_file.groupby(['NOME','CONTEUDO'])['CONTEUDO'].count()

        df.to_csv(log_table, sep=',', encoding='mbcs', header=True)


print('Log 2 Gerado Com Sucesso')
print('Gerando Proximo Log, Aguarde....')


for entry in f_open:
    file = entry
    file_data = path.join(del_data, 'del_{}'.format(file))
    log_table = path.join(gen_data, 'gen_{}'.format(file))
    log_pivot = path.join(rel_data, 'rel_{}'.format(file))

    with open(log_table, mode='r' ,encoding='mbcs') as pdf:
        pivot = pd.read_csv(pdf)
        df = pivot.pivot_table(columns=['CONTEUDO'], index=['NOME'])
        df.to_csv(log_pivot, header=True, encoding='mbcs')


print('Arquivos Gerados com Sucesso, Verifique a pasta {}'.format(gen_data))

