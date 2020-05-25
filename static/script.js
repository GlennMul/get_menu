function myFunc(menu,num,tot) {
    setTimeout(() => {
    fetch('/upload/', {
        method: 'POST',
        data: JSON.stringify(menu),
        num: 1

    }).then(function(response) {
        return response.text();
    }).then(function (text) {
        console.log('POST response: ');
        console.log(text);
    });
    }, 1000);
    console.log('Sending request...')

    return 200
}


var movies = {
   'title': 'soemthing',
    'release_date': 'date1'
    }

function myFunc1(menu,num,tot) {
    setTimeout(() => {
        if (num < tot) {
            $.ajax({
            url: '/upload/',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(menu),   // converts js value to JSON string
            })
            .done(function(response){     // on success get the return object from server
                console.log(result)     // do whatever with it. In this case see it in console
            })

            num ++
            myFunc2(menu,num,tot)

        } else {
            console.log('Upload Complete')
        }
    },1500)
}

function myFunc2(menu,num,tot) {
    setTimeout(() => {
        if (num < tot) {
            $.ajax({
            url: '/upload/',
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json',
            data: JSON.stringify(menu),   // converts js value to JSON string
            })
            .done(function(response){     // on success get the return object from server
                console.log(result)     // do whatever with it. In this case see it in console
            })

            num ++
            myFunc1(menu,num,tot)

        } else {
            console.log('Upload Complete')
        }
    },1500)
}