import asyncio
from pyrogram import Client
import requests
import random

IMG_URL = 'https://imgs.search.brave.com/PBR49CmBXq8BqXnvTK6CvlPAvXt-Ugb-iRmbN_hcF2c/rs:fit:500:0:0/g:ce/aHR0cHM6Ly9pbWFn/ZXMuY3RmYXNzZXRz/Lm5ldC9ocmx0eDEy/cGw4aHEvNnpSR1pu/MjFxekVOd2Rkdlcz/Wmd0Ti8zMzQ5NmZj/ZDM2YTg5MWE2Mzcw/NGFmNzJjNzMzNDVl/NC9Ib2xpLVRodW1i/LmpwZw'

app = Client("my_bot")

async def main():
    async with app:
        await send_media(app)
    
async def send_media(app):
    # Replace 'https://example.com/image.jpg' with the actual URL of the image, here IMG_URL is defined above

    # for _ in range(10):
    #     x = random.randint(0,9)
    image_url = IMG_URL
    local_path = 'downloaded_image.jpg' #HERE WO PATH DENGE JAHAN PAR DOWNLOADED FILE KO BHEJNA HAI 
    caption = "I sent you the photo."

    # Download the image from the URL:
    response = requests.get(image_url)
    with open(local_path,'wb') as f: # 'wb' means ki BINARY WRITE form me file ko open krrhe hai
        f.write(response.content)           #i.e when working with images, to ensure no charecter conversion occur

    # There is another Method for downloading Image file and storing it locally
    # async with app.get_file(image_url) as file:
        # await file.download()

    # Send the downloaded photo to the bot owner (you) using your user ID
    await app.send_photo("@sspark_33" , photo=local_path, caption=caption)

asyncio.run(main())