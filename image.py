import requests
r = requests.post(
    "https://api.deepai.org/api/nsfw-detector",
    files={
        'image': open('/root/Downloads/SocialScraper/NSFW-detection/nsfw_data_scraper/data/test/sexy/1b4c326b-ec1f-4374-a201-8b8bda3de168.jpg', 'rb'),
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())
