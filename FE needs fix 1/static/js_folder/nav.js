let elem_list = document.getElementsByTagName("*");

function include_html() {
    for (let i = 0; i < elem_list.length; i++) {
        let elem = elem_list[i];
        // look for an element with the attribute
        let file = elem.getAttribute("html_included");
        if (file) {
            // make an HTTP request using the attribute value as the file name
            let xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4) {
                    if (this.status == 200) {
                        elem.innerHTML = this.responseText;
                    } 
                }
            }      
            xhttp.open("GET", file, true);
            xhttp.send();
            return;
        }
    }
};

include_html();