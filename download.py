import httpx

def download_image(number):
    url = []
    for __ in range(number):
        response = httpx.get('https://picsum.photos/3840/2160', follow_redirects=True)
        temp_url = str(response.url)
        url.append(temp_url)
    return url
    