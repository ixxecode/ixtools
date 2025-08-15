#!/usr/bin/env python3
# ====================================================
# Archivo      : image.py
# Descripción  : Manejo de archivos AppImage
# Autor        : IxxeCODE
# Copyright    : 2025 IxxeCODE
# Licencia     : GNU General Public License v3 o superior
#               (ver archivo LICENSE para detalles completos)
# ====================================================

__version__ = "v2.0.0"
__desc__ = "Gestiona archivos .AppImage para listarlos o crear accesos directos (.desktop) y configurarlos."
__author__ = "IxxeCODE"

import os
import sys

# Importar funciones desde la carpeta _image_data
from ix.modules._image_data.list_appimages import list_appimages
from ix.modules._image_data.list_desktops import list_desktops
from ix.modules._image_data.list_all_desktops import list_all_desktops
from ix.modules._image_data.delete_desktop import delete_desktop
from ix.modules._image_data.create_desktop import create_desktop
from ix.modules._image_data.messages import (
    PREFIX,
    ERROR_FILE_NOT_FOUND,
    ERROR_NOT_APPIMAGE,
    ERROR_INVALID_COMMAND,
    ERROR_INVALID_SUBCOMMAND,
    USAGE_CREATE,
    USAGE_DELETE,
    USAGE_LIST,
    USAGE_EDIT,
    USAGE_UPDATE
)

def run(args):
    """
    Función principal para manejar los comandos relacionados con AppImage.
    Actúa como un compositor que dirige las llamadas a las funciones específicas
    ubicadas en la carpeta _image_data.

    Args:
        args (list): Una lista de argumentos de línea de comandos.
    """
    # Manejo de comandos globales como --version, --about, -h, --help
    if "--version" in args:
        print(f"{PREFIX} ix image {__version__}")
        return
    if "--about" in args:
        print(f"{PREFIX} {__desc__}")
        return
    if not args or args[0] in ["-h", "--help"]:
        print_help()
        return

    # Si no se proporcionan argumentos, por defecto se lista los desktops de ixtools
    if not args:
        list_desktops()
        return

    # Ajustar args si el primer elemento es el nombre del script 'image'
    if args[0].lower() == "image":
        args = args[1:]
        if not args: # Si después de quitar 'image' no quedan argumentos, mostrar ayuda o default
            list_desktops()
            return

    cmd = args[0].lower()

    # Diccionario para mapear subcomandos de 'list' a sus funciones
    list_commands = {
        "appimage": list_appimages,
        "desktop": list_desktops,
    }

    if cmd == "create":
        if len(args) < 2:
            print(USAGE_CREATE)
            return
        appimage_file = args[1]
        if not os.path.isfile(appimage_file):
            print(ERROR_FILE_NOT_FOUND.format(appimage_file))
            return
        if not appimage_file.lower().endswith(".appimage"):
            print(ERROR_NOT_APPIMAGE.format(appimage_file))
            return
        # Llama a la función para crear un archivo .desktop
        create_desktop(appimage_file, args[2] if len(args) > 2 else None)
    elif cmd == "delete":
        if len(args) < 2:
            print(USAGE_DELETE)
            return
        desktop_file = args[1]
        # La validación de existencia y tipo .desktop se maneja dentro de delete_desktop
        delete_desktop(desktop_file)
    elif cmd == "list":
        if len(args) < 2:
            print(USAGE_LIST)
            return
        sub_cmd = args[1].lower()
        if sub_cmd == "desktop" and len(args) > 2 and args[2].lower() == "--system":
            # Llama a la función para listar todos los archivos .desktop
            list_all_desktops()
        elif sub_cmd in list_commands:
            # Llama a la función correspondiente del diccionario
            list_commands[sub_cmd]()
        else:
            print(ERROR_INVALID_SUBCOMMAND.format(sub_cmd))
    elif cmd == "edit":
        print(USAGE_EDIT)
    elif cmd == "update":
        print(USAGE_UPDATE)
    else:
        print(ERROR_INVALID_COMMAND.format(cmd))

def print_help():
    print(f"""
Uso: ix image [comando] [argumentos]
       
Descripción:
  {__desc__}

Comandos:
  create <archivo.AppImage> [icono]   → Crea un .desktop para el AppImage especificado.
  delete <archivo.desktop>            → Elimina un .desktop creado por ixtools.
  edit <archivo.desktop>              → Edita un .desktop (no implementado).
  update <archivo.desktop> <appimage> → Actualiza la ruta de un .desktop (no implementado).
  list appimage                       → Lista todos los AppImage en la carpeta actual.
  list desktop                        → Lista solo los .desktop creados por ixtools.
  list desktop --system               → Lista todos los .desktop del usuario, incluyendo los del sistema.

Opciones globales:
  --version                           → Muestra la versión de la herramienta.
  --about                             → Muestra la descripción de la herramienta.
  -h, --help                          → Muestra esta ayuda.

Ejemplos:
  ix image create MiApp.AppImage
  ix image delete MiApp.desktop
  ix image list appimage
  ix image list desktop
  ix image list desktop --system
  ix image --version
""")
