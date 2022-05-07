document.write('\
<header>\
<h1>\
    <a class="a3" href="/"><i class="fas fa-ice-cream"></i>Quest for the Best Ice Cream<i class="fas fa-ice-cream"></i></a>\
</h1>\
</header>\
<ul class="nav">\
            <li class="item">\
                <h3>About Us</h3>\
                <p class="content">\
                    Welcome, ice cream enthusiasts! On this website, you can search through\
                    241 different ice creams from 4 brands: Ben and Jerry\'s, Haagen Dazs,\
                    Talenti, and Breyers. Click each brand below to get started.\
                </p>\
            </li>\
            <li class="item">\
                <h3>Editor\'s Choice</h3>\
                <ul class="content">\
                    <li><a class="a1" href="/ic_name=Salted Caramel Core">Salted Caramel Core</a></li>\
                    <li><a class="a1" href="/ic_name=White Chocolate Raspberry Truffle Ice Cream">White Chocolate Raspberry Truffle Ice Cream</a></li>\
                    <li><a class="a1" href="/ic_name=ALPHONSO MANGO SORBETTO">ALPHONSO MANGO SORBETTO</a></li>\
                    <li><a class="a1" href="/ic_name=Natural Vanilla">Natural Vanilla</a></li>\
                </ul>\
            </li>\
            <li class="item">\
                <h3>Seach in Categories</h3>\
                <div class="content">\
                    <div class="brand_search">\
                        <h4>Brand:</h4>\
                        <ul>\
                            <li><a class="a2" href="/feature=brand_search/input=bj">Ben & Jerry\'s</a></li>\
                            <li><a class="a2" href="/feature=brand_search/input=hd">Häagen-Dazs</a></li>\
                            <li><a class="a2" href="/feature=brand_search/input=talenti">Talenti</a></li>\
                            <li><a class="a2" href="/feature=brand_search/input=breyers">Breyers</a></li>\
                        </ul>\
                    </div>\
                    <div class="rating_search">\
                        <h4>Stars:</h4>\
                        <ul>\
                            <li>\
                                <a class="a2" href="/feature=rating_search/input=5.0">\
                                    5 star &nbsp;\
                                    {% for i in range(5): %}<i class="fa fa-star"></i>{% endfor %}\
                                </a>\
                            </li>\
                            <li>\
                                <a class="a2" href="/feature=rating_search/input=4.0">\
                                    4+ star\
                                    {% for i in range(4): %}<i class="fa fa-star"></i>{% endfor %}\
                                </a>\
                            </li>\
                            <li>\
                                <a class="a2" href="/feature=rating_search/input=3.0">\
                                    3+ star\
                                    {% for i in range(3): %}<i class="fa fa-star"></i>{% endfor %}\
                                </a>\
                            </li>\
                            <li>\
                                <a class="a2" href="/feature=rating_search/input=2.0">\
                                    2+ star\
                                    {% for i in range(2): %}<i class="fa fa-star"></i>{% endfor %}\
                                </a>\
                            </li>\
                            <li>\
                                <a class="a2" href="/feature=rating_search/input=1.0">\
                                    1+ star\
                                    <i class="fa fa-star"></i>\
                                </a>\
                            </li>\
                        </ul>\
                    </div>\
                    <br>\
                    <div class="rating_sort">\
                        <h4>Top Rated:</h4>\
                        <form id="sort_bar" action="feature=rating_sort">\
                            <label for="sort_bar">Sort by Ratings</label>\
                            <br>\
                            <input type="search" id="sort_bar" name ="input" placeholder="number of ice creams" autocomplete="off">\
                            <button>Go</button>\
                        </form>\
                    </div>\
                </div>\
            </li>\
            <li class="item">\
                <h3>Suggest Me Ice Cream</h3>\
                <div class="content">\
                    <p>Can\'t decide? We will pick one for you! Click the button.</p>\
                    <a class="a1" href="{{ random_ic_link }}">\
                        <button class="random_button">Press Here!</button>\
                    </a>\
                </div>\
            </li>\
            <li class="item">\
                <h3><i class="fas fa-search"></i></h3>\
                <form class="content last" id="form" action="feature=keyword_search">\
                    <label for="ic">Seach by Keys</label><br>\
                    <input class="btn" type="search" id="ic" name ="keyword" placeholder="keyword" autocomplete="off">\
                    <button class="btn">Search</button>\
                </form>\
            </li>\
</ul>\
');
