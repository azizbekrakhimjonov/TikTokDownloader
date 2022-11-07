def tk(link):
    import requests

    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url": link}

    headers = {"X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com",
        "X-RapidAPI-Key": "ac4cc9fd65mshef9ecd072aeb911p1cba1djsn75e88102fd2d"}

    response = requests.request("GET", url, headers=headers, params=querystring)
    result = response.json()
    return {"video": result['video'][0], "music": result['music'][0]}
# link = "https://www.tiktok.com/@nor10122/video/7037155617491913986"
# k = tk("https://www.tiktok.com/@nor10122/video/7037155617491913986")
# print(k)