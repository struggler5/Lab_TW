function OnDeleate() {
    let decision = confirm("Are you sure you want to delete this?");

    if (decision) {
        console.log("User clicked Yes!");
        // Put your 'Yes' logic here
    } else {
        console.log("User clicked No.");
    }
}


function Construction(){
    alert("Website still under construction! ");
}

const button = document.querySelector('.btn');

const applyGradient = () => {
  button.style.backgroundImage = 'linear-gradient(45deg, #f3bc2e, #f041ff)';
};

const removeGradient = () => {
  button.style.backgroundImage = 'none';
  button.style.backgroundColor = '#333';
};

button.addEventListener('mouseenter', applyGradient);
button.addEventListener('mouseleave', removeGradient);
