let btn1 = document.querySelector('#btn1');
let btn2 = document.querySelector('#btn2');
let list = document.querySelectorAll('.list .review');
let curr_item = 2;

/*
 * Define an event listener for the "Show sMore" button
 * which is evoked by user's keyboard/mouse click
 */
btn1.addEventListener('click', (event) => {
    btn2.style.display = 'table';
    for (let i = curr_item; i < curr_item + 2; i++) {
        if (list[i]) {
            list[i].style.display = 'block';
        }
    }
    curr_item += 2;

    // this button will disappear after list fully loaded
    if (curr_item >= list.length) {
        event.target.style.display = 'none';
    }
})

/*
 * Define an event listener for the "Show Less" button
 * which is evoked by user's keyboard/mouse click
 */
btn2.addEventListener('click', (event) => {
    btn1.style.display = 'table';
    for (let i = curr_item; i >= curr_item - 2; i--) {
        if (list[i]) {
            list[i].style.display = 'none';
        }
    }
    curr_item -= 2;

    // this more button will disappear if there are only two items left shown
    if (curr_item <= 2) {
        event.target.style.display = 'none';
    }
})