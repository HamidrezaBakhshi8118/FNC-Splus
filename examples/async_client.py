import asyncio
from fnc_splus import Client


async def main():
    async with Client('personal', data_dir='sessions') as client:
        message = await client.send('me', 'سلام از FNC-Splus')
        await client.send('me', 'پاسخ به پیام قبلی', reply_to_message_id=message.id)


if __name__ == '__main__':
    asyncio.run(main())
