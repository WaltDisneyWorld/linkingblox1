from ...structures.Bloxlink import Bloxlink # pylint: disable=no-name-in-module, import-error
import discord


get_guild_value = Bloxlink.get_module("cache", attrs=["get_guild_value"])



@Bloxlink.module
class Binds(Bloxlink.Module):
    def __init__(self):
        pass

    async def get_linked_group_ids(self, guild):
        db_data = await get_guild_value(guild, "roleBinds", "groupIDs") or {}

        role_binds = db_data.get("roleBinds") or {}
        group_ids  = db_data.get("groupIDs") or {}


        return set(group_ids.keys()).union(set(role_binds.get("groups", {}).keys()))

