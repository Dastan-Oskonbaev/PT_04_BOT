from telethon import TelegramClient, events

api_id = 21410387
api_hash = '348ab0d6c1edcc08f5e16ffef8da8a3a'

# Создаём клиент и авторизуемся
client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=[-1002427605552]))
async def handler(event):
    message = event.message.message.lower()
    if "новый заказ" in message or "заказ" in message:
        await client.send_message(event.chat_id, "Я беру заказ!")

        print(f"Ответил на сообщение: {event.message.message}")

client.start()
print("Бот запущен.")
client.run_until_disconnected()

# async def main():
#     async for dialog in client.iter_dialogs():
#         print(f"{dialog.name}: {dialog.id}")
#
# with client:
#     client.loop.run_until_complete(main())
