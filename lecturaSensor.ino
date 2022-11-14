int sensor=A0; // Define el pin al que está conectada la salida del sensor
int lectura; // Crea variable para almacenar la lectura del pin
float voltaje; // Crea variable para almacenar la diferencia de potencial eléctrico 
int espera=500; // Define el tiempo entre lecturas (en ms)
const int baud=9600; // Tasa de baudios
const int maxAnalogico=1023; // Lectura máxima del pin analógico, definida por Arduino
const int Vcc=5000; // Fuente de alimentación de 5V (5000 mV)

void setup() {
  Serial.begin(baud); 
  pinMode(sensor, INPUT);
}

void loop() {
   lectura = analogRead(sensor);  // Lee la entrada y almacena la lectura (valor entero entre 0 y 1023)
   voltaje = map(lectura, 0, maxAnalogico, 0, Vcc);    // Convierte lectura a un valor entre 0 mV y 5000 mV
   Serial.println(voltaje);   // Imprime valor 
   delay(espera);   //  Tiempo de espera entre lecturas
}
