#include <Arduino.h>
#include "DHT.h"

// Definindo os pinos dos sensores e relé
#define DHT_PIN 4       // Umidade do solo
#define DHT_TYPE DHT22  // Tipo de sensor DHT

#define P_SENSOR_PIN 12 // Fósforo (botão)
#define K_SENSOR_PIN 13 // Potássio (botão)
#define PH_SENSOR_PIN 34 // pH (LDR)
#define RELAY_PIN 25     // Relé (bomba)

DHT dht(DHT_PIN, DHT_TYPE);  // Instancia o sensor DHT

// Variáveis para armazenar os valores dos sensores
float humidity = 0.0;
int phosphorus = 0;
int potassium = 0;
int phValue = 0;

void setup() {
    Serial.begin(115200);  // Inicializa a comunicação serial
    pinMode(P_SENSOR_PIN, INPUT_PULLUP);  // Botão com pull-up
    pinMode(K_SENSOR_PIN, INPUT_PULLUP);  // Botão com pull-up
    pinMode(PH_SENSOR_PIN, INPUT);        // LDR para pH
    pinMode(RELAY_PIN, OUTPUT);           // Relé de controle da bomba
    dht.begin();                         // Inicializa o sensor DHT
    Serial.println("Sistema de Irrigação Inteligente Iniciado!");
}
void readSensors() {
    // Leitura da umidade do solo
    humidity = dht.readHumidity();
    if (isnan(humidity)) {
        Serial.println("Erro ao ler umidade!");
        humidity = -1;
    }

    // Leitura de fósforo e potássio (botão)
    phosphorus = !digitalRead(P_SENSOR_PIN); // Pressionado = presença (1)
    potassium = !digitalRead(K_SENSOR_PIN);  // Pressionado = presença (1)

    // Leitura do pH (LDR)
    phValue = analogRead(PH_SENSOR_PIN);

    // Exibindo as leituras no monitor serial
    Serial.print("Umidade: ");
    Serial.print(humidity);
    Serial.print("% | Fósforo: ");
    Serial.print(phosphorus);
    Serial.print(" | Potássio: ");
    Serial.print(potassium);
    Serial.print(" | pH: ");
    Serial.println(phValue);
}

//Função para controle da bomba
void controlPump() {
    // Lógica para controle da bomba que liga a bomba se a umidade estiver abaixo de 40%
    // ou se faltar fósforo/potássio
    if (humidity < 40 || phosphorus == 0 || potassium == 0) {
        digitalWrite(RELAY_PIN, HIGH);  // Liga a bomba
        Serial.println("Bomba ligada!");
    } else {
        digitalWrite(RELAY_PIN, LOW);  // Desliga a bomba
        Serial.println("Bomba desligada!");
    }
}
//Loop principal
void loop() {
    readSensors();  // Lê os sensores
    controlPump();  // Controla a bomba
    delay(2000);    // Aguarda 2 segundos antes da próxima leitura
}
