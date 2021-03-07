# discord.pyとosというモジュールをimportしている。
# importについて
# https://note.nkmk.me/python-import-usage/
import discord
import os
import asyncio

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

    # メッセージの内容が、"det# count"から始まる時
    elif message.content.startswith("det# count"):
        # メッセージ内容をスペースで区切り、その三つ目以降をリストとしてcountに代入する
        count = message.content.split(" ")[2:]

        # リストcountの一つ目が数字か判定する
        # str.isdigutについて
        # https://note.nkmk.me/python-str-num-determine/
        if not count[0].isdigit() is True:
            await message.channel.send("`det# count 10`のように入力してください。")
            # event関数on_messageを終了する
            return

        msg = await message.channel.send(f"残り{count[0]}秒\n{'■'*int(count[0])}")
        # countの1つ目をforで回す
        # for文について
        # https://note.nkmk.me/python-for-usage/
        for i in range(int(count[0])):
            num = int(count[0]) - i
            # 上で送信したメッセージを編集する
            # Message.editについて
            # https://discordpy.readthedocs.io/ja/latest/api.html#discord.Message.edit
            await msg.edit(content=f"残り{num}秒\n{'■'*int(num)}")
            # asyncio.sleep()を使うことで、プログラム上の処理を全て止めなくて済む
            # https://docs.python.org/ja/3/library/asyncio-task.html#sleeping
            await asyncio.sleep(1)
        await asyncio.sleep(0.5)
        # 送信したメッセージを削除する
        # https://discordpy.readthedocs.io/ja/latest/api.html#discord.Message.delete
        await msg.delete()
        await message.channel.send(f"{message.author.mention}-> 終了しました。")

# 環境変数からTOKENと一致する名前の項目を読み込んでいる。
client.run(os.environ["TOKEN"])
