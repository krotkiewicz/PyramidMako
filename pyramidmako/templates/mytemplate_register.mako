<%inherit file="template_base.mako"/>
<%block name='header'>
    <div class="form_login">
        <div class="head_login">Register</div>
        <form action="/reg" method="post">
            <input class="input_text" type="text" name='name' placeholder="login"/>
            <input class="input_text" type="password" name='pass' placeholder="password"/>
            <input class="input_text" type="password" name='pass2' placeholder="password"/>
            <button class="btn btn-primary" type=submit>Register</button>
        </form>
    </div>
</%block>