int shock(String command);
int relay = D1;
void setup() {
  pinMode(relay, OUTPUT);
  // register the cloud function
  Particle.function("shock", shock);
  Particle.function("shockconst", shockconst);
}

void loop() {

}


int shock(String shockTime) {
  for ( int i = 1; i <= atoi(shockTime) ; i++ )
  {
    if (atoi(shockTime) >= 40) {
        return 0;
    }
    digitalWrite(relay, HIGH);
    delay(40);
    digitalWrite(relay, LOW);
    delay(20);
  }
  return 1;
}


int shockconst(String shockTime) {
    if (atoi(shockTime) >= 5000) { // bruv i don't want to get burned
        return 0;                  // fuck youuuuuuuuu
    }
    digitalWrite(relay, HIGH);
    delay(atoi(shockTime));
    digitalWrite(relay, LOW);
    return 1;
}