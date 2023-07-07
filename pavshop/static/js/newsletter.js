let newsletterForm = document.getElementById('newsletter-form')
newsletterForm.addEventListener('submit', function(e){
    e.preventDefault()
    let email = document.getElementById('newsletter-email')
    console.log(email.value)

    fetch('http://127.0.0.1:8000/api/newsletter/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': newsletterForm.csrfmiddlewaretoken.value,
        },
        body: JSON.stringify({'email' : email.value})
    })
    .then(response => {
        if (response.ok){
            newsletterForm.innerHTML = '<h2 style="color:white;" margin-left: 50px>Thanks for your subscribing!</h2>'
        }
        else{
            alert('Already exists!')
        }
    })

}


)