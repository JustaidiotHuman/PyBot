import discord
import asyncio
import token_storage

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('hello') # Send normal message
            await message.reply('Hello!', mention_author=True) # Reply to author

        if message.content.startswith('$editme'): # Sends Message and then edits it
            msg = await message.channel.send('10')
            await asyncio.sleep(10.0)
            await msg.edit(content='40')

        if message.content.startswith('$deleteme'): # Deletes Message
            msg = await message.channel.send('I will delete myself now...')
            await msg.delete()
        
        

    async def on_member_join(self, member): # Greets new Join
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Welcome {0.mention} to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)


    async def on_message_edit(self, before, after): # Sends Message that message was edited
        fmt = '**{0.author}** edited their message:\n{0.content} -> {1.content}'
        await before.channel.send(fmt.format(before, after))

    async def on_message_delete(self, message): # Sends that message was deleted
        fmt = '{0.author} has deleted the message: {0.content}'
        await message.channel.send(fmt.format(message))

intents = discord.Intents.default()
intents.members = True

tok = token_storage.TokenStorage

client = MyClient(intents=intents)
client.run(tok.getToken)