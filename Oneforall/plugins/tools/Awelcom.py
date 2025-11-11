import asyncio
import random
from pyrogram import enums, filters
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton

# keep or reuse your existing random_photo list
ANIME_PHOTOS = [
    "https://files.catbox.moe/eebt15.jpg",
    "https://files.catbox.moe/ewcdeo.jpg",
    "https://files.catbox.moe/pfy94h.jpg",
    "https://files.catbox.moe/nruzva.jpg",
    "https://files.catbox.moe/0lc591.jpg",
]

@app.on_chat_member_updated(filters.group, group=-2)
async def greet_new_members(_, member: ChatMemberUpdated):
    try:
        chat_id = member.chat.id
        userbot = await get_assistant(chat_id)  # your assistant client
        disabled = await wlcm.find_one(chat_id)  # if True => welcome disabled
        if disabled:
            return

        # only act on a genuine new join (not status changes)
        if not (member.new_chat_member and not member.old_chat_member):
            return

        user = member.new_chat_member.user

        # create a safe markdown mention
        mention_md = f"[{user.first_name}](tg://user?id={user.id})"

        # decorative caption entirely in block-quotes (Markdown)
        caption = (
            "> ╔═══⋆⋆⋆⋆✦🌸✦⋆⋆⋆⋆═══╗\n"
            ">     **ᴅᴀʀᴋ ᴍᴜsɪᴄ**\n"
            "> ╚═══⋆⋆⋆⋆✦🌸✦⋆⋆⋆⋆═══╝\n"
            ">\n"
            f"> 🌈 **New Soul:** {mention_md}\n"
            f"> 🔖 **Realm ID:** `{chat_id}`\n"
            ">\n"
            "> 📖 *“Sakura drifts. Moons rise.\n"
            ">    Every traveler awakens beneath a new sky.\n"
            ">    Threads of fate shimmer… and welcome you home.”*\n"
            ">\n"
            "> 🌸 Cherry petals swirl around your arrival\n"
            "> 🐾 Fox spirits watch with quiet smiles\n"
            "> 🎴 Cards of fortune hum in hidden pockets\n"
            "> 🏮 Lanterns glow to light your first steps\n"
            ">\n"
            "> 🗡  **Courage sharpens your blade**\n"
            "> 🌙  **Serenity guards your dreams**\n"
            "> 🌟  **Wonder binds your path**\n"
            ">\n"
            "> 🍡 Step gentle, traveler\n"
            "> 🍃 The winds speak your name"
        )

        # inline button to developer profile - replace username
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="My Cute Developer", url="https://t.me/vandelone")]]
        )

        # pick an anime image
        photo_url = random.choice(ANIME_PHOTOS)

        await asyncio.sleep(3)  # small delay before sending
        await userbot.send_photo(
            chat_id=chat_id,
            photo=photo_url,
            caption=caption,
            reply_markup=keyboard,
            parse_mode=enums.ParseMode.MARKDOWN,
        )

    except Exception:
        # fail silently to avoid crashes on unexpected errors
        return
