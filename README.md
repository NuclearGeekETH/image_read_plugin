# Image Interpreter ChatGPT Plugin Quickstart

This quickstart guide will help you set up and run a ChatGPT plugin that utilizes [Pharmapsychotic's Clip Interrogator](https://twitter.com/pharmapsychotic) to generate an image description that you can interact with using the [Replicate API](https://replicate.com/). This plugin has been made in alliance with the [ChatGPT plugins documentation](https://platform.openai.com/docs/plugins). If you do not already have plugin developer access, please [join the waitlist](https://openai.com/waitlist/plugins).

## Setup locally

To install the required packages for this plugin, run the following command:

```bash
pip install -r requirements.txt
```

Setup your .env file:

1. In your project root, create a new file and name it .env.
2. Open the .env file.
3. Add your Replicate API Key in the following way:

```bash
REPLICATE_API_TOKEN="YOUR_REPLICATE_API_TOKEN"
```
4. Make sure you replace YOUR_REPLICATE_API_TOKEN with your actual Replicate Key.
5. Save the .env file.

To run the plugin, enter the following command:

```bash
python main.py
```

Once the local server is running:

1. Navigate to https://chat.openai.com. 
2. In the Model drop down, select "Plugins" (note, if you don't see it there, you don't have access yet).
3. Select "Plugin store"
4. Select "Develop your own plugin"
5. Enter in `localhost:5003` since this is the URL the server is running on locally, then select "Find manifest file".

Voila! Your Image Interpreter plugin should now be installed and enabled. You can test it by prompting it with: Give me a description of: https://i.imgur.com/F0QXNQp.jpeg.

## Setup remotely

### Cloudflare workers

### Code Sandbox

### Replit

## Getting help

If you run into issues or have questions building a plugin, please join our [Developer community forum](https://community.openai.com/c/chat-plugins/20).
