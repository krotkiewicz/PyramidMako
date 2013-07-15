<%inherit file="base.mako"/>
<%namespace name="comp" file="components.mako"/>
<%block name='header'>
            <div class="middle">
                <div class="form_login">
                    <div class="head_login">Login in</div>
                    <form action="/login" method="post">
                        ${comp.render_field(form.login, class_='input_text')}
                        ${comp.render_field(form.pass1, class_='input_text')}
                        <button class="btn btn-primary" type=submit>Login</button>
                    </form>
                </div>
            </div>
</%block>