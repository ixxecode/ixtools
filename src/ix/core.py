#!/usr/bin/env python3
# ====================================================
# Archivo     : core.py
# Descripción : Punto de entrada principal de ixtools
# Autor       : IxxeCODE
# Licencia    : GPL-3.0
# ====================================================

import sys
import importlib

# Lista de módulos disponibles y su descripción
COMMANDS = {
    "list": "Muestra todas las herramientas disponibles.",
    "image": "Gestiona y ejecuta archivos AppImage."
}

def main():
    if len(sys.argv) < 2:
        print("Uso: ix <comando> [opciones]")
        print("\nComandos disponibles:")
        for cmd, desc in COMMANDS.items():
            print(f"  {cmd:<8} {desc}")
        sys.exit(1)

    command = sys.argv[1]

    if command not in COMMANDS:
        print(f"Error: comando '{command}' no reconocido.")
        print("Usa 'ix list' para ver los comandos disponibles.")
        sys.exit(1)

    try:
        module = importlib.import_module(f"{__package__}.modules.{command}")
        module.run(sys.argv[2:])
    except ImportError as e:
        print(f"Error: no se pudo cargar el módulo '{command}'.\n{e}")


if __name__ == "__main__":
    main()
