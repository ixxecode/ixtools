#!/usr/bin/env python3
# ====================================================
# Archivo      : delete_desktop.py
# Descripción  : Elimina un archivo .desktop
# Autor        : IxxeCODE
# Copyright    : 2025 IxxeCODE
# Licencia     : GNU General Public License v3 o superior
#               (ver archivo LICENSE para detalles completos)
# ====================================================

import os
from ix.modules._image_data.messages import ERROR_FILE_NOT_FOUND, ERROR_NOT_DESKTOP, OK_DESKTOP_DELETED, ERROR_DELETE_FAILED

def delete_desktop(desktop_filename):
    """
    Elimina un archivo .desktop especificado del directorio de aplicaciones del usuario.
    Verifica si el archivo existe y si es un archivo .desktop antes de intentar eliminarlo.
    """
    desktop_dir = os.path.expanduser("~/.local/share/applications")
    desktop_path = os.path.join(desktop_dir, desktop_filename)

    if not os.path.exists(desktop_path):
        print(ERROR_FILE_NOT_FOUND.format(desktop_filename))
        return False
    
    if not desktop_filename.lower().endswith(".desktop"):
        print(ERROR_NOT_DESKTOP)
        return False

    try:
        os.remove(desktop_path)
        print(OK_DESKTOP_DELETED.format(desktop_filename))
        return True
    except OSError as e:
        print(ERROR_DELETE_FAILED.format(desktop_filename, e))
        return False
