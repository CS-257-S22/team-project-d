let btn = document.querySelector('.usage_btn');
let content = document.querySelector('.usage_content');

/*
 * Define an event listener for the "usage open" button
 * which is evoked by user's keyboard/mouse click. If
 * the content is shown and the user clicks this button,
 * it closes the content. Does the reverse if otherwsie.
 */
btn.addEventListener('click', (event) => {
    if(content.style.display == 'block') {
        content.style.display = 'none';
        btn.innerHTML = "USAGE (click to open):";
    } else {
        content.style.display = 'block';
        btn.innerHTML = "USAGE (click to close):";
    }
})