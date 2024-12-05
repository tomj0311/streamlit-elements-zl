
self.addEventListener('install', function(event) {
    console.log('Service worker installing...');
    // Perform install steps
});

self.addEventListener('activate', function(event) {
    console.log('Service worker activating...');
    // Perform activate steps
});

self.addEventListener('fetch', function(event) {
    console.log('Fetching:', event.request.url);
    // Perform fetch steps
});