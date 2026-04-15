# Orbit Revision E Board

This directory is intended for the PX4 board port for the Orbit revision E flight controller.

## Summary

- Target hardware is an STM32H743-based board.
- Port, GPIO, and pin values should be taken from the OrbitTest repository, as that implementation is known to work.
- The remaining bring-up work is to map the onboard peripherals to the appropriate PX4 and NuttX drivers where support already exists.

## Porting Notes

Use the OrbitTest repository as the hardware reference for:

- GPIO assignments
- SPI buses and chip selects
- I2C buses
- UART / serial ports
- ADC channels
- PWM outputs
- CAN pins
- USB, LEDs, power control, and other board-specific signals

## PX4 Integration Work

For each onboard peripheral, identify and enable the corresponding PX4 driver if it is supported, for example:

- IMU / gyro / accelerometer
- magnetometer
- barometer
- FRAM / flash / storage devices
- RC input
- power monitoring
- CAN peripherals
- GPS
- buzzer, LEDs, and other auxiliary devices

Unsupported peripherals should be documented clearly as part of the board bring-up effort.
