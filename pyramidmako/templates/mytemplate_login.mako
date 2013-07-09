<%inherit file="template_base.mako"/>
<%block name='header'>
            <div class="middle">
                <div class="form_login">
                    <div class="head_login">Login in</div>
                    <form action="/log" method="post">
                        <input class="input_text" type="text" name="login" placeholder="login"/>
                        <input class="input_text" type="password" name="password" placeholder="password"/>
                        <button class="btn btn-primary" type=submit>Login</button>
                    </form>
                </div>
            </div>
</%block>