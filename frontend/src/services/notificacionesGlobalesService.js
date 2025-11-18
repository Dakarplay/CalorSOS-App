// Inicio notificacionesGlobalesService.js

// frontend/src/services/notificacionesGlobalesService.js

// Servicio para monitorear notificaciones globales desde el backend
// Funciona independientemente de la página actual

import api from './api.js';
import notificacionesService from './notificacionesService.js';

class NotificacionesGlobalesService {
    constructor() {
        this.intervalId = null;
        this.lastNotificationId = null;
        this.isMonitoring = false;
        this.checkInterval = 30000; // Verificar cada 30 segundos
    }

    // Iniciar monitoreo de notificaciones globales
    startMonitoring() {
        if (this.isMonitoring) return;

        console.log('Iniciando monitoreo de notificaciones globales...');
        this.isMonitoring = true;

        // Verificar inmediatamente
        this.checkForNewNotifications();

        // Configurar intervalo de verificación
        this.intervalId = setInterval(() => {
            this.checkForNewNotifications();
        }, this.checkInterval);
    }

    // Detener monitoreo
    stopMonitoring() {
        if (!this.isMonitoring) return;

        console.log('Deteniendo monitoreo de notificaciones globales...');
        this.isMonitoring = false;

        if (this.intervalId) {
            clearInterval(this.intervalId);
            this.intervalId = null;
        }
    }

    // Verificar nuevas notificaciones
    async checkForNewNotifications() {
        try {
            // Obtener la última notificación del usuario actual
            const response = await api.get('/notificaciones/');
            const notificaciones = response.data?.data || [];

            if (notificaciones.length === 0) return;

            // Ordenar por fecha descendente (más reciente primero)
            const sortedNotifications = notificaciones.sort((a, b) =>
                new Date(b.fecha_envio) - new Date(a.fecha_envio)
            );

            const latestNotification = sortedNotifications[0];

            // Verificar si es una nueva notificación
            if (!this.lastNotificationId || latestNotification.id_notificacion !== this.lastNotificationId) {
                // Es una nueva notificación
                this.lastNotificationId = latestNotification.id_notificacion;

                // Determinar tipo de notificación y mostrarla
                await this.processNotification(latestNotification);
            }

        } catch (error) {
            console.warn('Error verificando notificaciones globales:', error);
        }
    }

    // Procesar y mostrar notificación según su tipo
    async processNotification(notification) {
        const mensaje = notification.mensaje;

        // Determinar tipo de notificación y mostrar push notification
        await this.showPushNotification(notification);
    }

    // Mostrar notificación de alerta de calor
    async showHeatAlertNotification(notification) {
        const mensaje = notification.mensaje;

        // Extraer información de la alerta (temperatura, UV, etc.)
        const tempMatch = mensaje.match(/Temp:\s*(\d+(?:\.\d+)?)°C/);
        const uvMatch = mensaje.match(/UV:\s*(\d+(?:\.\d+)?)/);

        const temperatura = tempMatch ? parseFloat(tempMatch[1]) : null;
        const uv = uvMatch ? parseFloat(uvMatch[1]) : null;

        // Crear objeto de alerta simulado
        const alertaSimulada = {
            nivel_riesgo: mensaje.match(/ALERTA DE CALOR\s+(\w+)/)?.[1] || 'MEDIA',
            temperatura: temperatura,
            indice_uv: uv,
            humedad: null // No disponible en el mensaje
        };

        await notificacionesService.showHeatAlert(alertaSimulada);
    }

    // Mostrar notificación push en la app
    async showPushNotification(notification) {
        const mensaje = notification.mensaje;

        // Determinar tipo de notificación
        if (mensaje.includes('ALERTA DE CALOR')) {
            // Es una alerta de calor
            const title = '⚠️ ALERTA DE CALOR';
            const body = mensaje.replace('⚠️ ALERTA DE CALOR ', '');
            await notificacionesService.showPushNotification(title, body, 5000); // 5 segundos
        } else {
            // Otro tipo de notificación
            const title = '📢 CalorSOS';
            await notificacionesService.showPushNotification(title, mensaje, 3000); // 3 segundos
        }
    }

    // Mostrar notificación genérica
    async showGenericNotification(notification) {
        const mensaje = notification.mensaje;

        // Mostrar como notificación genérica
        notificacionesService.showNotification(
            '📢 CalorSOS',
            {
                body: mensaje,
                icon: '/assets/images/logo.svg',
                tag: 'calorsos-generic',
                requireInteraction: false
            }
        );
    }

    // Forzar verificación inmediata
    async forceCheck() {
        await this.checkForNewNotifications();
    }

    // Obtener estado del servicio
    getStatus() {
        return {
            isMonitoring: this.isMonitoring,
            lastNotificationId: this.lastNotificationId,
            checkInterval: this.checkInterval
        };
    }

    // Cambiar intervalo de verificación
    setCheckInterval(intervalMs) {
        this.checkInterval = intervalMs;

        // Reiniciar monitoreo con nuevo intervalo
        if (this.isMonitoring) {
            this.stopMonitoring();
            this.startMonitoring();
        }
    }
}

// Crear instancia singleton
const notificacionesGlobalesService = new NotificacionesGlobalesService();

export default notificacionesGlobalesService;

// Fin notificacionesGlobalesService.js
