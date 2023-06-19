import requests

url = "http://localhost:10046/ai-server/ocr"
file_path = 'E:\\code\\java\\project-litongjava\\ai-server\\ai-server-service\\resources\\flight_ticket.jpg'
file_bytes = open(file_path, 'rb')

payload = {}

files = [
    ('file', (file_path, file_bytes, 'image/jpeg'))
]

headers = {
}
response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
