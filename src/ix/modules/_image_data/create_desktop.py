#!/usr/bin/env python3
# ====================================================
# Archivo      : create_desktop.py
# Descripción  : Crea un archivo .desktop para un .AppImage
# Autor        : IxxeCODE
# Copyright    : 2025 IxxeCODE
# Licencia     : GNU General Public License v3 o superior
#               (ver archivo LICENSE para detalles completos)
# ====================================================

import os
from ix.modules._image_data.messages import ERROR_FILE_NOT_FOUND, ERROR_NOT_APPIMAGE, OK_DESKTOP_CREATED, INFO_SEARCH_LAUNCHER

def create_desktop(appimage_path, icon_path=None):
    """
    Crea un archivo .desktop para un archivo .AppImage dado.
    El archivo .desktop se guarda en el directorio de aplicaciones del usuario.
    También se asegura de que el archivo .AppImage sea ejecutable.
    """
    appimage_path = os.path.abspath(appimage_path)

    if not os.path.exists(appimage_path):
        print(ERROR_FILE_NOT_FOUND.format(appimage_path))
        return False

    if not appimage_path.lower().endswith(".appimage"):
        print(ERROR_NOT_APPIMAGE.format(appimage_path))
        return False

    app_name = os.path.splitext(os.path.basename(appimage_path))[0]
    icon_path = icon_path or "application-x-executable"

    desktop_entry = f"""[Desktop Entry]
Version=1.0
Type=Application
Name={app_name}
Comment=AppImage ejecutable
Exec="{appimage_path}"
Icon={icon_path}
Terminal=false
Categories=Utility;
X-Created-By=ixtools
"""

    desktop_dir = os.path.expanduser("~/.local/share/applications")
    os.makedirs(desktop_dir, exist_ok=True)

    desktop_path = os.path.join(desktop_dir, f"{app_name}.desktop")
    with open(desktop_path, "w") as f:
        f.write(desktop_entry)

    os.chmod(appimage_path, 0o755)
    os.chmod(desktop_path, 0o755)

    print(OK_DESKTOP_CREATED.format(desktop_path))
    print(INFO_SEARCH_LAUNCHER)
    return True
