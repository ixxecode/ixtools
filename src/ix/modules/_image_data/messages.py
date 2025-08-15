#!/usr/bin/env python3
# ====================================================
# Archivo      : messages.py
# Descripción  : Mensajes estandarizados para la herramienta 'image'
# Autor        : IxxeCODE
# Copyright    : 2025 IxxeCODE
# Licencia     : GNU General Public License v3 o superior
#               (ver archivo LICENSE para detalles completos)
# ====================================================

# Mensajes estandarizados para la herramienta 'image'

# Prefijo para todos los mensajes de la herramienta
PREFIX = "[ixtools:image]"

# Mensajes de éxito
OK_DESKTOP_CREATED = f"{PREFIX} [OK] Archivo .desktop creado en: {{}}"
OK_DESKTOP_DELETED = f"{PREFIX} [OK] Archivo .desktop '{{}}' eliminado."
INFO_SEARCH_LAUNCHER = f"{PREFIX} Puedes buscarlo en tu lanzador de aplicaciones."

# Mensajes de error
ERROR_FILE_NOT_FOUND = f"{PREFIX} Error: no se encontró el archivo '{{}}'."
ERROR_NOT_APPIMAGE = f"{PREFIX} Error: el archivo '{{}}' no es un .AppImage."
ERROR_NOT_DESKTOP = f"{PREFIX} Error: el archivo especificado no es un .desktop."
ERROR_DELETE_FAILED = f"{PREFIX} Error al eliminar el archivo '{{}}': {{}}"
ERROR_READ_FILE = f"{PREFIX} Advertencia: No se pudo leer el archivo {{}}: {{}}"
ERROR_INVALID_COMMAND = f"{PREFIX} Comando '{{}}' no reconocido. Usa 'ix image --help' para ver los comandos disponibles."
ERROR_INVALID_SUBCOMMAND = f"{PREFIX} Subcomando '{{}}' no reconocido. Uso: ix image list [appimage|desktop [--system]]"

# Mensajes de uso
USAGE_CREATE = f"{PREFIX} Uso: ix image create <archivo.AppImage> [icono]"
USAGE_DELETE = f"{PREFIX} Uso: ix image delete <archivo.desktop>"
USAGE_LIST = f"{PREFIX} Uso: ix image list [appimage|desktop [--system]]"
USAGE_EDIT = f"{PREFIX} La función 'edit' aún no está implementada. Uso: ix image edit <archivo.desktop>"
USAGE_UPDATE = f"{PREFIX} La función 'update' aún no está implementada. Uso: ix image update <archivo.desktop> <appimage>"

# Mensajes informativos
INFO_NO_APPIMAGES_FOUND = f"{PREFIX} No se encontraron archivos .AppImage en la carpeta actual."
INFO_APPIMAGES_FOUND = f"{PREFIX} Archivos .AppImage encontrados:"
INFO_NO_DESKTOPS_FOUND = f"{PREFIX} No se encontraron archivos .desktop."
INFO_NO_IXTOOLS_DESKTOPS_FOUND = f"{PREFIX} No se encontraron archivos .desktop creados por ixtools."
INFO_IXTOOLS_DESKTOPS_FOUND = f"{PREFIX} Archivos .desktop creados por ixtools:"
INFO_ALL_DESKTOPS_FOUND = f"{PREFIX} Todos los archivos .desktop encontrados:"
