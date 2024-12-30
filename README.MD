# BTC-USD + Fees
![Bot Telegram](./img/imgbot.png)
Este projeto consiste em um bot do Telegram que fornece atualizações periódicas sobre o preço do Bitcoin (BTC) e as taxas de transação de Bitcoin em diferentes intervalos de tempo, consultando APIs de taxas da mempool.

O bot é configurado para enviar essas informações diretamente para um chat do Telegram **a cada 1 hora**, ajudando os usuários a monitorar o preço do Bitcoin e as taxas de transação de maneira automatizada.

## Funcionalidades

- **Consulta de Preço do Bitcoin**: Obtém o preço atual do BTC em USD.
- **Consulta de Taxas de Mempool**: Obtém as taxas de transação mais rápidas e médias para 30 minutos e 1 hora, baseadas na Mempool.
- **Envio de Atualizações no Telegram**: Envia as informações **periodicamente (a cada 1 hora)** para um chat do Telegram.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação para o desenvolvimento do bot.
- **Requests**: Para realizar chamadas HTTP às APIs.
- **Telegram API**: Para enviar mensagens no Telegram.
- **Asyncio**: Para execução assíncrona das funções e para gerenciar as chamadas às APIs.
- **dotenv**: Para gerenciar variáveis de ambiente de forma segura.

## Requisitos

- Python 3.x instalado.
- As bibliotecas mencionadas abaixo.

## Como Rodar o Projeto Localmente

1. Clone o repositório:

    ```bash
    git clone https://github.com/DanielCosta12/btc_usd_fees.git
    cd btc_usd_fees
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate   # Para Linux/Mac
    venv\Scripts\activate      # Para Windows
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:

    ```
    TOKEN=<SEU_TOKEN_DO_BOT>
    CHAT_ID=<SEU_CHAT_ID_DO_TELEGRAM>
    BTC_API_URL=<URL_DA_API_DE_PREÇO_BTC>
    MEMPOOL_API_URL=<URL_DA_API_DE_TAXAS_MEMPOOL>
    ```

    - **TOKEN**: O token do seu bot do Telegram, que pode ser obtido ao criar um bot no [BotFather](https://core.telegram.org/bots#botfather).
    - **CHAT_ID**: O ID do chat onde as mensagens serão enviadas (você pode obter isso de diversas formas, uma delas é enviando uma mensagem para o bot e usando a API do Telegram para obter o `chat_id`).
    - **BTC_API_URL**: A URL de uma API pública que forneça o preço do Bitcoin em USD.
    - **MEMPOOL_API_URL**: A URL da API que fornece informações sobre as taxas de transação no mempool de Bitcoin.

5. Execute o bot:

    ```bash
    python bot.py
    ```

    O bot começará a rodar e enviará atualizações **a cada 1 hora** com o preço do Bitcoin e as taxas de transação.

## Deploy no Railway

Este projeto também pode ser facilmente implementado no Railway, uma plataforma de deploy que suporta Python e outras tecnologias. Para implementar o projeto no Railway, siga estas etapas:

1. Crie uma conta no [Railway](https://railway.app/).
2. Crie um novo projeto e conecte seu repositório GitHub ao Railway.
3. Configure as variáveis de ambiente no painel do Railway (`TOKEN`, `CHAT_ID`, `BTC_API_URL`, `MEMPOOL_API_URL`).
4. Faça o deploy clicando em "Deploy".

Com isso, o bot será executado automaticamente no Railway e você não precisará mantê-lo rodando localmente.

## Contribuindo

Se você deseja contribuir para o projeto, siga os seguintes passos:

1. Faça um fork deste repositório.
2. Crie uma branch para suas modificações (`git checkout -b feature/nome-da-sua-modificação`).
3. Commit suas alterações (`git commit -am 'Adiciona nova funcionalidade'`).
4. Push para a branch (`git push origin feature/nome-da-sua-modificação`).
5. Abra um pull request.

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
