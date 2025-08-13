#!/usr/bin/env python3
# ====================================================
# Archivo     : image.py
# Descripción : Manejo de archivos AppImage
# Autor       : IxxeCODE
# Licencia    : GPL-3.0
# ====================================================

import os
import sys

__desc__ = "Gestiona archivos .AppImage: listarlos o crear accesos directos (.desktop)."

def run(args):
    if not args:
        print("Uso: ix image <archivo.AppImage> | list")
        return

    cmd = args[0].lower()
    if cmd == "list":
        list_appimages()
    else:
        create_desktop(args[0], args[1] if len(args) > 1 else None)

def list_appimages():
    cwd = os.getcwd()
    appimages = [f for f in os.listdir(cwd) if f.lower().endswith(".appimage")]
    if not appimages:
        print("No se encontraron archivos .AppImage en la carpeta actual.")
        return
    print("Archivos .AppImage encontrados:")
    for i, file in enumerate(appimages, 1):
        print(f"{i}. {file}")

def create_desktop(appimage_path, icon_path=None):
    appimage_path = os.path.abspath(appimage_path)

    if not os.path.exists(appimage_path):
        print(f"Error: no se encontró el archivo '{appimage_path}'.")
        return

    if not appimage_path.lower().endswith(".appimage"):
        print("Error: el archivo no es un .AppImage.")
        return

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
"""

    desktop_dir = os.path.expanduser("~/.local/share/applications")
    os.makedirs(desktop_dir, exist_ok=True)

    desktop_path = os.path.join(desktop_dir, f"{app_name}.desktop")
    with open(desktop_path, "w") as f:
        f.write(desktop_entry)

    os.chmod(appimage_path, 0o755)
    os.chmod(desktop_path, 0o755)

    print(f"[OK] Archivo .desktop creado en: {desktop_path}")
    print("Puedes buscarlo en tu lanzador de aplicaciones.")
