<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
<head>
  <title>NOkautALLegro</title>
  <meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
  <meta name="keywords" content="python web application" />
  <meta name="description" content="pyramid web application" />
  <link rel="stylesheet" href="${request.static_path('pyramidmako:static/css/style.css')}">
</head>
<body>
    <div id="container">
        <div class="main_box">
            <div class="head">
                <div class="logo_img"><img src="${request.static_path('pyramidmako:static/img/logo.png')}" alt="logo"></div>
                <div class="logo_txt">
                    Compare products
                    <div class="logo_txt_small">We will help you find and compare products</div>
                </div>
                <div class="box_login">
                    <a class="btn btn-success" href="#register">Register</a>
                    <a class="btn" href="#login">Login</a>
                </div>
            </div>
            <div class="middle">
                <div class="box_search">
                    <form action="/res">
                        <div class="search">
                            <input type="text" name = "product" value=""/>
                        </div>
                        <button class="btn_search btn btn-primary" type=submit>Search</button>
                    </form>
                    <a class="btn" href="#">Historia wyszukiwania</a>
                    <div class="clear"></div>
                </div>
                ${self.body()}
            </div>
        </div>
        <div class="footer">
            <img src="${request.static_path('pyramidmako:static/img/logo_stx.png')}" alt="logo_stx"/>
        </div>
    </div>
    <script type="text/javascript" src="${request.static_path('pyramidmako:static/js/jquery-1.8.3.min.js')}"></script>
    <script type="text/javascript">
    $(document).ready(function() {
        var btn_search = $('.search input');
        btn_search.focus(function() {
            $(this).attr('value','');
        });
    });
    </script>
</body>
</html>








