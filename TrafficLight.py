from gpiozero import LED, TrafficLights, Button, Buzzer
from time import sleep

traffic_light = TrafficLights(21,20,12)
button = Button(26)
buzzer = Buzzer(1)

is_pressed = False
def pressed():
    if traffic_light.green.is_lit:
        global is_pressed
        is_pressed = True
        sleep(2)
        traffic_light.green.off()
        traffic_light.yellow.on()
        sleep(3)
        traffic_light.yellow.off()
        traffic_light.red.on()
        for i in range(4):
            buzzer.on()
            sleep(0.5)
            buzzer.off()
            sleep(0.5)
        sleep(2)
        traffic_light.red.off()
        
def run_lights():
    global is_pressed
    while True:
        button.when_pressed = pressed
        traffic_light.red.off()
        traffic_light.green.on()
        for i in range(10):
            sleep(1)
            if is_pressed:
                button.when_pressed = None
                sleep(8)
                break
        if is_pressed:
            is_pressed = False
            continue
        traffic_light.green.off()
        traffic_light.yellow.on()
        sleep(3)
        traffic_light.yellow.off()
        traffic_light.red.on()
        sleep(6)
        traffic_light.red.off()

def main():
    run_lights()
    
if __name__ == '__main__':
    main()
