#!/usr/bin/env python3
# ====================================================
# Archivo      : list_desktops.py
# Descripción  : Lista archivos .desktop creados por ixtools
# Autor        : IxxeCODE
# Copyright    : 2025 IxxeCODE
# Licencia     : GNU General Public License v3 o superior
#               (ver archivo LICENSE para detalles completos)
# ====================================================

import os
import sys
from ix.modules._image_data.messages import INFO_NO_DESKTOPS_FOUND, INFO_NO_IXTOOLS_DESKTOPS_FOUND, INFO_IXTOOLS_DESKTOPS_FOUND, ERROR_READ_FILE

def list_desktops():
    """
    Lista los archivos .desktop creados por 'ixtools' en el directorio de aplicaciones del usuario.
    Imprime los nombres de los archivos .desktop o un mensaje si no se encuentran.
    """
    desktop_dir = os.path.expanduser("~/.local/share/applications")
    if not os.path.exists(desktop_dir):
        print(INFO_NO_DESKTOPS_FOUND)
        return

    desktop_files = []
    for f in os.listdir(desktop_dir):
        if f.lower().endswith(".desktop"):
            file_path = os.path.join(desktop_dir, f)
            try:
                with open(file_path, "r") as desktop_file:
                    content = desktop_file.read()
                    if "X-Created-By=ixtools" in content:
                        desktop_files.append(f)
            except Exception as e:
                print(ERROR_READ_FILE.format(f, e), file=sys.stderr)

    desktop_files.sort() # Ordenar alfabéticamente

    if not desktop_files:
        print(INFO_NO_IXTOOLS_DESKTOPS_FOUND)
        return

    print(INFO_IXTOOLS_DESKTOPS_FOUND)
    for i, file in enumerate(desktop_files, 1):
        print(f"{i}. {file}")
