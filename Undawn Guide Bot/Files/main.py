import os
import discord
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())


@bot.event
async def on_ready():
  await bot.change_presence(status=discord.Status.online)
  os.system('clear')
  print(f'Logged in as {bot.user} (ID: {bot.user.id})')


keep_alive()


@bot.command()
async def info_bike(ctx):
  await ctx.send(
    "Steering stability:- upgradable\n\n Acceleration performance:- upgradable\n\n Anti-hit ability: upgradable\n\n Climbing ability: upgradable\n\n Fuel consumption: upgradable\n\n Braking performance: upgradable\n\n Model name-\n Mad cow heavy-duty motorcycle.\n\n Weight-244KG.\n\nEngine model name-\n PW V-type twin-cylinder engine.\n\n Maximum torque -\n 87 NM @ 3750 RPM.\n\n Max speed-\n 60KM/H\n\n Engine displacement -\n 1202CC.\n\n Fuelel capacity-\n 7.9Litres ")


@bot.command()
async def info_special_effects_preview(ctx):
  await ctx.send(
    " [Absolute Suppression]- A certain skill intensity damage is caused every second when the severely injured target is attached with the wound effect, lasts 3 seconds, and cools down for 12 seconds.\n\n [Focus Boost] -After causing a head crit, the basic damage is increased for 3 seconds, and the effect is cooled for 5 seconds.\n\n [The more you fight]-the more you fight, the base damage increases for 2 seconds, the cooldown is 1 second, and the maximum increase is 3 layers.\n\n [Armor Blasting] -causes additional armor damage, and cannot restore armor by itself within a certain period of time.\n\n [Armor-piercing warhead]- hits with armor  At the same time, it will cause a percentage of damage to life.\n\n [Strategic Master] -The next time you use tactical skills, the skill intensity will be increased, and the cooldown will be 30 seconds.\n\n [Maneuvering damage reduction]- Increase the damage reduction after overturning the waves, lasts 6 seconds, cool down for 18 seconds.\n\n [Defense Specialization] -After using tactical skills, the armor value is increased, lasts 10 seconds, cools down for 20 seconds.\n\n [Weakening Corrosion]-  The target adds a damage effect of skill strength per second for 3 seconds.  Cool down for 15 seconds.\n\n [Unyielding Will] -Increase a certain upper limit of life.\n\n [Indifference domain]- Increase a certain amount of armor.\n\n [M can be a mecha]- Increase a certain upper limit of armor.")
   
@bot.command()
async def info_gunpic(ctx):
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg038zalcevW_5rSeYMDeKNIDXa4CjPCZJuqQOklP6S-fRBSJhAhwzuwf5T-R7Q08B4N5tzc6b0IVuRaZ0h-6kbbWKUknV0F933PlF5zt9-3T_Vwb6x-UaTEZu_vG25ILEDnUCmPp7L7u8gk2oqXen1GSUPTYqm0H4ax3Rhj8rs_truwPBfqumHgXAKPw/s1600/Screenshot_20210723-2036522.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjFM1OLgxxKfEM0d3cPfZOMGv3jZW8clxF6M7vD1A8_V7oNdBhTOp5du6vgnfixzGy83PF4BiKxC6YryoIAAyol7kJzDet_x3Y1AAr-fQnph0DQ0QPX5WWuLvFZIpDQRrX7A0gV6nM1ZQt9rMLX34UrSzRGqWJwXAoqUlDMU_MGtRjQuSDzgpg5F4B1Yw/s1600/Screenshot_20210726-0744452.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOsxJsVKu7KdbOwdNW2VBD0uClYW36o7xe4T5QdNCN4di3fyteeLta0p1ZXFkUMfDf7cgMT_3eKIg2HQz7cN-1B_bkbCegkpfd_jY3ZmwylwQ5egKeqos_7KQuR2KvMK30KVDvOsapp_A0Rm7CiW18tps2Ud2i0LUYRLrkcmDQyQ-6R2rZNDPu57uxAw/s1600/Screenshot_20210726-0744453.png")

@bot.command()
async def info_drone(ctx):
  await ctx.send("ELECTROMAGNETIC DRONE")

token = "Enter here your discord bot token"
bot.run(token)
