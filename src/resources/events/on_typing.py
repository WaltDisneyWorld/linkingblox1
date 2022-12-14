from ..structures.Bloxlink import Bloxlink # pylint: disable=import-error, no-name-in-module
from discord import Member, Object
from discord.utils import find
from ..constants import DEFAULTS, RELEASE # pylint: disable=import-error, no-name-in-module
from ..exceptions import CancelCommand # pylint: disable=import-error, no-name-in-module

cache_get, cache_set, get_guild_value = Bloxlink.get_module("cache", attrs=["get", "set", "get_guild_value"])
guild_obligations = Bloxlink.get_module("roblox", attrs=["guild_obligations"])
has_premium = Bloxlink.get_module("premium", attrs=["has_premium"])
has_magic_role = Bloxlink.get_module("extras", attrs=["has_magic_role"])


@Bloxlink.module
class ChannelTypingEvent(Bloxlink.Module):
    def __init__(self):
        pass

    async def __setup__(self):

        @Bloxlink.event
        async def on_typing(channel, user, when):
            if isinstance(user, Member):
                guild = user.guild

                return

                donator_profile = await has_premium(guild=guild)

                if "premium" in donator_profile.features:
                    if await cache_get(f"channel_typing:{guild.id}:{user.id}", primitives=True):
                        return

                    options = await get_guild_value(guild, ["persistRoles", DEFAULTS.get("persistRoles")])
                    persist_roles = options["persistRoles"]

                    if persist_roles:
                        await cache_set(f"channel_typing:{guild.id}:{user.id}", True, expire=7200)

                        if not await has_magic_role(user, guild, "Bloxlink Bypass"):
                            try:
                                await guild_obligations(user, guild, join=True, dm=False, event=False)
                            except CancelCommand:
                                pass
