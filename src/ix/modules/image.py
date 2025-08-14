#!/usr/bin/env python3
# ====================================================
# Archivo      : image.py
# Descripción  : Manejo de archivos AppImage
# Autor        : IxxeCODE
# Copyright    : 2025 IxxeCODE
# Licencia     : GNU General Public License v3 o superior
#               (ver archivo LICENSE para detalles completos)
# ====================================================

__version__ = "v1.1.0"
__desc__ = "Gestiona archivos .AppImage para listarlos o crear accesos directos (.desktop) y configurarlos."
__author__ = "IxxeCODE"

import os
import sys

def run(args):
    if not args or args[0] in ["--help", "-h"]:
        print_help()
        return

    cmd = args[0].lower()
    if cmd == "list":
        list_appimages()
    elif cmd == "-d":
        if len(args) == 1:
            list_desktops()
        elif len(args) == 2 and args[1].lower() == "delete":
            print("Uso: ix image -d delete <archivo.desktop>")
        elif len(args) == 3 and args[1].lower() == "delete":
            delete_desktop(args[2])
        else:
            print("Uso: ix image -d [delete <archivo.desktop>]")
    elif cmd == "-d-s":
        list_all_desktops()
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

def list_desktops():
    desktop_dir = os.path.expanduser("~/.local/share/applications")
    if not os.path.exists(desktop_dir):
        print("No se encontraron archivos .desktop.")
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
                print(f"Advertencia: No se pudo leer el archivo {f}: {e}", file=sys.stderr)

    desktop_files.sort() # Ordenar alfabéticamente

    if not desktop_files:
        print("No se encontraron archivos .desktop creados por ixtools.")
        return

    print("Archivos .desktop creados por ixtools:")
    for i, file in enumerate(desktop_files, 1):
        print(f"{i}. {file}")

def list_all_desktops():
    desktop_dir = os.path.expanduser("~/.local/share/applications")
    if not os.path.exists(desktop_dir):
        print("No se encontraron archivos .desktop.")
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
                print(f"Advertencia: No se pudo leer el archivo {f}: {e}", file=sys.stderr)

    all_desktop_files.sort(key=lambda x: x[0]) # Ordenar alfabéticamente por nombre de archivo

    if not all_desktop_files:
        print("No se encontraron archivos .desktop.")
        return

    print("Todos los archivos .desktop encontrados:")
    for i, (file, origin) in enumerate(all_desktop_files, 1):
        print(f"{i}. {file} {origin}")

def delete_desktop(desktop_filename):
    desktop_dir = os.path.expanduser("~/.local/share/applications")
    desktop_path = os.path.join(desktop_dir, desktop_filename)

    if not os.path.exists(desktop_path):
        print(f"Error: no se encontró el archivo '{desktop_filename}'.")
        return
    
    if not desktop_filename.lower().endswith(".desktop"):
        print("Error: el archivo especificado no es un .desktop.")
        return

    try:
        os.remove(desktop_path)
        print(f"[OK] Archivo .desktop '{desktop_filename}' eliminado.")
    except OSError as e:
        print(f"Error al eliminar el archivo '{desktop_filename}': {e}")

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
X-Created-By=ixtools
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

def print_help():
    print("""
Uso: ix image <archivo.AppImage> [icono]
       ix image list
       ix image -d [delete <archivo.desktop>]
       ix image -d-s
       
Descripción:
  Gestiona archivos .AppImage y sus accesos directos (.desktop).

Comandos:
  <archivo.AppImage> [icono]   → Crea un .desktop para el AppImage especificado. 
  list                         → Lista todos los AppImage en la carpeta actual.
  -d                           → Lista solo los .desktop creados por ixtools.
  -d delete <archivo.desktop>  → Elimina un .desktop creado por ixtools.
  -d-s                         → Lista todos los .desktop del usuario, incluyendo los del sistema.

Ejemplos:
  ix image Archivo.AppImage
  ix image list
  ix image -d
  ix image -d delete Archivo.desktop
""")
