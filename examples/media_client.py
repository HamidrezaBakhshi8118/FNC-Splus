import asyncio
from pathlib import Path
from fnc_splus import Client

CHAT_ID = 'me'
PHOTO = Path('photo.jpg')
VIDEO = Path('video.mp4')


async def main():
    # This example sends only to CHAT_ID when you explicitly run it.
    async with Client('personal', data_dir='sessions') as client:
        await client.send_photo(CHAT_ID, PHOTO, caption='کپشن عکس')
        await client.send_video(CHAT_ID, VIDEO, caption='کپشن فیلم')


if __name__ == '__main__':
    asyncio.run(main())
