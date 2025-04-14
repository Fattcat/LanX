# compiler/interpreter.py

import sys
import time
import re

def run_code(lines):
    for line in lines:
        line = line.strip()

        # Ignoruj komentáre
        if not line or line.startswith("//"):
            continue

        # SET PIN
        match = re.match(r"set pin (\d+) (high|low)", line)
        if match:
            pin, state = match.groups()
            print(f"[SIM] Setting pin {pin} {state.upper()}")
            continue

        # WAIT
        match = re.match(r"wait (\d+)\s*(ms|s)?", line)
        if match:
            value, unit = match.groups()
            value = int(value)
            if unit == "s":
                time.sleep(value)
            else:
                time.sleep(value / 1000)
            print(f"[SIM] Waiting {value} {unit or 'ms'}")
            continue

        # REPEAT (simulate infinite loop)
        if line == "repeat":
            print("[SIM] Repeating...")
            run_code(lines)
            break

        print(f"[ERROR] Unknown command: {line}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <sourcefile.nzj>")
        sys.exit(1)

    filepath = sys.argv[1]
    with open(filepath, "r") as f:
        code = f.readlines()

    run_code(code)
