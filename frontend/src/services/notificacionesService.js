// Inicio notificacionesService.js

// frontend/src/services/notificacionesService.js

// Servicio para manejar notificaciones push locales con sonido

class NotificacionesService {
    constructor() {
        this.audio = null;
        this.audioContext = null;
        this.isSupported = 'Notification' in window;
        this.hasPermission = false;
        this.settings = {
            sound: true,
            vibration: true,
            showAlerts: true
        };
        this.init();
    }

    // Inicializar el servicio
    async init() {
        if (!this.isSupported) {
            console.warn('Las notificaciones push no están soportadas en este navegador');
            return;
        }

        // Cargar configuración del usuario
        this.loadSettings();

        // Solicitar permisos si no los tenemos
        if (Notification.permission === 'default') {
            await this.requestPermission();
        } else if (Notification.permission === 'granted') {
            this.hasPermission = true;
        }

        // Inicializar audio
        this.initAudio();
    }

    // Solicitar permisos para notificaciones
    async requestPermission() {
        try {
            const permission = await Notification.requestPermission();
            this.hasPermission = permission === 'granted';
            return this.hasPermission;
        } catch (error) {
            console.error('Error solicitando permisos de notificación:', error);
            return false;
        }
    }

    // Inicializar sistema de audio
    initAudio() {
        try {
            // Crear contexto de audio para navegadores modernos
            if (window.AudioContext || window.webkitAudioContext) {
                this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            }

            // Crear elemento de audio
            this.audio = new Audio();
            this.audio.src = '/assets/audio/notificacion.mp3';
            this.audio.preload = 'auto';
            this.audio.volume = 0.7; // Volumen moderado

            // Manejar errores de carga
            this.audio.addEventListener('error', (e) => {
                console.warn('Error cargando audio de notificación:', e);
            });

        } catch (error) {
            console.warn('Error inicializando audio:', error);
        }
    }

    // Reproducir sonido de notificación
    async playSound() {
        if (!this.settings.sound || !this.audio) return;

        try {
            // Reanudar contexto de audio si está suspendido (requerido por política de autoplay)
            if (this.audioContext && this.audioContext.state === 'suspended') {
                await this.audioContext.resume();
            }

            // Reiniciar audio y reproducir
            this.audio.currentTime = 0;
            await this.audio.play();
        } catch (error) {
            console.warn('Error reproduciendo sonido:', error);
        }
    }

    // Vibrar dispositivo (si es móvil)
    vibrate() {
        if (!this.settings.vibration || !navigator.vibrate) return;

        // Patrón de vibración: 200ms on, 100ms off, 200ms on
        navigator.vibrate([200, 100, 200]);
    }

    // Mostrar notificación push
    showNotification(title, options = {}) {
        if (!this.hasPermission || !this.settings.showAlerts) return null;

        const defaultOptions = {
            icon: '/assets/images/logo.svg',
            badge: '/assets/images/logo.svg',
            silent: false, // Permitir sonido personalizado
            requireInteraction: false,
            tag: 'calorsos-alert', // Evitar duplicados
            ...options
        };

        try {
            const notification = new Notification(title, defaultOptions);

            // Auto-cerrar después de 5 segundos
            setTimeout(() => {
                notification.close();
            }, 5000);

            // Manejar clic en la notificación
            notification.onclick = () => {
                window.focus();
                notification.close();
            };

            return notification;
        } catch (error) {
            console.error('Error mostrando notificación:', error);
            return null;
        }
    }

    // Mostrar alerta de calor con sonido y notificación
    async showHeatAlert(alerta) {
        if (!alerta) return;

        const title = `⚠️ ALERTA DE CALOR ${alerta.nivel_riesgo.toUpperCase()}`;
        const body = `Temperatura: ${alerta.temperatura}°C | UV: ${alerta.indice_uv} | Humedad: ${alerta.humedad}%`;

        // Reproducir sonido
        await this.playSound();

        // Vibrar
        this.vibrate();

        // Mostrar notificación push
        this.showNotification(title, {
            body: body,
            icon: '/assets/images/logo.svg',
            tag: 'calorsos-heat-alert',
            requireInteraction: true, // Mantener visible hasta que el usuario interactúe
            actions: [
                {
                    action: 'view',
                    title: 'Ver detalles'
                }
            ]
        });
    }

    // Mostrar notificación push en la app con sonido
    async showPushNotification(title, body, duration = 3000) {
        // Reproducir sonido de notificación
        await this.playSound();

        // Crear elemento de notificación push
        const notification = document.createElement('div');
        notification.className = 'push-notification';
        notification.innerHTML = `
            <div class="push-notification-content">
                <div class="push-notification-title">${title}</div>
                <div class="push-notification-body">${body}</div>
            </div>
            <button class="push-notification-close" onclick="this.parentElement.remove()">×</button>
        `;

        // Agregar al DOM
        document.body.appendChild(notification);

        // Auto-remover después del tiempo especificado
        setTimeout(() => {
            if (notification.parentElement) {
                notification.remove();
            }
        }, duration);

        // Animación de entrada
        setTimeout(() => {
            notification.classList.add('show');
        }, 10);
    }

    // Cargar configuración del usuario
    loadSettings() {
        try {
            const saved = localStorage.getItem('notificationSettings');
            if (saved) {
                this.settings = { ...this.settings, ...JSON.parse(saved) };
            }
        } catch (error) {
            console.warn('Error cargando configuración de notificaciones:', error);
        }
    }

    // Guardar configuración del usuario
    saveSettings() {
        try {
            localStorage.setItem('notificationSettings', JSON.stringify(this.settings));
        } catch (error) {
            console.warn('Error guardando configuración de notificaciones:', error);
        }
    }

    // Actualizar configuración
    updateSettings(newSettings) {
        this.settings = { ...this.settings, ...newSettings };
        this.saveSettings();
    }

    // Verificar si las notificaciones están disponibles
    isAvailable() {
        return this.isSupported && this.hasPermission;
    }

    // Obtener estado actual
    getStatus() {
        return {
            supported: this.isSupported,
            permission: Notification.permission,
            hasPermission: this.hasPermission,
            settings: this.settings
        };
    }
}

// Crear instancia singleton
const notificacionesService = new NotificacionesService();

export default notificacionesService;

// Fin notificacionesService.js
