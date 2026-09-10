#include <Servo.h>
#include <Firmata.h>

Servo servo[6];
int default_angle[6] = {75, 75, 75, 75, -75, 60};
int variable[6] = {0, 0, 0, 0, 0, 0};
byte angle[6];
byte pre_angle[6];

long t = millis();

void setup() {
    Serial.begin(115200);
    servo[0].attach(3);
    servo[1].attach(5);
    servo[2].attach(6);
    servo[3].attach(9);
    servo[4].attach(10);
    servo[5].attach(11);

    for (size_t i = 0; i < 6; i++) {
        servo[i].write(default_angle[i]);
    }
}

void loop() {
    // Envoyer un signal "1" pour indiquer que l'Arduino est prêt
    Serial.println("1");

    // Si des données sont disponibles depuis Python
    if (Serial.available()) {
        Serial.readBytes(angle, 6);
        for (size_t i = 0; i < 6; i++) {
            if (angle[i] != pre_angle[i] && angle[i] > pre_angle[i]) {
                for (variable[i] = pre_angle[i]; variable[i] < angle[i]; variable[i]++) {
                    servo[i].write(variable[i]);
                    pre_angle[i] = variable[i];
                }
            } else if (angle[i] != pre_angle[i] && angle[i] < pre_angle[i]) {
                for (variable[i] = pre_angle[i]; variable[i] > angle[i]; variable[i]--) {
                    servo[i].write(variable[i]);
                    pre_angle[i] = variable[i];
                }
            }
        }
        t = millis();
    }

    if (millis() - t > 1000) {
        for (size_t i = 0; i < 6; i++) {
            servo[i].write(variable[i]);
        }
    }
}