from config import ASSISTANT_NAME
from helpers.bot_utils import BOT_NAME, USERNAME


START_TEXT = f"👋🏻 **𝙃𝙖𝙡𝙤**, \n\n𝙄𝙣𝙞 𝙖𝙙𝙖𝙡𝙖𝙝 **{BOT_NAME}** \n𝙎𝙖𝙮𝙖 𝘽𝙤𝙡𝙚𝙝 𝙎𝙩𝙧𝙚𝙖𝙢 𝙇𝙞𝙫𝙚𝙨, 𝙍𝙖𝙙𝙞𝙤, 𝙑𝙞𝙙𝙚𝙤 𝙔𝙤𝙪𝙏𝙪𝙗𝙚 & 𝙁𝙖𝙞𝙡 𝘼𝙪𝙙𝙞𝙤 / 𝙑𝙞𝙙𝙚𝙤 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙋𝙖𝙙𝙖 𝙎𝙚𝙢𝙗𝙖𝙣𝙜 𝙎𝙪𝙖𝙧𝙖 𝙆𝙪𝙢𝙥𝙪𝙡𝙖𝙣 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢. 𝙈𝙖𝙧𝙞 𝙉𝙞𝙠𝙢𝙖𝙩𝙞 𝙋𝙖𝙣𝙙𝙖𝙣𝙜𝙖𝙣 𝙎𝙞𝙣𝙚𝙢𝙖𝙩𝙞𝙠 𝙋𝙚𝙢𝙖𝙞𝙣 𝙑𝙞𝙙𝙚𝙤 𝙆𝙪𝙢𝙥𝙪𝙡𝙖𝙣 𝘽𝙚𝙧𝙨𝙖𝙢𝙖 𝙍𝙖𝙠𝙖𝙣 𝘼𝙣𝙙𝙖🥰! \n\n**𝙈𝙖𝙙𝙚 𝙒𝙞𝙩𝙝 ❤️ 𝘽𝙮 @SanzuCodingMY!** 👑"
HELP_TEXT = f"""
🛠-- **Setting Up Bot**:--

\u2022 Start Voice Chat In Your Group!
\u2022 Add Me (@{USERNAME}) & My Assistant (@{ASSISTANT_NAME}) To Your Group!
\u2022 Give Admin To Me (@{USERNAME}) & My Assistant (@{ASSISTANT_NAME}) In Your Group!

⚔️-- **Available Commands**:--

\u2022 `/play` - Stream An Audio
\u2022 `/stream` - Stream An Video
\u2022 `/pause` - Pause Current Stream
\u2022 `/resume` - Resume Paused Stream
\u2022 `/endstream` - End Stream & Left VC
\u2022 `/restart` - Restart Bot (Sudo Only)
"""
ABOUT_TEXT = f"💡-- **Information**:-- \n\nThis bot is created for streaming videos in telegram group video chats using several methods from WebRTC. Powered by pytgcalls the async client API for the Telegram Group Calls and Pyrogram the telegram MTProto API Client Library and Framework in Pure Python for Users and Bots. \n\n**This bot licensed under GNU-GPL 3.0 License!**"
