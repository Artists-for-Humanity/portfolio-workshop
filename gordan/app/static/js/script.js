// Get the modal

var modal = document.getElementById("myModal");
var closebutton = document.getElementsByClassName("close")[0];
var form = document.getElementsByClassName("contact-form")[0];

function openmodal() {
    console.log("OPEN");
    modal.style.display = "block";
}

function closemodal() {
    console.log("CLOSE");
    modal.style.display = "none";
}

form.addEventListener("submit", function (event) {
    var data = Object.fromEntries(new FormData(event.target));
    fetch('/formsubmit', {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-type': 'application/json'
        }
    }).then((response) => {
        return response.json();
    }).then((response) => {
        if (response.status == "success") {
            openmodal();
        }
        console.log(response);
    });
    event.preventDefault();
});

closebutton.addEventListener('click', () => {
    closemodal();
});