function toggleColor(element) {
    const button = element
    if (button.classList.contains("btn-secondary")){
        button.classList.replace("btn-secondary", "btn-warning")
        console.log(button.id + 'added')
    }
    else if (button.classList.contains("btn-warning")){
        button.classList.replace("btn-warning", "btn-secondary")
        console.log(button.id + 'removed')
    }
}


function getActiveSeats(){
    const selectedSeats = document.querySelectorAll(".btn-warning")
    const selectedSeatsId = []
    selectedSeats.forEach((seat) => {
        console.log(typeof seat.id)
        selectedSeatsId.push(seat.id)
    })
    console.log(selectedSeatsId)
    data = {
        seats: selectedSeatsId
    }
    fetch('/getActiveSeats', {
        method: 'POST',
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify(data)
    })
}
