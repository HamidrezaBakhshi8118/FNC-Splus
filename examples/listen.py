import asyncio
from fnc_splus import Client

client = Client('personal', data_dir='sessions')


@client.on('message')
async def on_message(client, delivery):
    print(delivery.chat_id, delivery.message_id, delivery.text)


async def main():
    async with client:
        await client.run()


if __name__ == '__main__':
    asyncio.run(main())
