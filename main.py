import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Bot is ready and online!')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# /start command - Bot status
@bot.tree.command(name="start", description="Check if bot is running")
async def start(interaction: discord.Interaction):
    await interaction.response.send_message("✅ Bot is running and online! 24/7 active!")

# Channel names list
CHANNEL_NAMES = [
    "💀・destroyed",
    "☢️・nuked",
    "💣・nuke-zone",
    "🔥・burnt-zone",
    "☠️・dead-zone",
    "🧨・chaos-zone",
    "💥・exploded",
    "⚠️・system-crashed",
    "☢️・radioactive",
    "💀・graveyard",
    "🔥・hell-zone",
    "💣・bombed",
    "☠️・total-destruction",
    "🧨・chaos-room",
    "💥・everything-gone",
    "🚨・critical-damage",
    "☢️・nuclear-zone",
    "💀・rip-server",
    "🔥・burning-zone",
    "💣・detonation",
    "☠️・fallen-zone",
    "🧨・blast-zone",
    "💥・impact-zone",
    "☢️・nuclear-fallout",
    "💀・dead-server",
    "🔥・inferno",
    "💣・war-zone",
    "☠️・no-survivors",
    "🧨・detonated",
    "💥・massive-damage",
    "☢️・toxic-zone",
    "💀・lost-zone",
    "🔥・ashes",
    "💣・bomb-zone",
    "☠️・death-zone",
    "🧨・blast-area",
    "💥・wrecked",
    "☢️・fallout-zone",
    "💀・destroyed-area",
    "🔥・flame-zone",
    "💣・explosion",
    "☠️・dark-zone",
    "🧨・chaos-area",
    "💥・broken-zone",
    "☢️・nuke-area",
    "💀・server-rip",
    "🔥・scorched-earth",
    "💣・detonation-zone",
    "☠️・end-zone",
    "🧨・blast-room",
    "💥・crash-zone",
    "☢️・toxic-waste",
    "💀・final-zone",
    "🔥・burned-out",
    "💣・nuclear-blast",
    "☠️・dead-end",
    "🧨・destruction-zone",
    "💥・shockwave",
    "☢️・fallout",
    "💀・ruins",
    "🔥・fire-zone",
    "💣・war-room",
    "☠️・death-room",
    "🧨・explosive-zone",
    "💥・wreckage",
    "☢️・hazard-zone",
    "💀・server-ruins",
    "🔥・ash-zone",
    "💣・bomb-site",
    "☠️・darkness",
    "🧨・blast-zone-2",
    "💥・destroyed-2",
    "☢️・nuke-2",
    "💀・dead-zone-2",
    "🔥・inferno-zone",
    "💣・mega-blast",
    "☠️・final-destruction",
    "🧨・chaos-core",
    "💥・impact-zone-2",
    "☢️・nuclear-core",
    "💀・grave-zone",
    "🔥・scorched-zone",
    "💣・mega-nuke",
    "☠️・death-core",
    "🧨・detonation-core",
    "💥・blast-core",
    "���️・toxic-core",
    "💀・void-zone",
    "🔥・fire-core",
    "💣・bomb-core",
    "☠️・doom-zone",
    "🧨・destruction-core",
    "💥・chaos-core-2",
    "☢️・fallout-core",
    "💀・end-of-server",
    "🔥・ashes-zone",
    "💣・last-blast",
    "☠️・final-ruins",
    "🧨・total-chaos"
]

# /nuke command - Delete all channels and create new ones
@bot.tree.command(name="nuke", description="Delete all channels in the server")
@discord.app_commands.checks.has_permissions(administrator=True)
async def nuke(interaction: discord.Interaction):
    await interaction.response.defer()
    
    guild = interaction.guild
    
    if not guild:
        await interaction.followup.send("❌ This command can only be used in a server!")
        return
    
    # Check if user has admin permissions
    if not interaction.user.guild_permissions.administrator:
        await interaction.followup.send("❌ You need Administrator permissions to use this command!")
        return
    
    try:
        channels = guild.channels
        total_channels = len(channels)
        deleted_count = 0
        
        await interaction.followup.send(f"🔄 Starting to delete {total_channels} channels...")
        
        # Delete all channels
        for channel in channels:
            try:
                await channel.delete()
                deleted_count += 1
                print(f"Deleted channel: {channel.name}")
                await asyncio.sleep(0.1)  # Small delay to avoid rate limiting
            except Exception as e:
                print(f"Failed to delete {channel.name}: {e}")
        
        await interaction.followup.send(f"✅ Deleted {deleted_count}/{total_channels} channels! Now creating 99 new channels...")
        
        # Create new channels
        created_count = 0
        for channel_name in CHANNEL_NAMES:
            try:
                await guild.create_text_channel(channel_name)
                created_count += 1
                print(f"Created channel: {channel_name}")
                await asyncio.sleep(0.1)  # Small delay to avoid rate limiting
            except Exception as e:
                print(f"Failed to create {channel_name}: {e}")
        
        await interaction.followup.send(f"✅ Successfully created {created_count}/99 new channels! Server NUKED! 💥")
        
    except Exception as e:
        await interaction.followup.send(f"❌ Error occurred: {str(e)}")
        print(f"Nuke command error: {e}")

# Error handler
@nuke.error
async def nuke_error(interaction: discord.Interaction, error: discord.app_commands.AppCommandError):
    if isinstance(error, discord.app_commands.MissingPermissions):
        await interaction.response.send_message("❌ You need Administrator permissions!", ephemeral=True)
    else:
        await interaction.response.send_message(f"❌ Error: {str(error)}", ephemeral=True)

# Run bot
token = os.getenv('DISCORD_TOKEN')
if token:
    bot.run(token)
else:
    print("❌ DISCORD_TOKEN not found in .env file")
