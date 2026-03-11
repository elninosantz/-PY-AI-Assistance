import os
import streamlit as st
from groq import Groq
from groq_config import response_chat_prompt_llm

def config_page_view():
    """ configuração principal da application

    Configuração principal da application, eventos, estilos e etc.

    :return: None
    """
    st.set_page_config(
        page_title='PY Assistance',
        page_icon='👽',
        layout='wide', # amplo
        initial_sidebar_state='expanded', # já começa expandida
    )


def sidebar_personal_view():
    """ Personalização do sidebar da pagina

    Utilizando markdown + html, para estilização da pagina, além de metodos do streamlit.

    :return: groq_api_key
    """

    config_page_view()

    st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            border-right: 1px solid rgba(255,255,255,0.08);
        }

        section[data-testid="stSidebar"] .block-container {
            padding-top: 2rem;
            padding-bottom: 1.5rem;
        }

        .alex-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.08);
            padding: 14px 16px;
            border-radius: 16px;
            margin-bottom: 14px;
        }

        .alex-muted {
            color: #B8BCC8;
            font-size: 0.92rem;
            line-height: 1.45;
        }

        .alex-footer {
            color: #8E93A5;
            font-size: 0.82rem;
            text-align: center;
            margin-top: 0.8rem;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("## 👽 PY-AI Assistance")
        st.caption("Seu assistente pessoal focado em desenvolvimento com a linguagem de programação python")

        st.markdown('<div>', unsafe_allow_html=True)

        groq_api_key = st.text_input(
            "Insira sua API Key da Groq",
            type="password",
        )
        st.markdown('</div>', unsafe_allow_html=True)

        with st.expander("Como obter sua API Key da Groq"):
            st.markdown("""
            1. Acesse a plataforma Groq  
            2. Faça login ou crie sua conta  
            3. Gere uma nova API Key  
            4. Copie a chave e cole aqui no campo acima
            """)
            st.link_button(
                "Abrir tutorial",
                "https://www.notion.so/Como-criar-uma-API-Key-no-Groq-31fa921422478035b48dc5aa44e1f179?source=copy_link",
                width="stretch"
            )

        st.markdown('<div class="alex-card alex-muted">'
                    'Assistente pessoal e personalizado para ajudar iniciantes a aprender Python de forma mais prática.'
                    '</div>', unsafe_allow_html=True)

        st.link_button(
            "📞 Entrar em Contato",
            "https://www.linkedin.com/in/elninosantz/",
            use_container_width=True
        )

        st.markdown(
            '<div class="alex-footer">Desenvolvido por <a href="https://github.com/elninosantz">Elninosantz</a></div>',
            unsafe_allow_html=True
        )

    return groq_api_key


def config_state_message():
    """ configuração da memória de estado

    configuração da mememoria de estado do usuario, para guardar o historico de mensagens entre
    assistente IA e Usuario

    :return: None
    """
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    for message in st.session_state.messages:
        with st.chat_message(message['role']):
            st.markdown(message['content'])


def main_page_custom():
    """ customização da página principal da aplicação

    Responsavel pela customização e importação da memoria de estado do usuairo

    :return: api_key_groq
    """
    api_key_groq = sidebar_personal_view()
    config_state_message()
    response_chat_prompt_llm(api_key_groq)

if __name__ == '__main__':
    main_page_custom()

