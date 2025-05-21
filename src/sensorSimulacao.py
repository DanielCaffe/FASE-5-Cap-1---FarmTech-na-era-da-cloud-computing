import os
import sqlite3
import pandas as pd
from datetime import datetime

# Conexão com banco SQLite (cria o arquivo se não existir)
conn = sqlite3.connect("simulador.db")
cursor = conn.cursor()

# Criação da tabela (simula a estrutura usada no Oracle)
cursor.execute("""
CREATE TABLE IF NOT EXISTS SensorSimulacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data_hora TEXT,
    temperatura REAL,
    umidade REAL,
    ph REAL,
    status_bomba INTEGER,
    tempo_ativacao REAL,
    fase TEXT
)
""")
conn.commit()

margem = ' ' * 4

# Loop principal
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("---- SIMULADOR DE SENSORES AGRÍCOLAS (SQLite) ----")
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

                data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                cursor.execute("""
                    INSERT INTO SensorSimulacao (data_hora, temperatura, umidade, ph, status_bomba, tempo_ativacao, fase)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (data_hora, temp, umi, ph, bomba, tempo, fase))
                conn.commit()
                print("\nLeitura cadastrada com sucesso!")
            except Exception as e:
                print("Erro ao cadastrar:", e)
            input("Pressione ENTER")

        case 2:
            print("----- LISTAR LEITURAS -----\n")
            cursor.execute("SELECT * FROM SensorSimulacao")
            data = cursor.fetchall()
            if data:
                df = pd.DataFrame(data, columns=[
                    'ID', 'Data/Hora', 'Temperatura', 'Umidade', 'pH', 'Status Bomba', 'Tempo Ativação', 'Fase'
                ])
                print(df.to_string(index=False))
            else:
                print("\nNenhuma leitura registrada.")
            input("\nPressione ENTER")

        case 3:
            try:
                print("----- ALTERAR LEITURA -----\n")
                leitura_id = int(input(margem + "Digite o ID da leitura a alterar: "))
                cursor.execute("SELECT * FROM SensorSimulacao WHERE id = ?", (leitura_id,))
                if not cursor.fetchone():
                    print("\nLeitura não encontrada!")
                else:
                    nova_umidade = float(input(margem + "Nova Umidade (%): "))
                    cursor.execute("UPDATE SensorSimulacao SET umidade = ? WHERE id = ?", (nova_umidade, leitura_id))
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
                cursor.execute("DELETE FROM SensorSimulacao WHERE id = ?", (leitura_id,))
                conn.commit()
                print("\nLeitura excluída!")
            else:
                print("ID inválido!")
            input("\nPressione ENTER")

        case 5:
            print("\n!!!!! EXCLUIR TODAS AS LEITURAS !!!!!\n")
            confirma = input(margem + "CONFIRMA A EXCLUSÃO DE TODAS AS LEITURAS? [S/N]: ")
            if confirma.upper() == 'S':
                cursor.execute("DELETE FROM SensorSimulacao")
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

# Fechamento da conexão
cursor.close()
conn.close()
