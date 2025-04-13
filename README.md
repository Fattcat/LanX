<div align="center">LanX</div>

**LanX** is a lightweight, hardware-focused programming language created for working with microcontrollers like Arduino. It aims for simplicity, clarity, and native support for hardware-level operations such as GPIO, I2C, Serial, and more.

---

## Table of Contents

- [Features](#features)
- [Code Example](#code-example)
- [Installation](#installation)
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

## Code Example

```lanx
// Blink LED 13
set pin 13 high
wait 500 ms
set pin 13 low
wait 500 ms
repeat
```

## Install
``` git clone https://github.com/Fattcat/lanx.git
cd lanx
chmod +x install.sh
./install.sh ```

## Support me with star
