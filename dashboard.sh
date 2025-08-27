#!/bin/bash

echo ""
echo "🔐 App Intelligence"
echo "------------------------------------------------"
echo "Opciones:"
echo "1. Iniciar (docker-compose up -d)"
echo "2. Reconstruir (docker-compose up --build)"
echo "3. Detener (docker-compose down)"
echo "4. Apagar totalmente (down + prune)"
echo "5. Salir"
echo "------------------------------------------------"
read -p "Selecciona una opción [1-5]: " opcion

case $opcion in
  1)
    echo "🚀 Iniciando servicio..."
    docker-compose up -d
    ;;
  2)
    echo "🔄 Reconstruyendo y reiniciando servicio..."
    docker-compose up --build
    ;;
  3)
    echo "🛑 Deteniendo servicio..."
    docker-compose down
    ;;
  4)
    echo "⚠ Apagando y limpiando recursos..."
    docker-compose down --volumes --remove-orphans
    docker system prune -f
    ;;
  5)
    echo "👋 Saliendo..."
    exit 0
    ;;
  *)
    echo "❌ Opción no válida"
    ;;
esac
