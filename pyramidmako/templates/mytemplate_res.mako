<%inherit file="template_base.mako"/>
<%block name='result'>
    <div class="main_box_left">
        <div class="name_product">
            ${name}
        </div>
        <div class="box_photo">
            <img src="${request.static_path('pyramidmako:static/img/img_demo.jpg')}" alt="img_demo"/>
        </div>
    </div>
    <div class="main_box_right">
        <div class="compare_box">
            <a href="${ allegro['url']}">
                <img src="${request.static_path('pyramidmako:static/img/logo_allegro.png')}" alt="logo_allegro"/>
                <div class="${allegro['comparison']}">
                    %if allegro['status']:
                        ${"%s" % allegro['status']}
                    %else:
                        ${"Cena: %.2f" % allegro['price']}
                    %endif
                </div>
            </a>
        </div>
        <div class="compare_box">
            <a href="${nokaut['url']}">
                <img src="${request.static_path('pyramidmako:static/img/logo_nokaut.png')}" alt="logo_nokaut"/>
                <div class="${nokaut['comparison']}">
                    %if nokaut['status']:
                        ${"%s" % nokaut['status']}
                    %else:
                        ${"Cena: %.2f pln" % nokaut['price']}
                    %endif
                </div>
            </a>
        </div>
    </div>
</%block>