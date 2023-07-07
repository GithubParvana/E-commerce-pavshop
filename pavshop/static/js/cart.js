function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');





// let btns = document.querySelectorAll(".shop-detail button")


// btns.forEach(btn=>{
//     btn.addEventListener("click", addToCart)
// })

// function addToCart(e){
//     let productsid = e.target.value
//     let url = "/add_to_cart/"
    
//     let data = {id:productsid}

//     fetch('http://127.0.0.1:8000/api/orders/', {
//         method: "POST",
//         headers: {"Content-Type":"application/json", 'X-CSRFToken': csrftoken},
//         body: JSON.stringify(data)
//     })
//     .then(res=>res.json())
//     .then(data=>{
//         console.log(data)
//     })
//     .catch(error=>{
//         console.log(error)
//     })

    
// }









var updateBttns = document.getElementsByClassName('update-cart')


for(var i = 0; i < updateBttns.length; i++){
    updateBttns[i].addEventListener('click', function(event){
        event.preventDefault()

        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)

        console.log('USER:', user)
        if(user === 'AnonymousUser')
        {
            console.log('Not logged in')
        }
        else
        {
            // updateUserOrder(productId, action)
            console.log('User is logged in, sending data...')
        }
    })
}



function updateUserOrder(productsId, action){
    console.log('User is logged in, sending data..')

    var url = '/update_item/'

    fetch('http://127.0.0.1:8000/api/orders/', {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body: JSON.stringify({'productsId': productsId, 'action':action})
    })

    .then((response) =>{
        return response.json()
    })

    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}