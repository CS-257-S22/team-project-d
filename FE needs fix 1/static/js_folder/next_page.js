let list = document.querySelectorAll('.wrap .ic_box');
let page_size = 9;
let page = [0, page_size - 1];
let next_btn = document.querySelector('.next')
let prev_btn = document.querySelector('.prev')

if(page_size >= list.length) {
    next_btn.style.display = 'none';
}

for(let i = 0; i < page_size; i++) {
    list[i].style.display = 'block';
}

/*
 * Delete the item conatined in the input page
 * Params: page - an array of two elements which indicate the 
 * start and end indecies of the current page
 */
function erase_items(page) {
    let upper = Math.min(list.length - 1, page[1])
    for(let i = page[0]; i <= upper; i++) {
        list[i].style.display = 'none';
    } 
}

/*
 * Displays the item conatined in the input page
 * Params: page - an a rray of two elements which indicate the 
 * start and end indecies of the current page
 */
function show_items(page) {
    let upper = Math.min(list.length - 1, page[1])
    for(let i = page[0]; i <= upper; i++) {
        list[i].style.display = 'block';
    }
}

/*
 * Define an event listener for the "next pages" button
 * which is evoked by user's keyboard/mouse click
 */
next_btn.addEventListener('click', event => {
    prev_btn.style.display = 'block';
    erase_items(page);
    if(page_size < list.length) {
        page = page.map(x => x + page_size);
    }
    show_items(page);

    if (page[1] >= list.length - 1) {
        event.target.style.display = 'none';
    }
})

/*
 * Define an event listener for the "prev page" button
 * which is evoked by user's keyboard/mouse click
 */
prev_btn.addEventListener('click', event => {
    next_btn.style.display = 'block';
    erase_items(page);
    if(page[0] > 0) {
        page = page.map(x => x - page_size); 
    }
    show_items(page);

    if (page[0] < page_size) {
        event.target.style.display = 'none';
    }
})