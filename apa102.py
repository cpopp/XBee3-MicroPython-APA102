# XBee3 MicroPython SPI Implementation for APA102
#
# Adjust constants SPI_CLK_PIN, SPI_MOSI_PIN, and LED_COUNT. 
# Switch "D2" to the pin you have hooked up to the CI line of the LEDs,
# and "D4" to the DI line of the LEDs.
#
# The loop at the bottom is just a sample that randomly sets the 
# LED colors with limited brightness to limit power use
# for long strips (a 64 LED strip stayed within 350 mA in my testing).

import time
import uos
import machine
from machine import Pin

SPI_CLK_PIN = Pin("D2", Pin.OUT)
SPI_MOSI_PIN = Pin("D4", Pin.OUT)
LED_COUNT = 64

def write_spi_byte(byte):
    for i in range(7, -1, -1):
        SPI_MOSI_PIN.value((byte >> i) & 1)
        SPI_CLK_PIN.value(0)
        SPI_CLK_PIN.value(1)

def write_start_frame():
    write_spi_byte(0)
    write_spi_byte(0)
    write_spi_byte(0)
    write_spi_byte(0)

def write_led_byte(red, green, blue):
    write_spi_byte(0xff)
    write_spi_byte(blue)
    write_spi_byte(green)
    write_spi_byte(red)

def write_end_frame():
    write_spi_byte(0xff)
    write_spi_byte(0xff)
    write_spi_byte(0xff)
    write_spi_byte(0xff)

while True:
    start = time.ticks_ms()
    write_start_frame()
    rnd_bytes = uos.urandom(LED_COUNT * 3)
    for i in range(LED_COUNT):
        red = rnd_bytes[i] % 20
        green = rnd_bytes[LED_COUNT + i] % 22
        blue = rnd_bytes[LED_COUNT + i] % 20
        write_led_byte(red, green, blue)
    write_end_frame()
    print("One Loop Took {} ms".format(time.ticks_ms()-start))
