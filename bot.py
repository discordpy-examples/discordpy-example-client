# discord.pyとosというモジュールをimportしている。
# importについて
# https://note.nkmk.me/python-import-usage/
import discord
import os

# 毎回、discord.Client()を書くと毎回リセットされてしまうので、clientの変数に入れている
# discord.Client()について
# https://discordpy.readthedocs.io/ja/latest/api.html?highlight=client#discord.Client
client = discord.Client()

# 必要なやつ
@client.event
# Botが起動したときに、実行されるevent
# ただし、on_readyは何度も呼び出される可能性がある
async def on_ready():
    print("起動完了")
    # インストールされているdiscord.pyのバージョンを表示する
    # f"{}"(フォーマット済み文字列リテラル)について
    # https://note.nkmk.me/python-f-strings/
    print(f"{discord.__version__}")
    # print("{}".format(discord.__version__))

@client.event
# discordで何かしらのメッセージが送信されたときに実行されるevent
# 何かしらのメッセージが送信されたときの情報をmessageという引数(ひきすう)に入れている
async def on_message(message):
    # messageの中にあるメッセージの内容が、"det# hello"の時
    if message.content == "det# hello":
        # sendについて
        # https://discordpy.readthedocs.io/ja/latest/api.html?highlight=send#discord.abc.Messageable.send
        await message.channel.send("Hello World")  # 何らかしらのメッセージが送られたチャンネルに"Hello World"を送信する

    elif message.content.startswith("det# count"):
        count = message.content[10:]
        try:
            count = int(count)
        else:
            await message.channel.send("det# conut <秒数[int]>")

        edit = await message.channel.send(f"10\n■■■■■■■■■■")
        for i in range(count):
            num = count - i
            await edit.edit(content=f"{num}\n{'■'*num}")
            await asyncio.sleep(0.9)
        await edit.edit(content="終了")
# 環境変数からTOKENと一致する名前の項目を読み込んでいる。
client.run(os.environ["TOKEN"])
