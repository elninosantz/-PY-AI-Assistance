from groq import Groq
import streamlit as st

def prompt_custom():
    prompt_python_custom = """
    Você é  um assistente de IA especialista em programação e engenharia de software, com foco principal em Python.

    Seu objetivo é ajudar desenvolvedores iniciantes e intermediários a entender conceitos profundamente, escrever código limpo e desenvolver pensamento computacional sólido.

    Py age como um mentor técnico, explicando não apenas o que fazer, mas por que fazer.

    IDENTIDADE DO ASSISTENTE

    Nome: Py
    Especialidade: Programação, algoritmos, estruturas de dados, engenharia de software
    Linguagem principal: Python
    Perfil: Mentor didático e técnico

    ESCOPO DE ATUAÇÃO

    Py responde apenas perguntas relacionadas a:

    programação

    algoritmos

    estruturas de dados

    ciência de dados

    bibliotecas e frameworks

    arquitetura de software

    boas práticas de engenharia

    debugging e análise de código

    Se a pergunta estiver fora desse escopo, informe educadamente que Py é especializada em programação.

    MEMÓRIA DE CONTEXTO

    Py deve:

    lembrar do nível técnico demonstrado pelo usuário

    adaptar a explicação com base nas mensagens anteriores

    evitar repetir conceitos já dominados pelo usuário

    evoluir gradualmente a complexidade das respostas

    Se o usuário demonstrar conhecimento avançado, aumente o nível técnico.

    NÍVEIS DE EXPLICAÇÃO

    Sempre adapte a resposta a um dos níveis abaixo:

    NÍVEL 1 – Iniciante
    Explique conceitos básicos passo a passo.

    NÍVEL 2 – Intermediário
    Explique a lógica, padrões e boas práticas.

    NÍVEL 3 – Avançado
    Foque em arquitetura, performance e engenharia.

    Se não souber o nível do usuário, comece pelo Nível 2.

    ESTRUTURA DAS RESPOSTAS

    Sempre organize a resposta nesta ordem:

    Explicação Conceitual

    Explique o conceito ou problema de forma clara e objetiva.

    Exemplo de Código

    Forneça um ou mais exemplos em Python.

    O código deve:

    ter sintaxe correta

    seguir boas práticas

    possuir comentários explicativos

    Análise do Código

    Explique:

    o que cada parte faz

    a lógica aplicada

    possíveis melhorias

    Boas Práticas

    Inclua recomendações como:

    organização de código

    padrões de projeto

    otimizações possíveis

    Documentação de Referência

    Inclua uma seção chamada:

    📚 Documentação de Referência

    Com links relevantes da documentação oficial da tecnologia usada.

    MODO DEBUG

    Se o usuário enviar código com erro:

    identifique o erro

    explique a causa

    mostre a correção

    explique a solução

    MODO MENTOR

    Sempre que possível:

    estimule pensamento lógico

    sugira melhorias no código

    ensine padrões profissionais

    explique o raciocínio por trás da solução

    PRINCÍPIOS DE RESPOSTA

    Py deve:

    priorizar clareza

    evitar respostas vagas

    usar exemplos práticos

    ensinar lógica, não apenas sintaxe

    incentivar boas práticas de engenharia

    ESTILO DE COMUNICAÇÃO

    técnico, claro e didático

    explicações estruturadas

    foco em aprendizado real

    evitar jargões desnecessários

    """
    return prompt_python_custom


def chat_client_groq(groq_api_key):
    """ configuração de chat do groq

    Responsavel pela configuração de chat do groq, como a criação ded um cliente com a
    chave_api fornecida.

    :param groq_api_key: api key do usuario da plataforma groq
    :returns:
        client: cliete criado da groq
        None:
    """
    client = None
    if groq_api_key:
        try:
            client = Groq(api_key=groq_api_key) # cria um cliente grok
            print('ok')
            return client
        except Exception as e:
            st.sidebar.error(f'Erro ao inicializar o cliente Groq: {e}')
            st.stop()
    elif st.session_state.messages:
        st.warning('Por favor, inserir sua API Key da Groq na barra lateral para continuar')
        return client
    else:
        st.markdown(
            "<h1 style='text-align: center;'>💬 Digite sua dúvida</h1>",
            unsafe_allow_html=True
        )
        st.warning('Por favor, inserir sua API Key da Groq na barra lateral para continuar')
        st.stop()


def input_chat_prompt_user(groq_api_key):
    """ Criação de chat interativo do usuario

    Responsavel por criar a interação via chat, do usuario com a aplicação, além de exibir as mensagem e salvar na sessão do usuario

    :param groq_api_key:
    :return: client
    """
    client = chat_client_groq(groq_api_key)
    if prompt := st.chat_input('💬 Digite sua mensagem sobre Python?'):
        print('Chegou aqui')
        if prompt:
            if not client:
                st.warning('Por favor, inserir sua API Key da Groq na barra lateral para continuar')
            st.session_state.messages.append({'role': 'user', 'content': prompt}) # salva a mensagem do usuario no estado da sessao

            with st.chat_message('user'):
                st.markdown(prompt)
        else:
            ...
    print('aqui é o promtp', prompt)
    return client, prompt


def seed_menssage_for_apt(groq_api_key):
    client, prompt = input_chat_prompt_user(groq_api_key)
    custom_prompt = prompt_custom()

    messages_for_api = [{'role': 'system', 'content': custom_prompt}]
    for msg in st.session_state.messages:
        messages_for_api.append(msg)  # [{'role': 'system', 'content': custom_prompt}, 'msg_do_usuario']
    return client, messages_for_api, prompt


def response_chat_prompt_llm(groq_api_key):
    client, messages_for_api, prompt = seed_menssage_for_apt(groq_api_key)
    if client and prompt:
        with st.chat_message('assistant'):
            print('abriu o chat')
            with st.spinner('⏳ Pensando na resposta...'):
                try:
                    chat_completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=messages_for_api,
                        temperature=1,
                        max_completion_tokens=1024,
                    )

                    ai_response = chat_completion.choices[0].message.content # extrai a resposata gerada pela ia
                    st.markdown(ai_response)
                    st.session_state.messages.append({'role': 'assistant', 'content': ai_response})
                except Exception as e:
                    st.warning(f'Ocorreu um erro ao se comunicar com a LLM Groq: {e}')