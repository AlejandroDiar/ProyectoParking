# PROYECTO 2 ASIR: Sistema de Control de Parking

Este proyecto soluciona la gestión y control de acceso a un parking mediante el reconocimiento de matrículas y sensores de proximidad para monitorizar la disponibilidad de aparcamientos libres. Gracias a una infraestructura virtualizada, el sistema garantiza una alta disponibilidad y seguridad en los datos.

## Sistema diseñado para:
- Controlar la **entrada y salida de vehículos** mediante cámaras.
- **Comprobar vehículos no válidos** o mal estacionados.
- Realizar el **seguimiento de la salida de un vehículo**.
- Integrar diferentes **dispositivos y sistemas de autentificación**.
- Ofrecer una **configuración rápida y sencilla**.

## Infraestructura
- **Proxmox VE:** Hypervisor central donde se alojan las máquinas servidores y clientes.
- **ZFS RAID 1:** Sistema de almacenamiento para generar archivos con redundancia y asegurar la integridad de los datos ante fallos físicos.
- **pfSense:** Router y firewall perimetral imprescindible para la seguridad y funcionamiento de la red.

## Software e IA
- **Python + Flask:** Backend del servidor web y gestión de la interfaz de usuario.
- **YOLO y EasyOCR:** Modelos de IA utilizados para la detección de vehículos y el reconocimiento de caracteres en las matrículas.
- **SQLite:** Base de datos ligera utilizada para el registro de las matrículas detectadas y su posterior almacenamiento.

## Hardware
- **Arduino:** Mediante ultrasonidos detecta la distancia al obstáculo, lo que permite conocer si una plaza de parking está vacía u ocupada.
- **Uptime Kuma:** Monitorización de conectividad de cámaras con alertas automáticas vía Gmail.
- **Grafana:** Visualización de métricas de rendimiento del servidor en tiempo real (CPU, RAM).

## Red y Seguridad
- **Segmentación LAN:** Gestión de tráfico mediante pfSense para minimizar la superficie de exposición.
- **Direccionamiento Estático:** Las cámaras IP utilizan reservas de IP por MAC para garantizar seguridad y rendimiento óptimo de los scripts.
- **Cifrado:** Implementación de certificado SSL mediante OpenSSL para asegurar el tráfico interno.
- **Hardening:** Implementación de Fail2Ban para mitigar ataques de fuerza bruta en la consola de administración.

## Flujo de Funcionamiento
1. **Detección:** Las cámaras IP (simuladas en Linux) envían el flujo de vídeo al script de Python.
2. **Procesado:** El modelo YOLO detecta el vehículo y EasyOCR extrae la matrícula.
3. **Validación:** Se comprueba si la matrícula está en la Lista Negra para disparar alertas de seguridad.
4. **Registro:** Los datos se guardan en SQLite y se visualizan en el dashboard de Flask.
5. **Hardware:** Los sensores ultrasónicos (Arduino) actualizan el estado de las plazas en tiempo real.

## Resiliencia y Datos
- **Tolerancia a Fallos:** Configuración ZFS RAID 1 que permite la operatividad continua ante el fallo de un disco físico.
- **Recuperación:** Plan de recuperación ante desastres (DRP) basado en la restauración de backups diarios gestionados mediante cron.

## Participantes

| Nombre | GitHub | Correo |
| :--- | :--- | :--- |
| Julio Jesús López Casado | [@juljesus77-lab](https://github.com/juljesus77-lab) | juljesus77@gmail.com |
| Roberto Ariza Molina | [@roberto-ariza](https://github.com/roberto-ariza) | rarimol@ieszaidinvergeles.org |
| Alejandro Álvarez Soro | [@aleexx30](https://github.com/aleexx30) | aalvsor725@ieszaidinvergeles.org |
| Alejandro Martín Fernández | [@Alejandro574](https://github.com/Alejandro574) | amarfer574@ieszaidinvergeles.org |
| Alejandro Díaz Ariza | [@AlejandroDiar](https://github.com/AlejandroDiar) | adiaari1810@ieszaidinvergeles.org |
