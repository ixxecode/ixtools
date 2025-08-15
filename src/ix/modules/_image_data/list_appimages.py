#!/usr/bin/env python3
# ====================================================
# Archivo      : list_appimages.py
# Descripción  : Lista archivos .AppImage en el directorio actual
# Autor        : IxxeCODE
# Copyright    : 2025 IxxeCODE
# Licencia     : GNU General Public License v3 o superior
#               (ver archivo LICENSE para detalles completos)
# ====================================================

import os
from ix.modules._image_data.messages import INFO_NO_APPIMAGES_FOUND, INFO_APPIMAGES_FOUND

def list_appimages():
    """
    Lista todos los archivos .AppImage encontrados en el directorio de trabajo actual.
    Imprime los nombres de los archivos .AppImage o un mensaje si no se encuentran.
    """
    cwd = os.getcwd()
    appimages = [f for f in os.listdir(cwd) if f.lower().endswith(".appimage")]
    if not appimages:
        print(INFO_NO_APPIMAGES_FOUND)
        return
    print(INFO_APPIMAGES_FOUND)
    for i, file in enumerate(appimages, 1):
        print(f"{i}. {file}")
