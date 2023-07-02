import replicate
import quart
import quart_cors
from quart import request
from dotenv import load_dotenv
import os

load_dotenv()

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")
replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])
model = replicate.models.get("pharmapsychotic/clip-interrogator")

@app.post("/predict")
async def image_description():
    data = await request.get_json(force=True)
    link = data.get('url', None)
    print(link)
    if link is None:
        return 'URL of the image is required', 400
    result = model.predict(image=link, clip_model_name='ViT-L-14/openai', mode='best')
    return {'description': result}, 200

@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
