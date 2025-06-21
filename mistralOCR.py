import requests

def extract(image_path):
 url = "https://admin.tomedes.com/api/v2/image-to-text/mistralocr"
 headers = {
  "api-key": "pDwCjq7CyeAmn1Z3osNunACg2U0SLIhwBTtsp1WqYFMf5UuSIvMBYGS4pt8OIsGMH",
  "authorization": "Bearer null"
 }

 try:
  with open(image_path, 'rb') as img_file:
   files = {'image[]': (image_path.split('/')[-1], img_file, 'image/png')}
   data = {'share_id': '6da58dd2-1733-4ee1-8e32-bccb2d9188f6'}
   response = requests.post(url, headers=headers, files=files, data=data)
   if response.status_code == 200:
    result = response.json()
    return result['result']['result']['mistralocr'][0]['text']
   else:
    print(f"Error API: {response.status_code} - {response.text}")
    return None
 except Exception as e:
  print(f"Error al procesar la imagen: {e}")
  return None
