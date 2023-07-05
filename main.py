import machine
import utime
import re
import urequests

short_dur = 500
long_dur = 3000

key_f = False
ctrl_f = False
key_s = 0
ctrl_s = 0

morse = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '-----': '0'
}
inv_morse = {v: k for k, v in morse.items()}
morse_in = []

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36', 
}


def key_interrupt(pin):
    global key_f, key_s
    if not pin.value():  # key pressed
        key_f = True
        key_s = utime.ticks_ms()
    else:  # key released
        if key_f:
            key_f = False
            key_dur = utime.ticks_diff(utime.ticks_ms(), key_s)
            if key_dur < short_dur:
                morse_in.append('.')
                haptic(200, 1023, 1000)  # duration, duty (0-1023), frequency
                print('.')
            elif key_dur >= short_dur:
                morse_in.append('-')
                haptic(500, 1023, 1000)
                print('-')


def ctrl_interrupt(pin):
    global ctrl_f, ctrl_s, morse_in
    if not pin.value():  # ctrl pressed
        ctrl_f = True
        ctrl_s = utime.ticks_ms()
    else:  # ctrl released
        if ctrl_f:
            ctrl_f = False
            ctrl_dur = utime.ticks_diff(utime.ticks_ms(), ctrl_s)
            if ctrl_dur <= short_dur:  # '  ' = '/'
                print(' ')
                haptic(200, 1023, 1000)
                morse_in.append(' ')
            elif ctrl_dur > short_dur and ctrl_dur < long_dur:
                print('SUBMIT')
                haptic(500, 1023, 1000)
                source = transcode(''.join(morse_in), True)
                if source is not None:
                    print('translate')
                    target = translate('en', 'fr', source)
                    print(f'{source} --> {target}')
                    res = transcode(target, False)
                    print(f'{target} --> {res}')
                    vibrate(res, 1023, 1000)
                    morse_in = []
                else:
                    print('raise error')
                    #raise_vib(404)
            elif ctrl_dur >= long_dur:
                print('CLEAR')
                vibrate(1000, 1023, 1000)
                morse_in = []


def haptic(dur, duty, freq):  # int, int, int
    led.value(0)
    vib_pwm.freq(freq)
    vib_pwm.duty(duty)
    start = utime.ticks_ms()
    while utime.ticks_diff(utime.ticks_ms(), start) < dur:
        pass
    led.value(1)
    vib_pwm.duty(0)


def vibrate(job, duty, freq):  # str, int, int
    print(job)
    for dd in job:
        if dd == '.':
            led.value(0)
            vib_pwm.duty(duty)
            utime.sleep_ms(200)
        elif dd == '-':
            led.value(0)
            vib_pwm.duty(duty)
            utime.sleep_ms(500)
        elif dd == ' ':
            led.value(0)
            vib_pwm.duty(0)
            utime.sleep_ms(500)
            
        led.value(1)
        vib_pwm.duty(0)
        utime.sleep_ms(100)
            

def transcode(job, codec):  # str, bool
    # '.... ..  -.. .- ...- .'
    if job:
        if codec:
            print('decode')
            fr = []
            for word in job.split('  '):  # ['.... ..', '-.. .- ...- .']
                for char in word.split(' '):  # ['....', '..']
                    if char:
                        res = morse.get(char)
                        if res:
                            fr.append(res)
                        else:
                            print(f'KeyError: {char}')
                            return None
                    else:
                        print('EMPTY')
                        return None
                fr.append(' ')
            #print(''.join(fr))
            #return ''.join(fr)
        elif not codec:
            print('encode')
            fr = []
            for word in job.split(' '):
                #print(word)
                for char in word:
                    #print(char)
                    res = inv_morse.get(char.upper())
                    if res:
                        fr.append(res)
                    else:
                        print(f'KeyError: {char}')
                        continue
                    fr.append(' ')
                fr.append(' ')
    else:
        print('EMPTY')
        return None
    
    return ''.join(fr)


def translate(sl, tl, fuck):  # str, str, str
    #print(fuck)
    url = f'https://translate.google.com/m?sl={sl}&tl={tl}&q={fuck}'
    #print(url)
    response = urequests.get(url, headers=headers).text
    #print(response)
    res = re.compile(r'<div class="result-container">(.*?)</div>').search(str(response))

    return res.group(1)


# set up pins and handlers
key_p = machine.Pin(19, machine.Pin.IN, machine.Pin.PULL_UP)
key_p.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=key_interrupt)
ctrl_p = machine.Pin(23, machine.Pin.IN, machine.Pin.PULL_UP)
ctrl_p.irq(trigger=machine.Pin.IRQ_FALLING | machine.Pin.IRQ_RISING, handler=ctrl_interrupt)

led = machine.Pin(5, machine.Pin.OUT)
led.value(1)

vib_pwm = machine.PWM(machine.Pin(12))
vib_pwm.freq(1000)
vib_pwm.duty(0)
