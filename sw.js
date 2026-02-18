// Service Worker para Prof. Sergio Seguel - Recursos Educativos
const CACHE_NAME = 'prof-sergio-v1';
const OFFLINE_URL = '/offline.html';

// Archivos a cachear inicialmente
const PRECACHE_ASSETS = [
    '/',
    '/index.html',
    '/videos.html',
    '/contacto.html',
    '/cursos/matematica-7basico.html',
    '/cursos/matematica-1medio.html',
    '/cursos/matematica-2medio.html',
    '/css/style.css',
    '/manifest.json',
    '/offline.html',
    'https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css',
    'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css'
];

// Instalar Service Worker
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('Cache abierto');
                return cache.addAll(PRECACHE_ASSETS);
            })
            .then(() => self.skipWaiting())
    );
});

// Activar y limpiar caches antiguos
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((cacheNames) => {
            return Promise.all(
                cacheNames
                    .filter((name) => name !== CACHE_NAME)
                    .map((name) => caches.delete(name))
            );
        }).then(() => self.clients.claim())
    );
});

// Estrategia: Network first, fallback to cache
self.addEventListener('fetch', (event) => {
    // Solo manejar requests GET
    if (event.request.method !== 'GET') return;

    // Ignorar requests de extensiones y analytics
    if (event.request.url.includes('chrome-extension') ||
        event.request.url.includes('google-analytics')) {
        return;
    }

    event.respondWith(
        fetch(event.request)
            .then((response) => {
                // Clonar respuesta para cache
                if (response.status === 200) {
                    const responseClone = response.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseClone);
                    });
                }
                return response;
            })
            .catch(() => {
                // Si falla la red, buscar en cache
                return caches.match(event.request)
                    .then((cachedResponse) => {
                        if (cachedResponse) {
                            return cachedResponse;
                        }
                        // Si es una pagina HTML, mostrar offline
                        if (event.request.headers.get('accept').includes('text/html')) {
                            return caches.match(OFFLINE_URL);
                        }
                    });
            })
    );
});
