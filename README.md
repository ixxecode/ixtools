# ixtools

ixtools es un conjunto de herramientas internas para VortexOS, AstraOS y sistemas basados en Linux, diseñado para automatizar tareas, optimizar flujos de trabajo y centralizar utilidades del sistema.
El objetivo es mantener un ecosistema limpio, modular y totalmente controlado por el usuario.

---

## 📦 Versión actual

v2.0.0 — Modular y escalable

Core actualizado con soporte global --version y --about.

Al invocar un módulo sin argumentos, muestra automáticamente ayuda o listado de recursos.

Módulos list e image actualizados: salida clara, orden alfabético, errores robustos, mensajes estandarizados.

Arquitectura modular lista para integrar nuevos módulos automáticamente (_image_data en image como ejemplo).

Mensajes centralizados en messages.py para consistencia y fácil mantenimiento.

---

## 📂 Estructura del proyecto
```bash
ixtools/
├── src/
│   └──ix/
│       ├── __init__.py
│       ├── core.py                 # Punto de entrada principal
│       ├── logger.py               # Módulo de logging interno
│       ├── config.py               # Configuraciones globales de ixtools
│       └── modules/                # Módulos y herramientas reutilizables
│           ├── __init__.py
│           ├── list.py             # Lista todos los módulos y su descripción
│           ├── image.py            # Gestión de archivos .AppImage y accesos directos
│           └── _image_data/        # Funciones internas de image
│               ├── __init__.py
│               ├── create_desktop.py
│               ├── delete_desktop.py
│               ├── list_all_desktops.py
│               ├── list_appimages.py
│               ├── list_desktops.py
│               └── messages.py
├── tests/                  # Tests de los módulos
├── .gitignore
├── README.md
├── LICENSE
├── pyproject.toml
└── requirements.txt
```

    Nota: La carpeta data/ se utiliza para almacenar información persistente o compartida entre módulos, y _image_data/ contiene todas las funciones internas de image para mantener modularidad y escalabilidad.

## ⚙️ Instalación en modo editable (desarrollo)
```bash
git clone https://github.com/<usuario>/ixtools.git
cd ixtools
pip install -e .
```

    Nota: Actualmente, ixtools funciona dentro del entorno virtual de desarrollo. En futuras versiones se implementará instalación global.

## 🖥️ Uso básico y comandos disponibles
### 1. Mostrar versión de ixtools
```bash
ix --version
```

Salida:
```bash
[ixtools] ix v2.0.0
```

### 2. Listar todos los módulos disponibles
```bash
ix list
```

Salida:
```bash
Herramientas disponibles:
- list      | v2.0.0  → Lista todos los módulos/herramientas disponibles en Ixtools
- image     | v1.1.0  → Gestiona archivos .AppImage y sus accesos directos (.desktop)
```
### 3. Gestionar archivos .AppImage
#### Listar todos los AppImage en la carpeta actual
```bash
ix image list appimage
```

#### Listar solo los .desktop creados por ixtools
```bash
ix image list desktop
```

#### Listar todos los .desktop del usuario, incluyendo los del sistema
```bash
ix image list desktop --system
```

#### Crear un .desktop para un AppImage
```bash
ix image create MiApp.AppImage [icono]
```

#### Eliminar un .desktop creado por ixtools
```bash
ix image delete MiApp.desktop
```

#### Mostrar ayuda del módulo
```bash
ix image
```

Todos los módulos ahora muestran ayuda automáticamente si se ejecutan sin argumentos.

## 📜 Licencia

Este proyecto está licenciado bajo la GPL-3.0.
Consulta el archivo LICENSE para más detalles.

## 📌 Notas para desarrolladores

Mantener el código documentado y consistente garantiza escalabilidad.

Cada módulo debe ejecutarse y testearse de forma independiente.

Todos los módulos deben implementar __version__, __desc__ y __author__.

Los mensajes deben centralizarse para mantener uniformidad (messages.py en image como referencia).

## 🤝 Contribuciones

Actualmente el desarrollo es cerrado y se gestiona de forma interna.
En el futuro se aceptarán pull requests, sugerencias y reportes de issues.