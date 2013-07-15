<%inherit file="base.mako"/>

<%block name='result'>
    <div class="main_box_left">
        <div class="name_product">
            ${entry.name}
        </div>
        <div class="box_photo">
            <img src="${request.static_path('pyramidmako:static/img/img_demo.jpg')}" alt="img_demo"/>
        </div>
    </div>
    <div class="main_box_right">
        <div class="compare_box">
            <a href="${entry.url_allegro}">
                <img src="${request.static_path('pyramidmako:static/img/logo_allegro.png')}" alt="logo_allegro"/>
            </a>
                <div class="price${' win' if entry.price_allegro < entry.price_nokaut and entry.price_allegro else ''}">
                    %if entry.status_allegro:
                        ${entry.status_allegro}
                    %else:
                        Cena: ${entry.price_allegro} pln
                    %endif
                </div>
        </div>
        <div class="compare_box">
            <a href="${entry.url_nokaut}">
                <img src="${request.static_path('pyramidmako:static/img/logo_nokaut.png')}" alt="logo_nokaut"/>
                </a>
                <div class="price${' win' if entry.price_allegro > entry.price_nokaut and entry.price_nokaut else ''}">
                    %if entry.status_nokaut:
                        ${entry.status_nokaut}
                    %else:
                       Cena:  ${entry.price_nokaut} pln
                    %endif
                </div>
        </div>
    </div>
</%block>
