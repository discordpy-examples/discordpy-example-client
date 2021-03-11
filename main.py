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
    
    # messageの中にあるメッセージの内容が、"det# ping"の時
    elif message.content.startswith("det# ping"):
        # pingというコマンドは古くからコンピュータ上で通信が異常なく行われているか
        # また，通信の遅延がどれほどあるかを計測するために使われています
        # discord bot上における通信の遅延として考えられるものは様々ありますが
        # 例えば以下のコマンド client.latency はこのbotから
        # discordとの相互通信を行うゲートウェイと呼ばれる窓口との通信遅延を求めています
        latency = client.latency

        # latencyは浮動小数点で与えられます(単位は秒です)
        # 浮動小数点をそのまま表示すると桁数が多くなってしまいます．
        # そのため以下の応答ではミリ秒単位に変換して小数点以下2桁で切り捨てを行っています．
        await message.channel.send(f"pong: {latency * 1000:.2f} ms")

# 環境変数からTOKENと一致する名前の項目を読み込んでいる。
client.run(os.environ["TOKEN"])
