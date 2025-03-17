import streamlit as st
import streamlit_authenticator as stauth

COOKIE_EXPIRY_DAYS = 30
def main():
    authenticator = stauth.Authenticate(
        {'username': {'teste': {'name': 'testando', 'password': 'blabla'}}},
        'random_cookie_name',
        'random_signature_key',
        COOKIE_EXPIRY_DAYS,
    )
    if 'clicou_registrar' not in st.session_state:
        st.session_state['clicou_registrar'] = False
    if st.session_state['clicou_registrar'] == False:
        login_form(autheticator=authenticator)

def login_form(autheticator):
    name, authetication_status, username = autheticator.login('Login')
    if authetication_status:
        autheticator.logout('Logout', main)
        st.title('Area do Dashboard')
        st.write(f'*{name} está logado(a)')
    elif authetication_status == False:
        st.error('Usuário/Senha inválidos')
    elif authetication_status == None:
        st.warning('Por favor informe um usuário e senha')
        clicou_em_registrar = st.button('Registrar')
        if clicou_em_registrar:
            st.session_state['clicou_registrar'] = True
            st.rerun()

def confirm_msg():
    hashed_password = stauth.Hasher([st.session_state.pswrd]).generate()
    if st.session_state.pswrd != st.session_state.confirm_pswrd:
        st.warning('Senhas não conferem')
    elif 'consulta_nome()':
        st.warning('Nome de usuário já existe!')
    else:
        'add_registro()'
        st.success('Registro Efetuado!')


def user_form():
    with st.form(key='formulario', clear_on_submit=True):
        nome = st.text_input('Nome', key='nome')
        username = st.text_input('Username', key='username')
        password = st.text_input('Senha', key='pswrd', type='password')
        confirm_password = st.text_input('Confirme a senha', key='confirm_pswrd', type='password')
        submit = st.form_submit_button('Salvar', on_click=confirm_msg)
        clicou_em_fazer_login = st.button('Fazer Login')
        if clicou_em_fazer_login:
            st.session_state['clicou_registrar'] = False
            st.rerun()

if __name__ == '__main__':
    main()