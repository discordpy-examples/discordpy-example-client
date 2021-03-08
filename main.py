# discord.pyとosというモジュールをimportしている。
# importについて
# https://note.nkmk.me/python-import-usage/
import discord
import os
# 入退室ログのチャンネルのIDを保管しているJsonファイルを読み込むためimportしている
import json

# 読み込みたいファイルを指定し、open関数でconfig.jsonを開いている
with open("config.json", "r") as f:
    # 開いたファイル(変数 : f)をjson.load関数でJSONにしている
    config = json.load(f)

# 毎回、discord.Client()を書くと毎回リセットされてしまうので、clientの変数に入れている
# discord.Client()について
# https://discordpy.readthedocs.io/ja/latest/api.html?highlight=client#discord.Client
intents = discord.Intents.all()
# discord.Intentsについて
# https://discordpy.readthedocs.io/ja/latest/api.html?highlight=intents#discord.Intents
client = discord.Client(intents=intents)

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

@client.event
# discordでユーザーが参加したときに実行されるevent
# 参加したユーザーの情報が member という引数に入っている
async def on_member_join(member):
    # configの Log_Channel_ID に書かれた数字を使ってチャンネルを取得、取得したチャンネルを引数の log_channel に入れている
    # get_channelについて
    # https://discordpy.readthedocs.io/ja/latest/api.html?highlight=member#discord.Guild.get_channel
    log_channel = member.guild.get_channel(config['Log_Channel_ID'])
    # 上で取得したチャンネルの種類がtextではない時
    if log_channel.type != discord.ChannelType.text:
        print("メッセージを送信することが出来ません")
        # ボイスチャンネルやカテゴリーチャンネルにはメッセージを送信することが出来ないため

    await log_channel.send(f"{member} さんがサーバーに参加しました")  # 指定されたチャンネルにメッセージを送信する

@client.event
# discordでユーザーが退出したときに実行されるevent
# 退出したユーザーの情報が member という引数に入っている
async def on_member_remove(member):
    log_channel = member.guild.get_channel(config['Log_Channel_ID'])
    # 上で取得したチャンネルの種類がtextではない時
    if log_channel.type != discord.ChannelType.text:
        print("メッセージを送信することが出来ません")
        # ボイスチャンネルやカテゴリーチャンネルにはメッセージを送信することが出来ないため

    await log_channel.send(f"{member} さんがサーバーに参加しました")  # 指定されたチャンネルにメッセージを送信する

# 環境変数からTOKENと一致する名前の項目を読み込んでいる。
client.run(os.environ["TOKEN"])
