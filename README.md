# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" width="40%">
  </a>
</p>

---

# 💧 Entrega 2: Armazenamento de Dados em Banco SQL com Python

## 💻 Grupo: Grupo: Graduação - 1TIAOB - 2025/1 - Grupo 23

## 👨‍🎓 Integrantes: 
- Daniel Caffé RM564440
- Larissa RM566418
- Enrico RM561352
- Davi RM566336
- Ednilton RM66069

## 👩‍🏫 Professores:
### Tutor(a)
- [Lucas Gomes Moreira](https://www.linkedin.com/company/inova-fusca)

### Coordenador(a)
- [Nome do Coordenador](https://www.linkedin.com/company/inova-fusca)

---

## 📜 Descrição

Projeto que simula sensores agrícolas no Wokwi (ESP32) e armazena dados em banco Oracle.

Sensores Simulados

Temperatura (temp): em graus Celsius

Umidade (umi): porcentagem

pH (ph): valor float entre 0 e 14

Status da Bomba (bomba): 1 = ligada, 0 = desligada

Tempo de ativação (tempo): em minutos (pode ser nulo)

Fase da operação: texto descritivo ("Inicial", "Crítica", etc)

---

## 📜 Dados do monitor serial do ESP32

![image](https://github.com/user-attachments/assets/f4970eea-af9e-4ccd-ab51-d23eff0e9f4a)

![image](https://github.com/user-attachments/assets/214c1646-bfa3-4b9d-a40c-9f74f04cb748)

![image](https://github.com/user-attachments/assets/1a72720f-94ad-4312-903f-6100b1a3d1d5)

![image](https://github.com/user-attachments/assets/61a80c01-3f7c-442a-9c7e-0feb569b6652)

---

## Funcionalidades do Menu

1 - Cadastrar Leitura
2 - Listar Leituras
3 - Alterar Leitura
4 - Excluir Leitura
5 - Excluir Todas as Leituras
6 - Sair

1. Cadastrar Leitura
Solicita os dados ao usuário e armazena uma nova linha no banco.

2. Listar Leituras
Exibe todas as leituras armazenadas utilizando um DataFrame do pandas.

3. Alterar Leitura
Permite alterar o valor de umidade de um registro específico com base no ID.

4. Excluir Leitura
Remove uma leitura com base no ID informado.

5. Excluir Todas as Leituras
Apaga todos os registros da tabela com confirmação do usuário.

## 🔧 Como Executar o Código

### 🛠 Requisitos:

- Python 3.11+
- Biblioteca oracledb:
- pip install oracledb
- Biblioteca pandas:
- pip install pandas
- Banco Oracle ativo

### 💻 Execução Script Python:

# Importação dos módulos
import os
import oracledb
import pandas as pd
from datetime import datetime

# Tentativa de conexão com o banco de dados
try:
    conn = oracledb.connect(user='USUARIO', password='SENHA', dsn='oracle.fiap.com.br:1521/ORCL')
    inst_cadastro = conn.cursor()
    inst_consulta = conn.cursor()
    inst_alteracao = conn.cursor()
    inst_exclusao = conn.cursor()
except Exception as e:
    print("Erro na conexão com o banco:", e)
    conexao = False
else:
    conexao = True

margem = ' ' * 4

# Loop principal da aplicação
while conexao:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---- SIMULADOR DE SENSORES AGRÍCOLAS ----")
    print("""
    1 - Cadastrar Leitura
    2 - Listar Leituras
    3 - Alterar Leitura
    4 - Excluir Leitura
    5 - EXCLUIR TODAS AS LEITURAS
    6 - SAIR
    """)

    escolha = input(margem + "Escolha -> ")

    if not escolha.isdigit():
        print("\nOpção inválida!")
        input("Pressione ENTER")
        continue

    match int(escolha):
        case 1:
            try:
                print("----- CADASTRAR LEITURA -----\n")
                temp = float(input(margem + "Temperatura (°C): "))
                umi = float(input(margem + "Umidade (%): "))
                ph = float(input(margem + "pH: "))
                bomba = int(input(margem + "Bomba Ligada? (1=Sim / 0=Não): "))
                tempo = input(margem + "Tempo de Ativação (min): ")
                tempo = float(tempo) if tempo else None
                fase = input(margem + "Fase da operação: ")

                sql = f"""
                INSERT INTO SensorSimulacao (data_hora, temperatura, umidade, ph, status_bomba, tempo_ativacao, fase)
                VALUES (TO_TIMESTAMP('{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}', 'YYYY-MM-DD HH24:MI:SS'),
                        {temp}, {umi}, {ph}, {bomba}, {tempo if tempo is not None else 'NULL'}, '{fase}')
                """
                inst_cadastro.execute(sql)
                conn.commit()
            except ValueError:
                print("\nDigite valores numéricos válidos!")
            except Exception as e:
                print("Erro ao cadastrar:", e)
            else:
                print("\nLeitura cadastrada com sucesso!")
            input("Pressione ENTER")

        case 2:
            print("----- LISTAR LEITURAS -----\n")
            inst_consulta.execute("SELECT * FROM SensorSimulacao")
            data = inst_consulta.fetchall()
            if data:
                df = pd.DataFrame.from_records(data, columns=[
                    'ID', 'Data/Hora', 'Temperatura', 'Umidade', 'pH', 'Status Bomba', 'Tempo Ativação', 'Fase'
                ], index='ID')
                print(df)
            else:
                print("\nNenhuma leitura registrada.")
            input("\nPressione ENTER")

        case 3:
            try:
                print("----- ALTERAR LEITURA -----\n")
                leitura_id = int(input(margem + "Digite o ID da leitura a alterar: "))
                sql_check = f"SELECT * FROM SensorSimulacao WHERE id = {leitura_id}"
                inst_consulta.execute(sql_check)
                if not inst_consulta.fetchall():
                    print("\nLeitura não encontrada!")
                else:
                    nova_umidade = float(input(margem + "Nova Umidade (%): "))
                    sql_update = f"UPDATE SensorSimulacao SET umidade = {nova_umidade} WHERE id = {leitura_id}"
                    inst_alteracao.execute(sql_update)
                    conn.commit()
                    print("\nLeitura atualizada com sucesso!")
            except Exception as e:
                print("Erro ao alterar leitura:", e)
            input("\nPressione ENTER")

        case 4:
            print("----- EXCLUIR LEITURA -----\n")
            leitura_id = input(margem + "Digite o ID da leitura a excluir: ")
            if leitura_id.isdigit():
                leitura_id = int(leitura_id)
                sql_del = f"DELETE FROM SensorSimulacao WHERE id = {leitura_id}"
                inst_exclusao.execute(sql_del)
                conn.commit()
                print("\nLeitura excluída!")
            else:
                print("ID inválido!")
            input("\nPressione ENTER")

        case 5:
            print("\n!!!!! EXCLUIR TODAS AS LEITURAS !!!!!\n")
            confirma = input(margem + "CONFIRMA A EXCLUSÃO DE TODAS AS LEITURAS? [S/N]: ")
            if confirma.upper() == 'S':
                inst_exclusao.execute("DELETE FROM SensorSimulacao")
                conn.commit()
                print("\nTodas as leituras foram removidas!")
            else:
                print("\nOperação cancelada.")
            input("\nPressione ENTER")

        case 6:
            print("Saindo da aplicação...")
            break

        case _:
            print("\nOpção inválida!")
            input("Pressione ENTER")

# Fechamento dos cursores e conexão
inst_cadastro.close()
inst_consulta.close()
inst_alteracao.close()
inst_exclusao.close()
conn.close()

---
# Justificativa da Estrutura de Dados e relacionamento MER

A estrutura de dados foi projetada para representar com fidelidade as leituras de sensores agrícolas em tempo real, simulando um cenário de automação no campo, com controle de irrigação baseado em variáveis ambientais.
---
Entidade Principal: SensorSimulacao
No Modelo Entidade-Relacionamento (MER), definimos a entidade central SensorSimulacao, que representa cada registro de leitura dos sensores no sistema. Esta entidade foi escolhida por ser atômica (uma linha = uma leitura completa) e independente (não depende de outras entidades para existir).

---

## Atributos e Justificativas

| Atributo         | Tipo         | Justificativa                                                               |
| ---------------- | ------------ | --------------------------------------------------------------------------- |
| `id`             | NUMBER       | Identificador único, gerado automaticamente. Facilita buscas e alterações.  |
| `data_hora`      | TIMESTAMP    | Captura o momento exato da leitura. Essencial para auditoria e análises.    |
| `temperatura`    | FLOAT        | Simula o sensor de temperatura, influencia diretamente a irrigação.         |
| `umidade`        | FLOAT        | Principal critério de ativação da bomba de irrigação.                       |
| `ph`             | FLOAT        | Simulado via sensor LDR; importante para qualidade do solo.                 |
| `status_bomba`   | NUMBER(1)    | Representa se a bomba estava ligada (1) ou desligada (0) durante a leitura. |
| `tempo_ativacao` | NUMBER       | Tempo de funcionamento da bomba (minutos). Pode ser nulo se desligada.      |
| `fase`           | VARCHAR2(30) | Representa o estágio do processo agrícola (Inicial, Crítica, etc.).         |

---

## Relacionamento com o MER

A estrutura segue o padrão de um MER relacional simples, com:

Chave primária (id) garantindo unicidade.

Dados normalizados (uma entidade, sem repetição de informações).

Campos bem tipados para refletir os sensores e contexto de leitura.

Sem necessidade de tabelas auxiliares, pois não há relacionamentos 1:N ou N:N no escopo da simulação.

---
Histórico de Lançamentos
0.1.0 - 20/05/2025

---

## 📋 Licença

<img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" height="22px"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" height="22px">

<p>
Este repositório é baseado no modelo acadêmico da FIAP e está licenciado sob a <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank">Creative Commons Attribution 4.0 International</a>.
</p>
