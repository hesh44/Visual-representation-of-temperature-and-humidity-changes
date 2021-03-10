import time, json
# Biblioteka za senzor
import Adafruit_DHT
import RPi.GPIO as GPIO
from flask_cors import CORS
# Flask web framework
from flask import Flask
app = Flask(__name__)
CORS(app)

# Funkcija koja manipulise LED lampicom u zavisnoti od temperature
# Prima tip senzora, pin koji salje vrednosti, kao i tri pina koji se odnose na boje
def funkcija(sensor, DHT_PIN, red, green, blue):
    humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_PIN)
    print("Vlaznost "+ str(humidity)+" Temperatura "+ str(temperature))
    if temperature==None:
        print("ne radi")
        GPIO.output(green, 1)
        GPIO.output(blue, 1)
        GPIO.output(red, 1)
    elif temperature <= 40.0 :
        print("blue")
        GPIO.output(blue, 1)
        GPIO.output(green,0)
        GPIO.output(red, 0)
    elif temperature >= 47.0:
        print("red")
        GPIO.output(red, 1)
        GPIO.output(green,0)
        GPIO.output(blue, 0)
    else:
        print("white")
        GPIO.output(green, 1)
        GPIO.output(blue, 1)
        GPIO.output(red, 1)

# Home ruta gde je lampica ugasena
@app.route('/')
def home():
    red = 27
    green = 22
    blue = 17
    GPIO.output(green,0)
    GPIO.output(blue, 0)
    GPIO.output(red, 0)
    GPIO.cleanup()

# Ruta koja setuje nacin na koji citamo pinove sa RPi-a i koja pokrece funkciju paljenja
@app.route('/uredjajON')
def upali():
    sensor = Adafruit_DHT.DHT11
    DHT_PIN = 4

    GPIO.setmode(GPIO.BCM) 
    red = 27
    green = 22
    blue = 17

    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(blue, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)
    while True:
        funkcija(sensor, DHT_PIN, red, green, blue)

#Ruta koja gasi uredjaj
@app.route('/uredjajOFF')
def hello():
    red = 27
    green = 22
    blue = 17

    GPIO.output(green,0)
    GPIO.output(blue, 0)
    GPIO.output(red, 0)
    GPIO.cleanup()
    return "Uredjaj ugasen"

#Ruta koja pali treperenje
@app.route('/treperenjeON')
def upaliTreperenje():
    sensor = Adafruit_DHT.DHT11
    DHT_PIN = 4

    GPIO.setmode(GPIO.BCM) 
    red = 27
    green = 22
    blue = 17

    GPIO.setup(red, GPIO.OUT)
    GPIO.setup(blue, GPIO.OUT)
    GPIO.setup(green, GPIO.OUT)
    # Petlja koja omogucava treperenje u intervalu od 1 sekunde
    while True:
        funkcija(sensor, DHT_PIN, red, green, blue)
        time.sleep(1)
        GPIO.output(green,0)
        GPIO.output(blue, 0)
        GPIO.output(red, 0)
        time.sleep(1)

# Ruta koja uzima vrednosti i koja se koristi kako bi menjali boje okvira polja preko ajaxa
@app.route('/getVrednosti')
def getVrednosti():
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
    return json.dumps({"vlaznost":humidity,"temperatura":temperature})
        

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')


