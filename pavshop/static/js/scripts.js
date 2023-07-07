// window.addEventListener('load', async function(event){
//     let response = await fetch('http://127.0.0.1:8000/api/products/')
//     let resData = await response.json()
//     let products = document.querySelector('#products')
//     const smallDescription = "{{}}"
//     const maxWords = 20;
//     const truncatedDescription = truncateWords(small_description, maxWords);
//     const lineBreaksDescription = this.addLineBreaks(truncatedDescription);
//     for (product of resData){
//         products.innerHTML += `
//         <div class="col-md-4">
//                 <div class="item"> 
//                   <!-- Item img -->
//                   <div class="item-img"> 
//                     <img class="img-1" src="${product.image}" alt="" >
//                     <!-- Overlay -->
//                     <div class="overlay">
//                       <div class="position-center-center">
//                         <div class="inn"><a href="#" data-lighter><i class="icon-magnifier"></i></a> <a href="{% url 'shopping_cart_page' %}"><i class="icon-basket"></i></a></div>
//                         <!-- <div class="inn"><a href="#" data-lighter><i class="icon-magnifier"></i></a> <a href="{% url 'shopping_cart_page' %}"><i class="icon-basket"></i></a> <a href="#." ><i class="icon-heart"></i></a></div> -->

//                       </div>
//                     </div>
//                   </div>

//                   <!-- Item Name -->
//                   <div class="item-name"> <a href="${product.get_absolute_url}">${product.title} ${product.category.name}</a>
//                     <p>${product.small_description}</p>
//                   </div>
//                   <!-- Price --> 
//                   <span class="price"><small>$</small>${product.money}</span> </div>
//               </div>
        
//         `
//     }

// })