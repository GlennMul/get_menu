function myFunc(menu) {
    setTimeout(() => {
    for (var i = 0; i < menu.Category.length; i++) {
    const item = menu.Category[i] +' : '+ menu.Menu_Item[i]  +' : '+ menu.Description[i] +' : '+ menu.Price[i] +' : '+ menu.Image_URL[i] ;
    console.log(item);
    console.log(i);
    }
    }, 2000);
    return 200
}
