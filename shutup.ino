/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.
  This example code is in the public domain.
*/

#include <stdlib.h>

#define CHANGE_THRESHOLD 1

int last_sent_reading = -(CHANGE_THRESHOLD);

void setup() {
    // initialize the digital pin as an output.
    // Pin 13 has an LED connected on most Arduino boards:
    pinMode(13, OUTPUT);
    Serial.begin(921600);
}

void loop() {
    // digitalWrite(13, HIGH);   // set the LED on
    // delay(100);              // wait for a second
    // digitalWrite(13, LOW);    // set the LED off
    // delay(100);              // wait for a second
    // Serial.println("will it keep running");

    int reading = analogRead(0);
    if(abs(reading - last_sent_reading) > CHANGE_THRESHOLD) {
        Serial.println(reading);
        last_sent_reading = reading;
    }
}