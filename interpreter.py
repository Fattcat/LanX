# compiler/interpreter.py

import sys
import time
import re
import subprocess

board_type = None
com_port = None
compiled_cpp = []

def parse_directives(line):
    global board_type, com_port

    # BOARD TYPE
    match = re.match(r"#define\s+hardware\.arduino(.+?)", line)
    if match:
        board_type = match.group(1).strip()
        print(f"[INFO] Selected board: {board_type}")
        return True

    # COM PORT
    match = re.match(r"#define\s+set\.port(.+?)", line)
    if match:
        com_port = match.group(1).strip()
        print(f"[INFO] Selected COM port: {com_port}")
        return True

    return False

def run_code(lines):
    for line in lines:
        line = line.strip()

        # Ignoruj prázdne riadky alebo komentáre
        if not line or line.startswith("//"):
            continue

        # Parsovanie direktív (board, port)
        if line.startswith("#define"):
            if parse_directives(line):
                continue

        # SET PIN
        match = re.match(r"set pin (\w+) (high|low)", line)
        if match:
            pin, state = match.groups()
            compiled_cpp.append(f"  digitalWrite({pin}, {'HIGH' if state == 'high' else 'LOW'});")
            print(f"[SIM] Setting pin {pin} {state.upper()}")
            continue

        # WAIT
        match = re.match(r"wait (\d+)\s*(ms|s)?", line)
        if match:
            value, unit = match.groups()
            delay = int(value) * 1000 if unit == 's' else int(value)
            compiled_cpp.append(f"  delay({delay});")
            print(f"[SIM] Waiting {delay} ms")
            continue

        # REPEAT (simuluje loop)
        match = re.match(r"repeat(.*)?", line)
        if match:
            # repeat(infinite) alebo repeat(10)
            compiled_cpp.insert(0, "void loop() {")
            compiled_cpp.append("}")
            continue

        # Premenné napr. #define LED 13
        match = re.match(r"#define\s+(\w+)\s+(\d+)", line)
        if match:
            name, value = match.groups()
            compiled_cpp.insert(0, f"#define {name} {value}")
            continue

        print(f"[ERROR] Unknown command: {line}")

def build_and_upload():
    if not board_type or not com_port:
        print("[ERROR] Missing board or port definition.")
        return

    cpp_code = "#include <Arduino.h>\n\n"
    cpp_code += "\n".join(compiled_cpp)
    cpp_code = cpp_code.replace("void loop()", "void setup() {\n  // setup logic\n}\n\nvoid loop()")

    with open("main.ino", "w") as f:
        f.write(cpp_code)

    print("[INFO] Compiling and uploading...")

    # Spusti arduino-cli alebo avrdude podľa board_type
    if board_type == "uno":
        # Používame avrdude - nahráva .hex súbor
        subprocess.run([
            "arduino-cli", "compile", "--fqbn", "arduino:avr:uno", "main.ino"
        ])

        subprocess.run([
            "arduino-cli", "upload", "--fqbn", "arduino:avr:uno", "-p", com_port, "main.ino"
        ])
    else:
        print(f"[ERROR] Unsupported board: {board_type}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Použitie: python interpreter.py <súbor.lanx>")
        sys.exit(1)

    filepath = sys.argv[1]
    with open(filepath, "r") as f:
        code = f.readlines()

    run_code(code)
    build_and_upload()