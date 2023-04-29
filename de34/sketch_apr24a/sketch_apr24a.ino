void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int val=0;
  val=analogRead(1);
  Serial.println(val);
  delay(5000);//5000ms=5秒　ごとに送信。【注意】サーバーに負荷がかかるので5000より小さい値は設定しないでください。
//実装する際は可能な限り大きな数字にしてください。
}
