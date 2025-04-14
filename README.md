<div align="center">LanX</div>

**LanX** is a lightweight, hardware-focused programming language created for working with microcontrollers like Arduino. It aims for simplicity, clarity, and native support for hardware-level operations such as GPIO, I2C, Serial, and more.

---

## Table of Contents

- [Features](#features)
- [Compatible Boards](#compatible-boards)
- [Set Board Type](#set-board-type)
- [Code Example](#code-example)
- [Install](#install)
  - [Linux (Terminal)](#linux-terminal)
  - [Windows 10 (CMD)](#windows-10-cmd)
- [VS Code Extension](#vs-code-extension)
- [Usage](#usage)
- [Planned Features](#planned-features)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- Simple syntax, optimized for embedded scripting
- Built-in commands for GPIO, delays, display output, etc.
- Fast transpilation to C or machine code
- Designed for small and real-time hardware applications
- Includes VS Code syntax highlighting and snippets

---
## Compatible Boards
- arduino Uno, nano, micro, esp32, esp8266
### Set Board Type
- for uno, micro, mega2560
  - #define hardware.arduino(uno)
- for esp boards
  - #define hardware.esp(32)
  - #define hardware.esp(8266)

---
## Code Example

```
// define your board (Uno, esp32, esp8266,)
// example for Arduino Uno board
#define hardware.arduino(uno)
// Blink LED 13

#define LED 13
set pin LED high
wait 500 ms
set pin LED low
wait 500 // time 0.5 seconds
repeat(infinite) // or repeat(10) for 10 times

```
## Run
```
lanx myCode.lanx
```

## Install
``` git clone https://github.com/Fattcat/lanx.git
cd lanx
chmod +x install.sh
./install.sh
```
## Support me with star
