import discord
from datetime import datetime
from discord.ext import commands

class UserInfo(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=["whois", "ui"])
	async def userinfo(self, ctx, member:discord.Member=None):
		roles = []
		if not member:
			member = ctx.author
		for role in member.roles:
			roles.append(str(role.mention))

		roles.reverse()

		embed = discord.Embed(title=f"{member}'s User Info")
		embed.add_field(name="Username", value=member.name)
		embed.add_field(name="Discriminator", value=member.discriminator)
		embed.add_field(name="ID", value=member.id)
		embed.add_field(name="Created At", value=datetime.strftime(member.created_at, "%A, %B %-d, %Y"))
		embed.add_field(name="Joined At", value=datetime.strftime(member.joined_at, "%A, %B %-d, %Y"))
		if len(str(" | ".join([x.mention for x in member.roles]))) > 1024:
			embed.add_field(name=f"Roles [{len(member.roles)}]", value="Too many to display.")
		else:
			embed.add_field(name=f"Roles [{len(member.roles)}]", value=" | ".join(roles))
		embed.add_field(name="Role Color", value=member.color)
		embed.set_thumbnail(url=member.avatar_url)
		await ctx.send(embed=embed)
		
def setup(client):
	client.add_cog(UserInfo(client))

