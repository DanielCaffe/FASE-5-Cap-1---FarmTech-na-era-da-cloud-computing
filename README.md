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

## 📁 Estrutura de Pastas

```
📦 nome arquivo/
├── assets/
├── config/
├── document/
│   └── other/
├── scripts/
├── src/
├── .github/
├── README.md
├── wokwi.toml
```

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

### 💻 Execução Local com PlatformIO

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/repositorio.git
   ```
2. Navegue até a pasta:
   ```bash
   cd repositorio
   ```
3. Instale as dependências e compile:
   ```bash
   pio run
   ```
4. Para fazer upload (se estiver com ESP32 real):
   ```bash
   pio run --target upload
   ```

---

## 🧠 Teoria de Operação

### Botões:

- **Verde (Manual)**: Liga a bomba de irrigação
- **Azul (Simulado)**: Controla acionamento automatizado
- Possuem **resistores pull-down** ou **pull-up** conforme a lógica
- Atributo `bounce="1"` no Wokwi evita ruído (debounce mecânico)

### Sensores:

- **DHT22**: Umidade relativa do ar e temperatura
- **LDR**: Mede intensidade luminosa (lux)
- Os valores dos sensores são lidos e avaliados para decidir irrigação

---

## 🗃 Histórico de Lançamentos

- 0.1.0 - 20/05/2025
---

## 📋 Licença

<img src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" height="22px"><img src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" height="22px">

<p>
Este repositório é baseado no modelo acadêmico da FIAP e está licenciado sob a <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank">Creative Commons Attribution 4.0 International</a>.
</p>
