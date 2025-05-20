# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
  <a href="https://www.fiap.com.br/">
    <img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" width="40%">
  </a>
</p>

---

# 💧 Sistema de Irrigação Inteligente com ESP32

## 💻 Grupo: FarmTech Solutions

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

O projeto consiste em um **sistema de irrigação inteligente** utilizando o microcontrolador **ESP32**, com sensores físicos simulados na plataforma **Wokwi**. A proposta é monitorar condições ambientais como:

- Temperatura e umidade do ar (DHT22)
- Luminosidade (LDR)
- Umidade do solo (simulada)
- Acionamento de bomba via botão físico

A automação da bomba ocorre de forma manual (botão verde) ou via simulação de necessidade hídrica (sensores). Os dados capturados podem ser armazenados via script em **Python**, simulando a integração com um banco de dados relacional.

---

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

## 🔧 Como Executar o Código

### 🛠 Pré-requisitos:

- VS Code + Extensão [PlatformIO](https://platformio.org/install)
- Conta no [Wokwi](https://wokwi.com/)
- Python 3.11+
- Git instalado

### 🧪 Simulação no Wokwi

1. Abra o projeto no site [wokwi.com](https://wokwi.com/)
2. Faça upload do `diagram.json` e `wokwi.toml`
3. Insira o código `main.cpp` na IDE do Wokwi
4. Execute a simulação com o botão "Start Simulation"

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
