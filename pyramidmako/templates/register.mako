<%inherit file="base.mako"/>
<%namespace name="comp" file="components.mako"/>
<%block name='header'>
    <div class="form_login">
        <div class="head_login">Register</div>
        <form action="/register" method="post">
            ${comp.render_field(form.login, class_='input_text')}
            ${comp.render_field(form.pass1, class_='input_text')}
            ${comp.render_field(form.pass2, class_='input_text')}
            <button class="btn btn-primary" type=submit>Register</button>
        </form>
    </div>
</%block>
