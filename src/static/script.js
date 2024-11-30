function toggleColor(element) {
    const button = element
    if (button.classList.contains("btn-secondary")){
        button.classList.replace("btn-secondary", "btn-warning")
        console.log(button.id)
         fetch('/toggleColor', {
            method: 'POST',
           headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                button_id: button.id
              })
        })
    }
    else if (button.classList.contains("btn-warning")){
        button.classList.replace("btn-warning", "btn-secondary")
        console.log("lox")
        fetch('/toggleColor', {
            method: 'POST',
           headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                button_id: button.id
              })
        })
    }
}

function confirmChoice(){
    const email = form.querySelector('[name="email"]'),
    name = form.querySelector('[name="name"]'),
    surname = form.querySelector('[name="surname"]')
    const data = {
        email: email.value,
        name: name.value,
        surname: surname.value
    }
    fetch('/confirmChoice', {
           method: 'POST',
           headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({
                email: email.value
                name: name.value
                surname: surname.value
              })
        })
}