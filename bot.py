import os
import discord
from discord import app_commands

# ---- BOT SETUP ----
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# ---- TRE LLO LINKS ----
STYLE_TRELLO = {
    "combat": "https://trello.com/c/to9HwmQW/61-basic-combat",
    "street fighthing": "https://trello.com/c/MImGjGHg/176-street-fighting",
    "boxing": "https://trello.com/c/81B6bcDU/62-boxing",
    "taekwondo": "https://trello.com/c/WsHGZnuR/63-taekwondo",
    "sumo": "https://trello.com/c/Km751TDO/64-sumo",
    "muay thai": "https://trello.com/c/ACP9QHrn/175-muay-thai",
    "karate": "https://trello.com/c/5bBspSLk/199-karate",
    "wrestling": "https://trello.com/c/4bKllJA9/230-wrestling",
    "aikido": "https://trello.com/c/aYa8ZucW/245-aikido",
    "kick boxing": "https://trello.com/c/VOvp5bZp/301-kick-boxing",
    "kung fu": "https://trello.com/c/DDHJBDCW/304-kung-fu",
    "taekkyon": "https://trello.com/c/QZydKmdR/315-taekkyon",
    "capoeira": "https://trello.com/c/jWmyP8PZ/387-capoeira",
    "kures tradition": "https://trello.com/c/H1c4lHJq/172-kures-traditions",
    "raishin": "https://trello.com/c/ilbDoTCs/249-raishin",
    "niko style": "https://trello.com/c/Bka5Tk9E/341-niko-style",
    "total violence": "https://trello.com/c/8FO6whSl/342-total-violence",
    "primeval": "https://trello.com/c/aZ0IFh97/275-primeval"
}

CARD_TRELLO = {
    "general": "https://trello.com/c/Lzr7vQJj/95-general",
    "player traits": "https://trello.com/c/rblJ8lfe/183-player-traits",
    "street fighting": "https://trello.com/c/VR6DjBPp/180-street-fighting",
    "boxing": "https://trello.com/c/2T1i0x8l/96-boxing",
    "taekwondo": "https://trello.com/c/L4R05so7/97-taekwondo",
    "sumo": "https://trello.com/c/cFbZCn5k/98-sumo",
    "muay thai": "https://trello.com/c/L1nCCam0/179-muay-thai",
    "karate": "https://trello.com/c/eeeDRYpD/203-karate",
    "wrestling": "https://trello.com/c/TxKafm2T/233-wrestling",
    "aikido": "https://trello.com/c/BSk7gQvx/248-aikido",
    "kick boxing": "https://trello.com/c/auJXNEo3/302-kick-boxing",
    "kung fu": "https://trello.com/c/DdZIrZyK/314-kungfu",
    "taekkyon": "https://trello.com/c/6kN7nxji/327-taekkyon",
    "capoeira": "https://trello.com/c/NptqYQjC/401-capoeira",
    "kures tradition": "https://trello.com/c/ytSGfczj/174-kure-traditions",
    "raishin": "https://trello.com/c/6pg8f7D7/265-raishin",
    "niko style": "https://trello.com/c/NekQ5g7G/373-niko-style",
    "total violence": "https://trello.com/c/OnUyBHnx/374-total-violence",
    "primeval": "https://trello.com/c/AesB2dFd/281-primeval",
    "trance state": "https://trello.com/c/5lvsVmcH/241-trance-state",
    "primitive": "https://trello.com/c/rwcdwBZ5/278-primitive",
    "guihun": "https://trello.com/c/8fdqFKP8/402-guihun",
    "ultra instinct": "https://trello.com/c/BWPi4N4S/240-ultra-instinct",
    "removal": "https://trello.com/c/j49gRMpW/239-removal",
    "lightning god": "https://trello.com/c/53NRh30U/266-lightning-god",
    "congential ultra instinct": "https://trello.com/c/IKPTnDW5/375-congenital-ultra-instinct",
    "demon back": "https://trello.com/c/3roqnlks/376-demon-back",
    "advance": "https://trello.com/c/4oxohfFA/377-half-advance",
    "infinity tech": "https://trello.com/c/gJRtk8DQ/238-infinity-tech",
    "animal instinct": "https://trello.com/c/SrAIzTkY/237-animal-instinct"
}

MODE_TRELLO = {
    "trance state": "https://trello.com/c/rM8WutsY/236-trance-state",
    "primitive": "https://trello.com/c/Y7urRIgZ/274-primitive",
    "advance": "https://trello.com/c/veP2kxsW/344-half-full-advance",
    "guihun": "https://trello.com/c/yTE5uFoP/394-guihun-wu",
    "ultra instinct": "https://trello.com/c/64maoxAh/198-ultra-instinct-park",
    "lightning god": "https://trello.com/c/d5kudolc/258-lightning-god-mikazuchi",
    "removal": "https://trello.com/c/2CMXUZ56/184-removal-kure",
    "congential ultra instinct": "https://trello.com/c/Hd6QLmFH/343-congenital-ultra-instinct-yamazaki",
    "demon back": "https://trello.com/c/QtWEp2rt/345-demon-back-hanma",
    "infinity tech": "https://trello.com/c/W1bbjlKD/138-infinity-tech-seong",
    "animal instinct": "https://trello.com/c/dkP9vwhc/208-animal-instinct-jang"
}

