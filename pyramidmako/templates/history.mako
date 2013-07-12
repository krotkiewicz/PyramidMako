<%inherit file="base.mako"/>
<%block name='result'>
<table cellpadding="0" celllspacing="0" border="0" class="list">
    <td class="thumb"></td>
        <td class="name_list" >Name</td>
        <td class="price_list_header">Price <br>allegro</td>
        <td class="price_list_header">Price <br>nokaut</td>
        <td class="price_list_header">Number<br>of visits</td>
        <td class="price_list_header">Creation<br> date</td>
        <td class="more"></td>
    %for row in history:
    <tr>
        <td class="thumb"><img src="http://image.ceneo.pl/data/products/401968/f-philips-gc-4410.jpg" alt="img_demo"/></td>
        <td class="name_list">${row.name}</td>
        <td class="price_list">${row.price_allegro}</td>
        <td class="price_list">${row.price_nokaut}</td>
        <td class="price_list">${row.count}</td>
        <td class="date_list">${row.date.ctime()}</td>
        <td class="more"><a href="/res?product=${row.name}" class="link_more btn">Open</a></td>
    </tr>
    %endfor
</table>
</%block>