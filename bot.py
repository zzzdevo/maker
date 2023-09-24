from pyrogram import Client, idle
#'‹ ٰ💸 ⇣ سورس الفراعنة ⇣ 💸 › .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=12962251,
    api_hash="b51499523800add51e4530c6f552dbc8",
    bot_token="6668468593:AAFHmKESsD-xcKy-r_2QilryxNxLjvBUsoc",#توكن المصنع
    plugins=dict(root="MHelal")
    )

async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "IQ7amo"#يوزر المطور المصنع
    try:
        await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
    except:
        pass
    await idle()
