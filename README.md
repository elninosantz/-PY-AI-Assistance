# PY-AI Assistance

PY-AI Assistance é um assistente de IA focado em **programação com
Python**.

A aplicação utiliza **Streamlit** para a interface e **Groq LLM** para
geração de respostas.\
A ideia do projeto é funcionar como um pequeno mentor técnico que ajuda
desenvolvedores a entender conceitos de programação, analisar código e
resolver dúvidas.

------------------------------------------------------------------------

## Deploy

A aplicação está disponível em:

https://dxzeahnbsl9xpx3r4wrjrd.streamlit.app/

------------------------------------------------------------------------

## Tecnologias utilizadas

-   Python
-   Streamlit
-   Groq API
-   Modelos LLM compatíveis com Groq

------------------------------------------------------------------------

## Estrutura do projeto

    .
    ├── app.py
    ├── groq_config.py
    ├── .gitignore
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------


---

## Arquitetura da aplicação

A aplicação segue uma arquitetura simples dividida em três partes:

### Interface (UI)

Responsável pela interação com o usuário utilizando Streamlit.

Principais componentes:

- `st.chat_input`
- `st.chat_message`
- `st.sidebar`
- `st.session_state`

Arquivo principal:

`app.py`

A interface também controla:

- histórico de conversa
- renderização das mensagens
- entrada da API Key

:contentReference[oaicite:0]{index=0}

---

### Lógica da aplicação

Responsável por controlar o fluxo da conversa e preparar os dados enviados para a LLM.

Principais funções:

- criação do cliente Groq
- captura da mensagem do usuário
- montagem do contexto da conversa
- controle de histórico

Arquivo:

`groq_config.py`



---

### Integração com LLM

A comunicação com a LLM ocorre através da **Groq API**.

#### Fluxo da requisição:
Usuário</br>
↓
</br>Streamlit Chat</br>
↓
</br>Construção do contexto da conversa</br>
↓
</br>Groq Client</br>
↓
</br>Modelo LLM</br>
↓</br>
Resposta exibida no chat

------------------------------------------------------------------------

## Como executar localmente

Clone o repositório:

    git clone https://github.com/elninosantz/-PY-AI-Assistance.git

Entre na pasta:

    cd -PY-AI-Assistance

Instale as dependências:

    pip install -r requirements.txt

Execute o projeto:

    streamlit run app.py

------------------------------------------------------------------------

## Configuração da API

Para usar o assistente é necessário uma **API Key da Groq**.

Crie uma conta em:

https://console.groq.com

Depois insira sua **API Key na barra lateral da aplicação**.

------------------------------------------------------------------------

## Objetivo do projeto

Este projeto foi criado para estudar:

-   integração de aplicações Python com LLMs
-   construção de interfaces com Streamlit
-   engenharia de prompts
-   desenvolvimento de assistentes de programação

------------------------------------------------------------------------

## Autor

El Nino Santz

GitHub: https://github.com/elninosantz