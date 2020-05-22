function myFunc(menu) {
    setTimeout(() => {
    fetch('/upload/', {
        method: 'POST',
        body: JSON.stringify(menu)
    }).then(function(response) {
        return response.text();
    }).then(function (text) {
        console.log('POST response: ');
        console.log(text);
    });
    }, 1000);
    console.log('Sending request...')
}
