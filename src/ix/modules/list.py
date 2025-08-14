#!/usr/bin/env python3
# ====================================================
# Archivo      : list.py
# Descripción  : Lista todas las herramientas de Ixtools
# Autor        : IxxeCODE
# Copyright    : 2025 IxxeCODE
# Licencia     : GNU General Public License v3 o superior
#               (ver archivo LICENSE para detalles completos)
# ====================================================

__version__ = "v2.0.0"
__desc__ = "Herramienta para ver todos los comandos de los módulos/herramientas disponibles en Ixtools"
__author__ = "IxxeCODE"

import os
import importlib.util

def run(args):
    print("Herramientas disponibles:")
    
    # Obtener la ruta del directorio actual (donde se encuentra list.py)
    modules_dir = os.path.dirname(__file__)
    
    # Listar todos los archivos en el directorio de módulos
    for filename in os.listdir(modules_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # Eliminar la extensión .py
            module_path = os.path.join(modules_dir, filename)
            
            try:
                spec = importlib.util.spec_from_file_location(module_name, module_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                doc_string = getattr(module, "__desc__", "Sin descripción disponible.")
                version_string = getattr(module, "__version__", "N/A")
                print(f"- {module_name:<10} | {version_string:<7} → {doc_string}")
            except Exception as e:
                print(f"- {module_name:<10} | N/A     → Error al cargar o leer módulo: {e}")