PSYCHES_TRELLO = {
    "common": "https://trello.com/c/c4U4NEGs/8-common-60",
    "rare": "https://trello.com/c/NoWXVXfI/7-rare-35",
    "legendary": "https://trello.com/c/cOnMiAJo/6-legendary-45",
    "mythic": "https://trello.com/c/8gJCYUxW/5-mythics-5"
}

CLAN_TRELLO = {
    "evolved": "https://trello.com/c/2zT4ekfN/287-evolved",
    "common": "https://trello.com/c/JwP3dsdG/4-common-60",
    "uncommon": "https://trello.com/c/uL3qHbog/57-uncommon-20",
    "rare": "https://trello.com/c/wy2AJw25/3-rare-14",
    "legendary": "https://trello.com/c/ouFXL562/2-legendary-5",
    "mythic": "https://trello.com/c/mf8Lq4Jn/1-mythic-1"
}

# ---- AUTOCOMPLETE ----
async def style_autocomplete(interaction, current):
    return [app_commands.Choice(name=k.title(), value=k)
            for k in STYLE_TRELLO if current.lower() in k.lower()][:25]

async def card_autocomplete(interaction, current):
    return [app_commands.Choice(name=k.title(), value=k)
            for k in CARD_TRELLO if current.lower() in k.lower()][:25]

async def mode_autocomplete(interaction, current):
    return [app_commands.Choice(name=k.title(), value=k)
            for k in MODE_TRELLO if current.lower() in k.lower()][:25]

# ---- READY ----
@client.event
async def on_ready():
    await tree.sync()
    print(f"Bot logged in as {client.user}")

# ---- COMMANDS ----
@tree.command(name="style")
@app_commands.autocomplete(name=style_autocomplete)
async def style(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(STYLE_TRELLO[name])

@tree.command(name="card")
@app_commands.autocomplete(name=card_autocomplete)
async def card(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(CARD_TRELLO[name])

@tree.command(name="mode")
@app_commands.autocomplete(name=mode_autocomplete)
async def mode(interaction: discord.Interaction, name: str):
    await interaction.response.send_message(MODE_TRELLO[name])

@tree.command(name="psyches")
@app_commands.choices(
    rarity=[
        app_commands.Choice(name="Common", value="common"),
        app_commands.Choice(name="Rare", value="rare"),
        app_commands.Choice(name="Legendary", value="legendary"),
        app_commands.Choice(name="Mythic", value="mythic"),
    ]
)
async def psyches(
    interaction: discord.Interaction,
    rarity: app_commands.Choice[str]
):
    await interaction.response.send_message(PSYCHES_TRELLO[rarity.value])

@tree.command(name="clan")
@app_commands.choices(
    rarity=[
        app_commands.Choice(name="Evolved", value="evolved"),
        app_commands.Choice(name="Common", value="common"),
        app_commands.Choice(name="Uncommon", value="uncommon"),
        app_commands.Choice(name="Rare", value="rare"),
        app_commands.Choice(name="Legendary", value="legendary"),
        app_commands.Choice(name="Mythic", value="mythic"),
    ]
)
async def clan(
    interaction: discord.Interaction,
    rarity: app_commands.Choice[str]
):
    await interaction.response.send_message(CLAN_TRELLO[rarity.value])
@tree.command(name="items", description="Show all obtainable items")
async def items(interaction: discord.Interaction):
    await interaction.response.send_message("🧾 Items list coming soon.")

@tree.command(name="subskills", description="Show all sub skills")
async def subskills(interaction: discord.Interaction):
    await interaction.response.send_message("⚔️ Subskills list coming soon.")

@tree.command(name="clanskills", description="Show all clan skills")
async def clanskills(interaction: discord.Interaction):
    await interaction.response.send_message("🏯 Clan skills list coming soon.")

@tree.command(name="boss", description="Show all bosses")
async def boss(interaction: discord.Interaction):
    await interaction.response.send_message("👹 Boss list coming soon.")

@tree.command(name="mobs", description="Show all mobs")
async def mobs(interaction: discord.Interaction):
    await interaction.response.send_message("🧟 Mob list coming soon.")

@tree.command(name="npc", description="Show all NPCs")
async def npc(interaction: discord.Interaction):
    await interaction.response.send_message("🧍 NPC list coming soon.")

@tree.command(name="shopnpc", description="Show all shop NPCs")
async def shopnpc(interaction: discord.Interaction):
    await interaction.response.send_message("🛒 Shop NPC list coming soon.")

@tree.command(name="info", description="Game information")
async def info(interaction: discord.Interaction):
    await interaction.response.send_message("ℹ️ Ryujin information panel.")

@tree.command(name="questnpc", description="Show all quest NPCs")
async def questnpc(interaction: discord.Interaction):
    await interaction.response.send_message("📜 Quest NPC list coming soon.")

# ---- RUN ----
client.run(os.getenv("DISCORD_TOKEN"))
