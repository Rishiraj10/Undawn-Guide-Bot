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
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi9jVqi-M5FTMZ5u9JkwJvYLfsQn9xn7FCo92pUJqo_tzkW_dg3F6NdW-i6_AFMc48lihA5bT5s9MfQnlAh_6JQ2PBFouSnC13esolZST6TBfNwN-UXoC39-bdziBc1jaLx4uKQiLNztYTwLS6VpPxbu5S_Fvrac7tGywIslthlKGygHgGzU4n0n2dN9g/s1600/Screenshot_20210726-0744454.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiUhrCO9gSHZeRId2Iu6qpommTnlAC_C8IOu8iZpdHS8L4hM8ZFm1f7vtIFr7AqLeYOeMQED94L57fB76bBeyOwz91K1p3rX7mVgSaQO9AQNNkU-iO5L5kdEzoj3L9EtqJQmq71wF90KAwFW824YU_WJ8gojQpAJ735Fw0psGgNC7XbibYERfD5iCcNJg/s1600/Screenshot_20210726-0744562.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgXZ05RiS_b6ob9RVZOsZkjtbBjrPbh7OXtzNi80rKrA-ZJEtlz70aHcXEPUzUu-da8eYyzN3AKCoA75pAiFAgGXumDFfFdr09MrMvFnZEucDdElJkqEr8Tik8-pHQsbxq2xl5-m1iLQDMnogAdkNehO-dDiENDSmar28jzeCQsl5fLuGvYyBys1EWS1A/s1600/Screenshot_20210726-0745062.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijoA6Dnfk45KWkcB9t8FcGSID__M_wHyzHbRVhZ4X82AprYEz7xUn72Mw4yI2Ho5l97sKZqkRW76zg0WzV0uXbAdQtgvCPA1OxYuQZ_9GkqwoNnVlt8Bme4G5WVdzPgpqFCivN7duSq9CEDdx5BcjdTRIVLS-c7njxuyvgEWEbcF8VCBQG62fD7IiYew/s1600/Screenshot_20210726-0745063.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh7V_3SNeXGpZEmiGKNRaCEYpRVAupBhc53XWGB6bL7XYvT_TTgM2ca9jWYeID5z5oMAuu620wJxb4pBeBiEoLbe4XtjveFhhZd5EDYSnNxZvmCdoNisSh6pmYAN1v1B8wrVTmAJ6GO08fmajKd2MpssIQ_qXECOXgQcgt_BsiLa5pCwaDNJtBOcvth4w/s1600/Screenshot_20210726-0747252.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiy3Fr8Z8guqmRoRyaZsDWkHwvZrvfUr2mQzvuBSJz_zwMOElofnkYN9L68-F4jfUUzBPQVGxsmIeBM0_1XzqpQoJzxGjx_YrOZbrFr9LeOrBmeqNvfpUpFEsL3UipI88e7aEEbxO9gw-E6xVZ6F5WUeFsC2_6EHe4f8ECciTI_fmbj9-sWNd4tjDPLFg/s1600/Screenshot_20210726-0747312.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhiMrL0PgbulOeNB2eZCh0Q0Y0lcx76AIah_nEL7OxOk0033aXJ-bXD6dM0AYq2Ur1lpLJlliOrKqD4EZmleHz0MByBasDUQdqk2zDEInaueio8M99CdiJkJ5MksxinoN5I4ZMb6Ua85E12PcSeK7SERH0OlQK-NUjAXnvVC4bzkJh2Ug6ia3RRxJIWzQ/s1600/Screenshot_20210726-0747462.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhWP_9bxRvkPGC8_fflWGcPJu0vzXvSvKcO7k22FXYXlTTVCY-6tHZ22gkpDlACdKw0AC8d-ajEBW8yroJ1SZLsJLdD4oqu--EymnhkEORduDjYlnTdPWH2g4TocLuvuVhPY6d8uziS0H5lMXlwpC0_ATr8KWPgqFWV3Ek2Gf3eT7dJDwY0BmweW5-VOg/s1600/Screenshot_20210726-1029562.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEixeIe947BvX-ZwS4Nr_AG-_Lv6z0x2Q0qtpe6DraSsWdY1yiK_lFNsmg4xBnOmZ9rfMI-TAaOKS66cYG3lipyI7mlBG3_9MT0i4IJoFqd7wEtSLGiOmcZFE7zZGwMZ9YKDUqxjtxzGCoDJJ_va-uz1llJHtJ9jR7xqu8-eABVTpySOauyuJAZENpvp_Q/s1600/Screenshot_20210726-1030252.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqqYhHKLjvja0ksC_op21SXsSVsDSYeQUgDhw6lXXb_L-H-lHoh3x1P7iQ1WY4MvA6WtL3tWoRxNiC1yq_kEIIgb0qwWlVCyCn7rRF-B18-qrjCv_5qkELErU5WkUP_xBsSfaTjCsJdn89La7-dlFp6_C3N_wdsQNp_W3_a0d9bbb8Mv5_st-XzFlrvA/s1600/Screenshot_20210726-1030342.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhj0rbeEX_UM63V8Xcnr3lA1eiX8vzzbXi3SkmnuW4Hu0MH8ZZHeJd56bXjnJWHCDlYPRUxwb5ef8uefDY_OEEsSV-kgHcP1fNp011zd8s1Z1jq-g-0S_cxMkWmSfTf7ZPrMduopGywwb7AC-NYtCtYzXRMCGr85ktSIBvhQrM_PBF9r3AeKE4NFqVMpA/s1600/Screenshot_20210726-1030592.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjjnmg7xz30vDjBTAfUvcEZlGGCqpRPBiIs_5RUJN0cAFwkcPsFwPz-FLhXt3ikGlo2DGPiEeTdSl29s4-7uVXzhStru8BmMDsiidfzoVwAvGIyAJkxRAKPe1VbXnJ987Pkgbfs7b6MsLrPEYvudnfK8dM1FayKVtMB518qGEckks4l7HQNnvYERI4-vQ/s1600/Screenshot_20210726-1031202.png")
  await ctx.send("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgcBnqDRbnHkD-6lhFn-HUAhSmaIhFxIZJwTqc2vEgO8l_NDZJGq8M3Fw0Tl2g9g9C1ZvMgZadlIFZQQc30bFgdGlbIKzckePGU-pW-nObx74SKFhaD3xfW3utXHJMRYyS1EVz0YSdZa2jsVLA0JfwYB6iB9o4F49dc2KVw0m7SCWKEn9q4zoQAJvZDUQ/s1600/Screenshot_20210726-1030482.png")

@bot.command()
async def info_drone(ctx):
  await ctx.send("ELECTROMAGNETIC DRONE")

token = "Enter here your discord bot token"
bot.run(token)
