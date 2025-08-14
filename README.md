# ixtools

ixtools es un conjunto de herramientas internas para VortexOS, AstraOS y sistemas basados en Linux, diseñado para automatizar tareas, optimizar flujos de trabajo y centralizar utilidades del sistema.
El objetivo es mantener un ecosistema limpio, modular y totalmente controlado por el usuario.

## 📦 Versión actual

v2.0.0 — Modular y escalable

Core actualizado con soporte --version global.

Al invocar un módulo sin argumentos, muestra su versión y ayuda automáticamente.

Listado de módulos muestra nombre, versión y descripción.

Módulos list e image mejorados: salida clara, orden alfabético y errores robustos.

Arquitectura modular preparada para integrar nuevos módulos automáticamente.

## 📂 Estructura del proyecto
```bash
ixtools/
├── core.py        # Punto de entrada principal
├── modules/       # Módulos y herramientas reutilizables
│   ├── list.py    # Lista todos los módulos y su descripción
│   └── image.py   # Gestión de archivos .AppImage y accesos directos
├── scripts/       # Herramientas individuales adicionales
└── docs/          # Documentación técnica y guía de desarrollo
```
## ⚙️ Instalación en modo editable (desarrollo)
```bash
git clone https://github.com/<usuario>/ixtools.git
cd ixtools
pip install -e .
```

Nota: Actualmente, ixtools funciona dentro del entorno virtual de desarrollo.
En futuras versiones se implementará instalación global.

## 🖥️ Uso básico y comandos disponibles
### 1. Mostrar versión de ixtools
ix --version


Salida:

ixtools version v2.0.0

### 2. Listar todos los módulos disponibles
ix list


Salida:

Herramientas disponibles:
- list      | v2.0.0  → Lista todos los módulos/herramientas disponibles en Ixtools
- image     | v1.1.0  → Gestiona archivos .AppImage y sus accesos directos (.desktop)

### 3. Gestionar archivos .AppImage
ix image list        # Lista archivos .AppImage en la carpeta actual
ix image -d          # Lista solo los .desktop creados por ixtools
ix image -d delete <archivo.desktop>  # Elimina un .desktop creado por ixtools
ix image -d-s        # Lista todos los .desktop del usuario, incluyendo los del sistema
ix image <Archivo.AppImage> [icono]   # Crea un .desktop para un AppImage


Todos los módulos ahora muestran ayuda automáticamente si se ejecutan sin argumentos:

ix image

## 🛠️ Próximos pasos

Añadir nuevos módulos: pkg, config, sysinfo, etc.

Mejorar manejo de rutas y parámetros en módulos existentes.

Extender soporte a instalación global.

Documentar cada comando en /docs con ejemplos y versiones.

Integración futura de scripts automáticos para CI/CD y tests modulares.

## 📜 Licencia

Este proyecto está licenciado bajo la GPL-3.0.
Consulta el archivo LICENSE para más detalles.

## 📌 Notas para desarrolladores

Los comentarios # TODO: marcan ideas o funcionalidades pendientes.

Mantener el código documentado y consistente garantiza escalabilidad.

Cada módulo debe ejecutarse y testearse de forma independiente.

Todos los módulos deben implementar __version__ y __desc__.

## 🤝 Contribuciones

Actualmente el desarrollo es cerrado y se gestiona de forma interna.
En el futuro se aceptarán pull requests, sugerencias y reportes de issues.