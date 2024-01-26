from openai import OpenAI
from keys import token_openai_crt_image

openai = OpenAI(api_key=token_openai_crt_image['TOKEN'])

def generate_image(prompt):
  response = openai.images.generate(
    model='dall-e-2',
    prompt=prompt,
    size='1024x1024',
    quality='standard',
    n=1,
  )
  
  image_url = response.data[0].url
  return image_url
