# 🛡️ Cybersecurity Intelligence Dashboard

Un dashboard completo para la recopilación, procesamiento y visualización de datos de ciberataques de múltiples fuentes de inteligencia de amenazas.

## 📋 Descripción

Este proyecto es un dashboard de inteligencia de ciberseguridad que permite centralizar y procesar información de amenazas desde diversas fuentes como RSS feeds, IntelX, AlienVault (OTX), y otras plataformas de threat intelligence. La aplicación proporciona una interfaz unificada para analizar y monitorear ciberataques en tiempo real.

## ✨ Características

- 🔍 **Múltiples fuentes de datos**: Integración con RSS, IntelX, AlienVault OTX
- 📊 **Dashboard interactivo**: Visualización en tiempo real de amenazas
- 🐳 **Containerizado**: Fácil despliegue con Docker
- ⚡ **Procesamiento automático**: Curación automática de datos
- 🔄 **Actualizaciones en tiempo real**: Monitoreo continuo de fuentes
- 📈 **Análisis de tendencias**: Identificación de patrones de amenazas

## 🚀 Instalación

### Prerrequisitos

- Docker y Docker Compose
- Git
- Bash (para el script de ejecución)

### Clonar el repositorio

```bash
git clone https://github.com/JaviGr3p/pipeline-intelligence.git
cd pipeline-intelligence
```

### Configuración

1. Copia el archivo de configuración de ejemplo:
```bash
cp .env.example .env
```

2. Edita el archivo `.env` con tus credenciales y configuraciones:
```bash
nano .env
```

### Ejecutar con Docker

#### Opción 1: Script automatizado (Recomendado)
```bash
chmod +x dashboard.sh
./dashboard.sh
```

#### Opción 2: Docker Compose manual
```bash
docker-compose up -d
```

## 🔧 Uso

Una vez iniciado el dashboard, accede a través de tu navegador:

```
http://localhost:8080
```

### Comandos principales

- **Iniciar el dashboard**: `./dashboard.sh start`
- **Detener el dashboard**: `./dashboard.sh stop`
- **Ver logs**: `./dashboard.sh logs`
- **Reiniciar servicios**: `./dashboard.sh restart`
- **Estado de contenedores**: `./dashboard.sh status`

## 📁 Estructura del proyecto

```
pipeline-intelligence/
├── docker-compose.yml          # Configuración de Docker
├── Dockerfile                  # Imagen personalizada
├── dashboard.sh               # Script principal de ejecución
├── .env.example              # Configuración de ejemplo
├── config/                   # Archivos de configuración
│   ├── sources.yml          # Configuración de fuentes
│   └── dashboard.conf       # Configuración del dashboard
├── src/                     # Código fuente
│   ├── collectors/          # Módulos de recolección de datos
│   ├── processors/          # Procesadores de datos
│   └── dashboard/           # Interfaz web
├── data/                    # Datos persistentes
└── logs/                    # Archivos de log
```

## ⚙️ Configuración de fuentes

### RSS Feeds
```yaml
rss_sources:
  - name: "Security Feed"
    url: "https://feeds.feedburner.com/eset/blog"
    interval: 300
```

### IntelX
```yaml
intelx:
  api_key: "your_api_key"
  endpoint: "https://2.intelx.io"
  queries:
    - "malware"
    - "ransomware"
```

### AlienVault OTX
```yaml
otx:
  api_key: "your_otx_key"
  endpoint: "https://otx.alienvault.com/api/v1"
```

## 📊 Fuentes de datos soportadas

- **RSS Feeds**: Blogs de seguridad, feeds de noticias
- **IntelX**: Búsquedas en bases de datos de inteligencia
- **AlienVault OTX**: Open Threat Exchange
- **APIs personalizadas**: Integración con APIs propias
- **Archivos locales**: CSV, JSON, XML

## 🛠️ Desarrollo

### Requisitos de desarrollo
```bash
# Instalar dependencias de desarrollo
pip install -r requirements-dev.txt
```

### Ejecutar en modo desarrollo
```bash
./dashboard.sh dev
```

### Tests
```bash
docker exec -it pipeline-intelligence pytest
```

## 🔒 Seguridad

- Todas las credenciales deben almacenarse en el archivo `.env`
- No commitear archivos de configuración con credenciales reales
- Usar HTTPS en producción
- Configurar firewalls apropiadamente

## 📝 Logs y monitoreo

Los logs se almacenan en la carpeta `logs/` y se pueden consultar con:

```bash
./dashboard.sh logs [servicio]
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**JaviGr3p**
- GitHub: [@JaviGr3p](https://github.com/JaviGr3p)

## 🆘 Soporte

Si encuentras algún problema o tienes preguntas:

1. Revisa la sección de [Issues](https://github.com/JaviGr3p/pipeline-intelligence/issues)
2. Crea un nuevo issue si no encuentras solución
3. Proporciona logs y detalles del error

## 📋 Roadmap

- [ ] Integración con más fuentes de threat intelligence
- [ ] Dashboard móvil
- [ ] Alertas automáticas por email/Slack
- [ ] Análisis con machine learning
- [ ] API REST para integración externa
- [ ] Exportación de reportes
- [ ] Modo clustering para alta disponibilidad

## 🔄 Changelog

### v1.0.0 (Próximo release)
- Primera versión estable
- Integración con fuentes principales
- Dashboard web funcional
- Containerización completa

---

⭐ Si este proyecto te resulta útil, ¡dale una estrella!

🐛 **¿Encontraste un bug?** Abre un issue [aquí](https://github.com/JaviGr3p/pipeline-intelligence/issues)

💡 **¿Tienes una idea?** Las sugerencias son bienvenidas
