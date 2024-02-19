""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 6.1.0
"""
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context


# Here we name the cog and create a new class for the cog.
class UserRole(commands.Cog, name="userrole"):
    def __init__(self, bot) -> None:
        self.bot = bot

    # Here you can just add your own commands, you'll always need to provide "self" as first parameter.

    @commands.hybrid_command(
        name="major",
        description="Choose your major role (ECE, IPS, CSE)",
    )
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @app_commands.describe(
        major="The Major role to be set (ece, ips or cse)",
    )
    async def major(self, context: Context, *, major: str) -> None:
        """
        Choose your dice major (ECE, IPS or CSE)

        :param context: The application command context.
        :param major: The major chosen by the user.
        """
        major = str(major).lower()
        member = context.guild.get_member(context.author.id) or await context.guild.fetch_member(
            context.author.id
        )

        ece = context.guild.get_role(1166779671879364750) # ECE⚡
        ips = context.guild.get_role(1166780221383508029) # IPS 💽
        cse = context.guild.get_role(1166780097030791238) # CSE 🖳

        if(ece in member.roles or ips in member.roles or cse in member.roles):
            embed = discord.Embed(
                description="You already have a major role. Please ask an admin to change your major.",
                color=0xE02B2B,
                )
            await context.send(embed=embed)
        else:
            try:
                match major:
                    case 'ece':
                        await member.add_roles(ece)
                        embed = discord.Embed(
                        description="Welcome to ECE⚡",
                        color=0xBEBEFE,
                        )
                        await context.send(embed=embed)
                    case 'ips':
                        await member.add_roles(ips)
                        embed = discord.Embed(
                        description="Welcome to IPS 💽",
                        color=0xBEBEFE,
                        )
                        await context.send(embed=embed)
                    case 'cse':
                        await member.add_roles(cse)
                        embed = discord.Embed(
                        description="Welcome to CSE 🖳",
                        color=0xBEBEFE,
                        )
                        await context.send(embed=embed)
                    case _:
                        embed = discord.Embed(
                        description="Major not found. Possible majors are ece, ips or cse.",
                        color=0xE02B2B,
                        )
                        await context.send(embed=embed)
            except:
                embed = discord.Embed(
                    title="Error!",
                    description="An error occurred while trying to assign the role! Please contact a mama cub.",
                    color=0xE02B2B,
                )
                await context.send(embed=embed)

# And then we finally add the cog to the bot so that it can load, unload, reload and use it's content.
async def setup(bot) -> None:
    await bot.add_cog(UserRole(bot))
