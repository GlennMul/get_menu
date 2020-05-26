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



function myFunc1(menu,num,tot) {
    setTimeout(() => {
        if (num < tot) {
            menu = {'num' : num, 'menu' : JSON.stringify(menu)}
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
            menu = {'num' : num, 'menu' : JSON.stringify(menu)}
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
            //myFunc1(menu,num,tot)

        } else {
            console.log('Upload Complete')
        }
    },1500)
}

function myFunc3(menu,num,tot) {
    const run1 = new Promise((resolve, reject) => {
        menu = {'num' : num, 'menu' : JSON.stringify(menu)}
        setTimeout(() => {
            $.ajax({
                url: '/upload/',
                type: 'POST',
                dataType: 'json',
                contentType: 'application/json',
                data: JSON.stringify(menu),   // converts js value to JSON string
                success: function(response) {
                   console.log(response);
                   num++;
                   if (num < tot) {
                        myFunc4(jsmenu,num,tot);
                   } else {
                        console.log('Upload Complete')
                   }
                },
                })
            resolve(num+"/"+tot);
        },1500)
    });

    run1.then(ID => {console.log(ID)})

}

function myFunc4(menu,num,tot) {
    const run1 = new Promise((resolve, reject) => {
        menu = {'num' : num, 'menu' : JSON.stringify(menu)}
        setTimeout(() => {
            $.ajax({
                url: '/upload/',
                type: 'POST',
                dataType: 'json',
                contentType: 'application/json',
                data: JSON.stringify(menu),   // converts js value to JSON string
                success: function(response) {
                    console.log(response);
                   num++;
                   if (num < tot) {
                        myFunc3(jsmenu,num,tot);
                   } else {
                        console.log('Upload Complete')
                   }
                },
                })
            resolve(num+"/"+tot);
        },1500)
    });

    run1.then(ID => {console.log(ID)})

}