# ixtools

**ixtools** es un conjunto de herramientas internas para **VortexOS**, **AstraOS** y sistemas basados en **Linux**, diseñadas para automatizar tareas, optimizar flujos de trabajo y centralizar utilidades del sistema.  
El objetivo es mantener un ecosistema limpio, modular y totalmente controlado por el usuario.

---

## 📦 Versión actual
**v0.1 — MVP funcional**  
- Base del sistema lista.  
- Comandos `list` e `image list` funcionando desde entorno virtual.  
- Arquitectura modular inicial implementada.

---

## 📂 Estructura del proyecto
```bash
ixtools/
├── core.py # Punto de entrada principal
├── modules/ # Módulos y funciones reutilizables
├── scripts/ # Herramientas individuales
└── docs/ # Documentación técnica
```

---

## ⚙️ Instalación en modo editable (desarrollo)
```bash
git clone https://github.com/<usuario>/ixtools.git
cd ixtools
pip install -e .
Nota: Actualmente, ixtools solo funciona dentro del entorno virtual de desarrollo.
En futuras versiones se implementará instalación global.
```

---

## 🖥️ Comandos disponibles
1. Listar herramientas
```bash
ix list
```

Salida:
```bash
Herramientas disponibles:
- list   → Lista todas las herramientas.
- image  → Gestiona archivos AppImage.
```

2. Listar archivos .AppImage
```bash
ix image list
```

Salida (si no hay archivos):
```bash
No se encontraron archivos .AppImage en la carpeta actual.
```

---

## 🛠️ Próximos pasos
- Añadir nuevos módulos (pkg, config, sysinfo, etc.).
- Mejorar manejo de rutas y parámetros.
- Extender soporte a instalación global.
- Documentar cada comando en /docs.

---

## 📜 Licencia
Este proyecto está licenciado bajo la GPL-3.0.
Consulta el archivo LICENSE para más detalles.

---

## 📌 Notas para desarrolladores
Los comentarios # TODO: marcan ideas o funcionalidades pendientes.
Mantener el código documentado para asegurar escalabilidad.
Cada módulo debe poder ejecutarse y testearse de forma independiente.

---

## 🤝 Contribuciones
Actualmente el desarrollo está cerrado y se gestiona de forma interna.
En el futuro se aceptarán pull requests y reportes de issues.

---