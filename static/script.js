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
        },500)
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
        },500)
    });

    run1.then(ID => {console.log(ID)})

}