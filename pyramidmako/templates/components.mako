<%def name="render_field(field, **kwargs)">
  <dt>${field.label}
  <dd>${field(**kwargs)}
  % if field.errors:
    <ul class=errors>
    % for error in field.errors:
      <li class='my_error'>${error}</li>
    % endfor
    </ul>
  % endif
  </dd>
</%def>