import requests

def download_files(url):
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        print("Downloading...")
        with open('c:/Users/HRUTHVIK/Destop/'+local_filename, 'wb') as f:
            print("Writing data to file")
            for chunk in r.iter_content(chunk_size=1024):
                f.write(chunk)
    f.close()
    print("Download complete")
    print("File saved as "+ local_filename)

while 1:
    print("Welcome to the image downloader")
    image_url = input(str("Image url : "))
    download_files(image_url)
    print("")
