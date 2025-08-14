#!/usr/bin/env python3
# ====================================================
# Archivo      : core.py
# Descripción  : Punto de entrada principal de IxTools
# Autor        : IxxeCODE
# Copyright    : 2025 IxxeCODE
# Licencia     : GNU General Public License v3 o superior
#               (ver archivo LICENSE para detalles completos)
# ====================================================

__version__ = "v2.0.0"

import sys
import importlib.util
import os

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--version":
        print(f"ixtools version {__version__}")
        sys.exit(0)

    modules_dir = os.path.join(os.path.dirname(__file__), "modules")
    available_modules = {}

    for filename in os.listdir(modules_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module_path = os.path.join(modules_dir, filename)
            try:
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                desc = getattr(module, "__desc__", "Sin descripción.")
                version = getattr(module, "__version__", "N/A")
                available_modules[module_name] = {"desc": desc, "version": version}
            except Exception as e:
                print(f"Advertencia: No se pudo cargar el módulo '{module_name}': {e}", file=sys.stderr)

    if len(sys.argv) < 2:
        print("Uso: ix <comando> [opciones]")
        print("\nMódulos disponibles:")
        for cmd, info in available_modules.items():
            print(f"  {cmd:<10} {info['version']:<5} {info['desc']}")
        sys.exit(1)

    command = sys.argv[1]

    if command not in available_modules:
        print(f"Error: comando '{command}' no reconocido.")
        print("Usa 'ix' para ver los módulos disponibles.")
        sys.exit(1)

    try:
        module = importlib.import_module(f"{__package__}.modules.{command}")
        
        # Si no hay subcomandos, mostrar la versión y la ayuda del módulo
        if len(sys.argv) == 2:
            module_info = available_modules[command]
            print(f"Módulo {command} versión {module_info['version']}")
            module.run([]) # Llama a run con una lista vacía para activar la ayuda
        else:
            module.run(sys.argv[2:])
    except ImportError as e:
        print(f"Error: no se pudo cargar el módulo '{command}'.\n{e}", file=sys.stderr)
    except Exception as e:
        print(f"Error al ejecutar el módulo '{command}': {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
