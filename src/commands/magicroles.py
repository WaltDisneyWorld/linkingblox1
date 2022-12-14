from resources.structures.Bloxlink import Bloxlink # pylint: disable=import-error, no-name-in-module, no-name-in-module
from resources.constants import ARROW, BROWN_COLOR, MAGIC_ROLES # pylint: disable=import-error, no-name-in-module, no-name-in-module
from resources.exceptions import Error # pylint: disable=import-error, no-name-in-module, no-name-in-module
import discord


post_event = Bloxlink.get_module("utils", attrs=["post_event"])
set_guild_value, get_guild_value = Bloxlink.get_module("cache", attrs=["set_guild_value", "get_guild_value"])
has_premium = Bloxlink.get_module("premium", attrs=["has_premium"])


@Bloxlink.command
class MagicRolesCommand(Bloxlink.Module):
    """add/view/remove magic roles"""

    def __init__(self):
        self.permissions = Bloxlink.Permissions().build("BLOXLINK_MANAGER")
        self.category = "Premium"
        self.hidden = True
        self.aliases = ["magicrole", "magicroles", "magic-roles"]
        self.free_to_use = True

    async def __main__(self, CommandArgs):
        await CommandArgs.response.send("You can modify your magic roles from our dashboard: https://blox.link/dashboard")
