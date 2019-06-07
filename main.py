

import discord
import asyncio
from selenium import webdriver

class Bot(discord.Client):
    ready_array = []

    async def on_ready(self):
        print("Bot is now ready to take requests")

    async def on_message(self, message):
        if message.content == "!ready":
            if str(message.author) in self.ready_array:
                await message.channel.send("You have already readied up!")
            else:
                self.ready_array.append(str(message.author))
                await message.channel.send(str(message.author) + " is now ready! This makes the current players " +  str(len(self.ready_array)))
        elif message.content == "!players":
            await message.channel.send(str(self.ready_array))

        elif  message.content == "!unready":
            if str(message.author) in self.ready_array:
                self.ready_array.remove(str(message.author))
                await message.channel.send("You have successfully unreadied!")
            else: await message.channel.send("You can't unready if you haven't readied in the first place")

        if len(ready_array) == 10:
            for i in range(1,4):
                await message.channel.send("@everyone 10 man is ready, players are " +  str(self.ready_array))
                await message.channel.send("The link is: " + self.exec())

            del self.ready_array



    def exec():
        browser = webdriver.Chrome()
        browser.get("https://popflash.site/scrim")
        python_button = browser.find_elements_by_class_name("start-scrim btn green")
        python_button.click()
        return browser.current_url

client = Bot()
client.run("YOUR OWN KEY HERE")

