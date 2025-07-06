import requests

def extract(image_path):
 url = "https://admin.tomedes.com/api/v2/image-to-text/gemini"
 headers = {
  "api-key": "pDwCjq7CyeAmn1Z3osNunACg2U0SLIhwBTtsp1WqYFMf5UuSIvMBYGS4pt8OIsGMH",
  "authorization": "Bearer null"
 }

 try:
  with open(image_path, 'rb') as img_file:
   files = {'image[]': (image_path.split('/')[-1], img_file, 'image/png')}
   response = requests.post(url, headers=headers, files=files)

   if response.status_code == 200:
    result = response.json()
    result_data = result['result']['result']

    gemini_text = result_data.get('gemini', [{}])[0].get('text', '').strip()
    chatgpt_text = result_data.get('chatgpt', [{}])[0].get('text', '').strip()

    if gemini_text and gemini_text.lower() != "this source was unable to extract text from the image.":
     return gemini_text
    elif chatgpt_text and chatgpt_text.lower() != "this source was unable to extract text from the image.":
     return chatgpt_text
    else:
     return "No se pudo extraer texto de la imagen."
   else:
    print(f"Error API: {response.status_code} - {response.text}")
    return None
 except Exception as e:
  print(f"Error al procesar la imagen: {e}")
  return None
