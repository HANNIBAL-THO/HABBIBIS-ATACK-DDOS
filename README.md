# 🚀 THO DDOS ATTACK TOOL

[![Discord](https://img.shields.io/discord/123456789?color=7289da&label=Discord&logo=discord&logoColor=ffffff)](https://discord.gg/4svwzsy3UP)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=flat&logo=youtube&logoColor=white)](TU_LINK_DE_YOUTUBE)

Una herramienta de DDoS con interfaz gráfica que incluye múltiples métodos de ataque y bypass.

![Preview](assets/preview.png)

## ⚡ Características

- 🎯 6 métodos diferentes de ataque
- 🔄 Rotación automática de proxies
- 🛡️ Bypass para Cloudflare y WAF
- 🖥️ Interfaz gráfica moderna
- 📊 Consola de logs en tiempo real

## 📥 Instalación

### Requisitos previos

```bash
# Instalar Python 3.8 o superior
# Instalar Git (opcional)
```

### Pasos de instalación

1. Clonar el repositorio o descargar como ZIP:
```bash
git clone https://github.com/TU_USUARIO/THO_PANEL_DDOS.git
cd THO_PANEL_DDOS
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 🚀 Uso

1. Ejecutar el script:
```bash
python "THO DDOS WEB.py"
```

2. Ingresar la URL objetivo
3. Seleccionar número de paquetes (threads)
4. Elegir método de ataque
5. Cargar/Buscar proxies
6. Iniciar ataque

## 🔨 Compilar a EXE

1. Instalar pyinstaller:
```bash
pip install pyinstaller
```

2. Compilar el script:
```bash
pyinstaller --onefile --icon=assets/icon.ico --noconsole "THO DDOS WEB.py"
```

3. El ejecutable se generará en la carpeta `dist`

## 🛠️ Métodos de Ataque

- **FLOOD ATTACK**: Combina GET+POST para saturar el servidor
- **BYPASS ATTACK**: Utiliza HEAD+GET para evadir protecciones
- **PROXY ROTATION**: Rota proxies para evitar bloqueos
- **CLOUDFLARE BYPASS**: Evasión específica para Cloudflare
- **CACHE BYPASS**: Ataque a la caché del servidor
- **WAF EVASION**: Bypass de Web Application Firewalls

## ⚠️ Aviso Legal

Esta herramienta es solo para propósitos educativos. El mal uso puede ser ilegal.

## 🔗 Links

- [Discord](https://discord.gg/4svwzsy3UP)
- [YouTube](TU_LINK_DE_YOUTUBE)

## 📝 Requisitos

```txt
pyside6
requests
urllib3
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea tu rama de característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📜 Licencia

Distribuido bajo la licencia MIT. Ver `LICENSE` para más información.
