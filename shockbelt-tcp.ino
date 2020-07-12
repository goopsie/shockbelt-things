// Only beatsaber-shockbelt.py uses this, everything else uses shockbelt-curl.ino

TCPClient client;                            // Create TCP Client object
byte server_ip[] = { 192, 168, 0, 4 };       // IP Address of server
int  server_port = 54027;                    // port to connect on...
String message   = "";                       // goopsie was here
int relay = D1;

void setup() 
{
  pinMode(relay, OUTPUT);
  Serial.begin(9600);
  // waitFor(Serial.isConnected, 30000);
  Serial.println("Serial Connected.");    // you can't prove it's not connected

  while(!client.connect(server_ip, server_port)) {
    Serial.println("Server connection failed. Trying again...");
  }
  Serial.println("Connected to TCP Server."); 
}
 
void loop() {
  while(client.available()) {
    char c = client.read();
    message = message + c;
  }

  if(!client.available() && message != "") {
    Serial.println(message);
    if(message == "ping" || message == "ping\n") {
      client.print("pong");
    }
    
    if(message == "shock") {             // use this, it's static & less dangerous
      Serial.println("Shocking time aaa");
      digitalWrite(relay, HIGH);
      delay(500);
      digitalWrite(relay, LOW);
      Serial.println("Done shocking");
    } else if(message == "shockon"  ) {  // Don't use these (unless you're james)
        digitalWrite(relay, HIGH);
    } else if (message == "shockoff") {  // Don't use these (unless you're james)
        digitalWrite(relay, LOW);        // stop the agony
    }
    message = "";
  }

  if(!client.connected()) {
    Serial.println("Client Disconnected.");
    client.stop();
                                        // try to connect again
    while(!client.connect(server_ip, server_port)) {
      client.stop();
      Serial.println("Server connection failed. Trying again...");
    }
    Serial.println("Connected to TCP Server.");
  }
}