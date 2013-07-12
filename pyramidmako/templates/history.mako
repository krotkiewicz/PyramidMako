<%inherit file="base.mako"/>
<%block name='result'>
<table cellpadding="0" celllspacing="0" border="0" class="list">
    %for row in history:
    <tr>
        <td class="thumb"><img src="http://image.ceneo.pl/data/products/401968/f-philips-gc-4410.jpg" alt="img_demo"/></td>
        <td class="name_list">${row.name}</td>
        <td class="price_list">Allegro: ${row.price_allegro}</td>
        <td class="price_list">Nokaut: ${row.price_nokaut}</td>
        <td class="more"><a href="/res?product=${row.name}" class="link_more btn">Zobacz</a></td>
    </tr>
    %endfor
</table>
</%block>