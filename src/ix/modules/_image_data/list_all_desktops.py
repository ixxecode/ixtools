#!/usr/bin/env python3
# ====================================================
# Archivo      : list_all_desktops.py
# Descripción  : Lista todos los archivos .desktop del usuario
# Autor        : IxxeCODE
# Copyright    : 2025 IxxeCODE
# Licencia     : GNU General Public License v3 o superior
#               (ver archivo LICENSE para detalles completos)
# ====================================================

import os
import sys
from ix.modules._image_data.messages import INFO_NO_DESKTOPS_FOUND, INFO_ALL_DESKTOPS_FOUND, ERROR_READ_FILE

def list_all_desktops():
    """
    Lista todos los archivos .desktop del usuario, incluyendo los creados por 'ixtools' y los del sistema.
    Imprime los nombres de los archivos .desktop y su origen (ixtools/system) o un mensaje si no se encuentran.
    """
    desktop_dir = os.path.expanduser("~/.local/share/applications")
    if not os.path.exists(desktop_dir):
        print(INFO_NO_DESKTOPS_FOUND)
        return

    all_desktop_files = []
    for f in os.listdir(desktop_dir):
        if f.lower().endswith(".desktop"):
            file_path = os.path.join(desktop_dir, f)
            try:
                with open(file_path, "r") as desktop_file:
                    content = desktop_file.read()
                    if "X-Created-By=ixtools" in content:
                        all_desktop_files.append((f, "[ixtools]"))
                    else:
                        all_desktop_files.append((f, "[system]"))
            except Exception as e:
                print(ERROR_READ_FILE.format(f, e), file=sys.stderr)

    all_desktop_files.sort(key=lambda x: x[0]) # Ordenar alfabéticamente por nombre de archivo

    if not all_desktop_files:
        print(INFO_NO_DESKTOPS_FOUND)
        return

    print(INFO_ALL_DESKTOPS_FOUND)
    for i, (file, origin) in enumerate(all_desktop_files, 1):
        print(f"{i}. {file} {origin}")
