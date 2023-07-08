// Select all elements with class "bingo-card__item"
var bingoItems = document.querySelectorAll(".bingo-card__item");

// Add event listener to each element
bingoItems.forEach(function(item) {
    item.addEventListener("click", function() {
        // Toggle the "active" class on click
        this.classList.toggle("active");
    });
});

// Select the clear button element
var clearButton = document.querySelector(".clear-button");

// Add event listener to the clear button
clearButton.addEventListener("click", function() {
    // Remove the "active" class from all bingo items
    bingoItems.forEach(function(item) {
        item.classList.remove("active");
    });
});
