from openai import OpenAI
import os
openai = OpenAI(api_key = os.environ['generate_image_key'])

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
