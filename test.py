import replicate
from dotenv import load_dotenv
import os

load_dotenv()

replicate.Client(api_token=os.environ["REPLICATE_API_TOKEN"])
model = replicate.models.get("pharmapsychotic/clip-interrogator")

def get_description(link):
    result = model.predict(image=link, clip_model_name='ViT-L-14/openai', mode='best')
    print(result)
    return(result)

link='https://i.imgur.com/F0QXNQp.jpeg'
get_description(link)
