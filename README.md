# my_AI

This Python script that implements a Telegram chatbot based on ChatGPT. The chatbot is designed to respond to user messages and generate images based on prompts.

## Prerequisites

Before running the script, make sure you have the following dependencies installed:

- Python 3.x
- `python-telegram-bot` library
- `configparser` library
- `requests` library
- OpenAI Python library (`openai`)

You can install the required dependencies using the following command:

```
pip install python-telegram-bot configparser requests openai
```

## Setup

1. Clone the repository and navigate to the project directory.

2. Obtain the Telegram access token for your bot. You can create a new bot and obtain the access token from the [Telegram BotFather](https://core.telegram.org/bots#botfather).

3. Create a `config.ini` file in the project directory and add the following content:

   ```
   [TELEGRAM]
   ACCESS_TOKEN_GPT = <YOUR_TELEGRAM_ACCESS_TOKEN>
   ```

4. Set up the OpenAI API key. Make sure you have an OpenAI API key with access to the ChatGPT model. Set the API key as an environment variable with the name `OPENAI_API_KEY`.

5. Optionally, you can customize the AI models used for text generation and image generation by modifying the `new_model` and `pic_model` variables in the script.

## Usage

Run the script using the following command:

```
python script_name.py
```

Once the script is running, you can interact with the Telegram bot by sending messages to it. The bot will respond to your messages and generate images based on prompts starting with the prefix `genImg:`.

## Functionality

The script provides the following functionality:

- Responds to user messages: The bot uses the ChatGPT model to generate responses to user messages. The responses are translated using the OpenAI API.
- Generates images: The bot can generate images based on prompts provided by the user. It uses the OpenAI API to generate the images.

## Commands

The bot supports the following commands:

- `/start`: Initializes the conversation with the bot.
- `/help`: Provides information on how to use the bot.

## Limitations

- The script currently uses the default ChatGPT model (`gpt-4`) and the default image generation model (`davinci`). You can modify these models in the script according to your needs.
- The script relies on the OpenAI API for text generation and image generation. Make sure you have the necessary API access and quota.
- The script runs indefinitely in a loop, continuously listening for new messages. You may need to handle stopping the script manually.

## Contributions

Contributions to the project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
The script relies on the OpenAI API for text generation and image generation. Make sure you have the necessary API access and quota.
The script runs indefinitely in a loop, continuously listening for new messages. You may need to handle stopping the script manually.
Contributions
Contributions to the project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. 
