<%inherit file="template_base.mako"/>
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
<%block name='header'>
            <div class="middle">
                <div class="form_login">
                    <div class="head_login">Login in</div>
                    <form action="/log" method="post">
                        ${render_field(form.login, class_='input_text')}
                        ${render_field(form.pass1, class_='input_text')}
                        <button class="btn btn-primary" type=submit>Login</button>
                    </form>
                </div>
            </div>
</%block>