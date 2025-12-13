import RPi.GPIO as GPIO
import time

WATER_PIN = 17        # 第1顆水位偵測，BCM 17（實體 PIN 11）
BUZZER_PIN = 18       # 蜂鳴器，BCM 18（實體 PIN 12）
WATER2_PIN = 27       # 第2顆水位偵測，BCM 27（實體 PIN 13）
RELAY_PIN = 23        # 繼電器控制腳，BCM 23（實體 PIN 16）

GPIO.setmode(GPIO.BCM)

# 第1顆水位偵測：用內建拉高電阻
GPIO.setup(WATER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 第2顆水位偵測：同樣用內建拉高電阻
GPIO.setup(WATER2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 蜂鳴器：輸出腳
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.output(BUZZER_PIN, GPIO.LOW)  # 先關閉蜂鳴器

# 繼電器：輸出腳（假設低電位觸發）
'''GPIO.setup(RELAY_PIN, GPIO.OUT)'''
GPIO.setup(23, GPIO.OUT,initial=GPIO.HIGH)
GPIO.output(RELAY_PIN, GPIO.HIGH)  # 先預設為「不吸合、不通電」

def read_level():
    v = GPIO.input(WATER_PIN)
    # v == 1 表示「水高」
    return v  # 回傳 1 或 0

def read_level2():
    v = GPIO.input(WATER2_PIN)
    # v == 1 表示「水高」
    return v  # 回傳 1 或 0

try:
    while True:
        # 第1顆水位：決定蜂鳴器
        v1 = read_level()
        if v1 == 1:
            print("第1顆水位：水高")
            GPIO.output(BUZZER_PIN, GPIO.HIGH)   # 蜂鳴器叫
        else:
            print("第1顆水位：水低")
            GPIO.output(BUZZER_PIN, GPIO.LOW)    # 蜂鳴器關

        # 第2顆水位：決定繼電器
        v2 = read_level2()
        if v2 == 1:
            print("第2顆水位：水高 -> 繼電器通電（吸合）")
            GPIO.output(RELAY_PIN, GPIO.HIGH)     # 低電位觸發，讓繼電器吸合
        else:
            print("第2顆水位：水低 -> 繼電器斷電（釋放）")
            GPIO.output(RELAY_PIN, GPIO.LOW)    # 關閉繼電器

        print("----------")
        time.sleep(0.5)

finally:
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # 結束前確保繼電器不吸合
    GPIO.cleanup()
