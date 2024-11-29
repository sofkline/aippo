function toggleColor(element) {
    const button = element
    if (button.classList.contains("btn-secondary")){
        button.classList.replace("btn-secondary", "btn-warning")
        console.log('tst')
    }
    else if (button.classList.contains("btn-warning")){
        button.classList.replace("btn-warning", "btn-secondary")
    }
}