addEventListener('fetch', event => {
    let url = new URL(event.request.url);
    url.hostname = 'pan.baidu.com';   
    let request = new Request(url, event.request);
    event.respondWith(
        fetch(request, {
            headers:{
                'User-Agent':'pan.baidu.com'
            }
        })
    );
});
