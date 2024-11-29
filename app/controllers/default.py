from urllib.request import urlopen
import RPi.GPIO as gpio
import time as delay
import requests
from app import app
from flask import render_template

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

# Pinos GPIO
ledVermelho, ledVerde = 11, 12
pin_e = 16
pin_t = 15
lixeira_v = 20

statusVermelho = ""
statusVerde = ""

# Configuração dos pinos
gpio.setup(ledVermelho, gpio.OUT)
gpio.setup(ledVerde, gpio.OUT)
gpio.output(ledVermelho, gpio.LOW)
gpio.output(ledVerde, gpio.LOW)

gpio.setup(pin_t, gpio.OUT)
gpio.setup(pin_e, gpio.IN)

# URL do ThingSpeak
urlBase = 'https://api.thingspeak.com/update?api_key='
keyWrite = 'WE1VA2D3TD10APHF'
keyRead = 'HYYY1MYZGQXMCYWH'
sensorTampa = '&field1='
sensorDistancia = '&field2='

def enviaDados(tampa, lixeira):
    """
    Função para enviar dados para o ThingSpeak.
    """
    urlDados = (urlBase + keyWrite + sensorTampa + tampa + sensorDistancia + lixeira)
    retorno = requests.post(urlDados)
    if retorno.status_code == 200:
        print('Dados enviados com sucesso')
    else:
        print(f'Erro ao enviar dados: {retorno.status_code}')
        delay.sleep(20)

def lixeira():
    """
    Função para calcular a ocupação da lixeira com base no sensor de distância.
    """
    gpio.output(pin_t, True)
    delay.sleep(0.000001)
    gpio.output(pin_t, False)

    tempo_i = delay.time()
    tempo_f = delay.time()

    while gpio.input(pin_e) == False:
        tempo_i = delay.time()
    while gpio.input(pin_e) == True:
        tempo_f = delay.time()

    temp_d = tempo_f - tempo_i
    distancia = (temp_d * 34300) / 2

    ocupacao_l = (distancia / lixeira_v) * 100
    ocupacao_f = 100 - ocupacao_l
    ocupacao_lixeira = ('{0:0.0f}%'.format(ocupacao_f))

    # Garante que a ocupação esteja entre 0 e 100
    ocupacao = min(max(ocupacao_f, 0), 100)
    
    return ocupacao

def status_led_vermelho():
    """
    Retorna o status do LED vermelho (ON ou OFF).
    """
    if gpio.input(ledVermelho) == 1:
        return 'LED vermelho ON'
    else:
        return 'LED vermelho OFF'

def status_led_verde():
    """
    Retorna o status do LED verde (ON ou OFF).
    """
    if gpio.input(ledVerde) == 1:
        return 'LED verde ON'
    else:
        return 'LED verde OFF'

@app.route("/")
def index():
    """
    Rota principal que exibe o status dos LEDs e a ocupação da lixeira.
    """
    gpio.output(ledVerde, gpio.LOW)
    gpio.output(ledVermelho, gpio.LOW)
    templateData = {
        'ledRed': status_led_vermelho(),
        'ledGreen': status_led_verde(),
        'lixeira': lixeira()
    }
    return render_template('index.html', **templateData)

@app.route("/tampa/<action>")
def led(action):
    """
    Controla a abertura e o fechamento da tampa e acende o LED correspondente com base na ocupação.
    """
    gpio.output(ledVerde, gpio.LOW)
    gpio.output(ledVermelho, gpio.LOW)
    ocupacao = int(lixeira())
    print(ocupacao)

    if action == 'abrir':
        for i in range(2):
            gpio.output(ledVerde, gpio.HIGH)
            delay.sleep(0.5)
            gpio.output(ledVerde, gpio.LOW)
            delay.sleep(0.5)

        if ocupacao < 50:
            gpio.output(ledVerde, gpio.HIGH)
        else:
            gpio.output(ledVermelho, gpio.HIGH)

        enviaDados('1', str(ocupacao))

    if action == 'fechar':
        for i in range(2):
            gpio.output(ledVermelho, gpio.HIGH)
            delay.sleep(0.5)
            gpio.output(ledVermelho, gpio.LOW)
            delay.sleep(0.5)

        if ocupacao < 50:
            gpio.output(ledVerde, gpio.HIGH)
        else:
            gpio.output(ledVermelho, gpio.HIGH)

        enviaDados('0', str(ocupacao))

    templateData = {
        'ledRed': status_led_vermelho(),
        'ledGreen': status_led_verde(),
        'lixeira': lixeira()
    }
    return render_template('index.html', **templateData)

@app.route("/distancia")
def conf_distancia():
    """
    Rota para mostrar a ocupação da lixeira.
    """
    templateData = {
        'ocup_lixeira': lixeira()
    }
    return render_template('index.html', **templateData)
