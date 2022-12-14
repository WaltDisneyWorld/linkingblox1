from os import environ as env
from time import time
from re import search
from discord.utils import find

RELEASE = env.get("RELEASE", "LOCAL")
IS_DOCKER = bool(env.get("RELEASE"))

TOPGG_API = "https://top.gg/api"
DBL_API = "https://discordbotlist.com/api/v1"

SHARDS_PER_CLUSTER = int(env.get("SHARDS_PER_CLUSTER", "1"))

CLUSTER_ID = env.get("CLUSTER_ID") or search(r".+\-(\d+)", env.get("HOSTNAME", "bloxlink-0"))
CLUSTER_ID = (CLUSTER_ID and ((isinstance(CLUSTER_ID, str) and CLUSTER_ID.isdigit() and int(CLUSTER_ID)) or int(CLUSTER_ID.group(1)))) or 0

SHARD_COUNT = int(env.get("SHARD_COUNT", "1"))

SHARD_RANGE = []

_to_add = 0
for _ in range(SHARDS_PER_CLUSTER):
  shard = (CLUSTER_ID * SHARDS_PER_CLUSTER) + _to_add

  if shard + 1 > SHARD_COUNT:
      break

  SHARD_RANGE.append(shard)
  _to_add += 1

if RELEASE == "LOCAL":
    SELF_HOST = True # changes bot behavior, such as using the Bloxlink API for requests
else:
    SELF_HOST = False

SERVER_INVITE = "https://discord.gg/jJKWpsr"

STARTED = time()

RED_COLOR       = 0xdb2323
INVISIBLE_COLOR = 0x36393E
ORANGE_COLOR    = 0xCE8037
GOLD_COLOR      = 0xFDC333
CYAN_COLOR      = 0x4DD3CC
PURPLE_COLOR    = 0xa830c5
GREEN_COLOR     = 0x0ec37e
BROWN_COLOR     = 0xa2734a
BLURPLE_COLOR   = 0x4a58a2
YELLOW_COLOR    = 0xf1c40f
PINK_COLOR      = 0xf47fff

DEV_COLOR               = 0x4DD3CC
STAFF_COLOR             = 0x3ca770
COMMUNITY_MANAGER_COLOR = 0xc4306f
VIP_MEMBER_COLOR        = 0x3271c2
PARTNERS_COLOR          = 0xda43d1

PARTNERED_SERVER        = 0x4f91a0

if RELEASE == "PRO":
    EMBED_COLOR = YELLOW_COLOR
elif RELEASE == "MAIN":
    EMBED_COLOR = RED_COLOR
elif RELEASE == "CANARY":
    EMBED_COLOR = ORANGE_COLOR
elif RELEASE == "LOCAL":
    EMBED_COLOR = PURPLE_COLOR

VERIFY_URL_GUILD = "https://blox.link/dashboard/verifications/verify?page=username&guild={guild}"
VERIFY_URL = "https://blox.link/verify"

VERIFYALL_MAX_SCAN = 5

HTTP_RETRY_LIMIT = 5

MODULE_DIR = [
	"src/resources/modules",
	"src/resources/events",
	"src/commands",
    "src/apps"
]

NICKNAME_TEMPLATES = (
    "{roblox-name} \u2192 changes to their Roblox Username (unique)\n"
    "{display-name} \u2192 changes to their Roblox Display Name (not unique)\n"
    "{smart-name} \u2192 changes to: display name (@username) if the user has a display name; otherwise, changes to their username\n"
    "{roblox-id} \u2192 changes to their Roblox user ID\n"
    "{roblox-age} \u2192 changes to their Roblox user age in days\n"
    "{roblox-join-date} \u2192 changes to their Roblox join date\n"
    "{group-rank} \u2192 changes to their group rank\n"
    "{group-rank-ID} \u2192 changes to their group rank in group with ID\n"
    "{discord-name} \u2192 changes to their Discord display name; works on unverified users\n"
    "{discord-nick} \u2192 changes to their Discord nickname; works on unverified users\n"
    "{server-name} \u2192 changes to the server name; works on unverified users\n"
    "{clan-tag} \u2192 replaceable text which the user can set\n"
    "\n"
    "{disable-nicknaming} \u2192 overrides all other options and returns a blank nickname. Note that this ONLY APPLIES TO NICKNAMES."
)

SERVER_VERIFIED_TEMPLATES = (
    "{roblox-name} \u2192 changes to their Roblox Username (unique)\n"
    "{display-name} \u2192 changes to their Roblox Display Name (not unique)\n"
    "{smart-name} \u2192 changes to: display name (@display name) if the user has a display name; otherwise, changes to their username\n"
    "{roblox-id} \u2192 changes to their Roblox user ID\n"
    "{roblox-age} \u2192 changes to their Roblox user age in days\n"
    "{roblox-join-date} \u2192 changes to their Roblox join date\n"
    "{group-rank} \u2192 changes to their group rank\n"
    "{group-rank-ID} \u2192 changes to their group rank in group with ID\n"
    "{discord-name} \u2192 changes to their Discord display name\n"
    "{discord-mention} \u2192 changes to a string that mentions (pings) the user\n"
    "{discord-id} \u2192 changes to their Discord ID\n"
    "{discord-nick} \u2192 changes to their Discord nickname; works on unverified users\n"
    "{server-name} \u2192 changes to the server name; works on unverified users\n"
    "{prefix} \u2192 changes to the server prefix"
)

UNVERIFIED_TEMPLATES = (
    "{discord-name} \u2192 changes to their Discord display name\n"
    "{discord-nick} \u2192 changes to their Discord nickname\n"
    "{server-name} \u2192 changes to the server name\n"
    "{discord-mention} \u2192 changes to a string that mentions (pings) the user\n"
    "{discord-id} \u2192 changes to their Discord ID"
)

ESCAPED_NICKNAME_TEMPLATES = NICKNAME_TEMPLATES.replace("{", "{{").replace("}", "}}")

OPTIONS = {                # fn,  type, max length or choices, premium only, desc
    "verifiedRoleName":      (None, "string", 100,    False, "The Verified role is given to people who are linked on Bloxlink. You can change the name of the role here."),
    "verifiedRoleEnabled":   (None, "boolean", None, False, "The Verified role is given to people who are linked on Bloxlink. Enable/disable it here."),
    "unverifiedRoleEnabled": (None, "boolean", None, False, "The Unverified role is given to people who aren't linked on Bloxlink. Enable/disable it here."),
    "Linked Groups":         (None,  None, None,     False, "Bind groups to your server so group members get specific roles."),
    "allowOldRoles":         (None, "boolean", None, False, "Bloxlink will NOT remove roles if this is enabled."),
    "autoRoles":             (None, "boolean", None, False, "Bloxlink will give all matching/corresponding roles to people who join the server. Set eligible roles with `/bind`. Note that this being enabled will override 'autoVerification'."),
    "autoVerification":      (None, "boolean", None, False, "Bloxlink will give the Verified role to people who join the server and are linked to Bloxlink.\nNote that 'autoRoles' being enabled overrides this setting."),
    "dynamicRoles":          (None, "boolean", None, False, "Bloxlink will make missing group roles from your Linked Groups as people need them."),
    "welcomeMessage":        (None, "string", 1500,  False, "The welcome message is used on `/getrole` responses. Note that you can use these templates: ```{templates}```"),
    "joinDM":                (lambda g, gd: bool(gd.get("verifiedDM", True)) or bool(gd.get("unverifiedDM")), None, None, False, "Customize the join DM messages of people who join the server."),
    "joinChannel":           (lambda g, gd: bool(gd.get("joinChannel", True)), None, None, False, "Customize the join messages of people who join the server."),
    "leaveChannel":          (lambda g, gd: bool(gd.get("leaveChannel", True)), None, None, False, "Customize the leave messages of people who leave the server."),
    "persistRoles":          (None, "boolean", None, True,  "Update members' roles/nickname as they type."),
    "allowReVerify":         (None, "boolean", None, True,  "If this is enabled: members can change their Roblox account as many times as they want in your server; otherwise, only allow 1 account change."),
    "nicknameTemplate":      (None,  "string", 100,  False, "Set the universal nickname template. Note that `/bind` nicknames will override this."),
    "unverifiedRoleName":    (None,  "string", 100,  False, "Set the 'Unverified' role name -- the role that Unverified users get."),
    "shorterNicknames":      (None,  "boolean", None,False, "Brackets in group rank names will be captured instead of the full rank name, resulting in a shorter nickname."),
    "ageLimit":              (None,  "number", None, True,  "Set the minimum Roblox age in days a user must be to enter your server. People who are less than this value will be kicked."),
    "banRelatedAccounts":    (None, "boolean", None, True,  "If this is enabled: when members are banned, their known alts are also banned from the server."),
    "unbanRelatedAccounts":  (None, "boolean", None, True,  "If this is enabled: when members are unbanned, their known alts are also unbanned from the server."),
    "disallowAlts":          (None, "boolean", None, True,  "If this is enabled: when someone joins the server and already has a linked account in the server, kick the old alt out."),
    "disallowBanEvaders":    (None, "choice", ("ban", "kick"), True,  "If this is enabled: when members join, and they have a banned account in the server, their new account will also be actioned."),
    "promptDelete":          (None, "boolean", None, False, "Toggle the deleting of prompt messages after it finishes."),
    "deleteCommands":        (None, "number", 180, False, "Set X higher than 0 to delete every command after X seconds."),
    "magicRoles":            (lambda g, gd: gd.get("magicRoles"), None, None, True, "Customize the names of the Bloxlink Magic Roles."),
}

PROMPT = {
	"PROMPT_TIMEOUT": 300,
	"PROMPT_ERROR_COUNT": 5
}

DEFAULTS = {
    "Linked Groups": "view using `@Bloxlink viewbinds`",
    "verifiedRoleName": "Verified",
    "verifiedRoleEnabled": True,
    "unverifiedRoleEnabled": True,
    "allowOldRoles": False,
    "autoRoles": True,
    "autoVerification": True,
    "dynamicRoles": True,
    "persistRoles": False,
    "allowReVerify": True,
    "welcomeMessage": ":wave: Welcome to **{server-name}**, {roblox-name}! Visit <" + VERIFY_URL + "> to change your account.",
    "nicknameTemplate": "{smart-name}",
    "unverifiedRoleName": "Unverified",
    "shorterNicknames": True,
    "ageLimit": 0,
    "promptDelete": True,
    "deleteCommands": 0,
    "inactiveRole": None,
    "banRelatedAccounts": False,
    "unbanRelatedAccounts": False,
    "disallowAlts": False,
    "disallowBanEvaders": False,
    "verifyChannelTextModal": "Welcome to **{server-name}!** Click the button below to Verify with Bloxlink and gain access to the rest of the server.",
    "groupLockKickMessageVerified": "You've been kicked from **{server-name}** because your Roblox account **{roblox-name}** is not in the group **{group-name}.**\n\n"
                                    "**How to fix this:** Join {group-url}, then rejoin the server.\n\n**Wrong Roblox account?** Go to <" + VERIFY_URL + "> to change your account.",
    "groupLockKickMessageRolesetsVerified": "You've been kicked from **{server-name}** because your Roblox account **{roblox-name}** does not have the required Roleset in **{group-name}.**\n\n"
                                    "**How to fix this:** Join {group-url}, then rejoin the server.\n\n**Wrong Roblox account?** Go to <" + VERIFY_URL + "> to change your account.",
    "groupLockDMMessageVerified": "You are required to join the group **{group-name}** to access **{server-name}.**\n\n"
                                  "**How to fix this:** Join {group-url}, then run `/getrole`.\n\n**Wrong Roblox account?** Go to <" + VERIFY_URL + "> to change your account.",
    "groupLockDMMessageRolesetsVerified": "You are required to have the required Roleset in **{group-name}** to access **{server-name}.**\n\n"
                                  "**How to fix this:** Join {group-url}, then run `/getrole`.\n\n**Wrong Roblox account?** Go to <" + VERIFY_URL + "> to change your account.",
    "kickMessageNotVerified": "You were kicked from **{server-name}** for not being linked to Bloxlink.\n\n"
                            f"**How to fix this:** Go to <" + VERIFY_URL + "> to verify with Bloxlink.\n\n"
                            "**Stuck? Watch this video:** <https://www.youtube.com/watch?v=mSbD91Zug5k&t=0s>\n\n"
                            f"Join {SERVER_INVITE} for additional help.",
    "DMMessageNotVerified": "You are required to verify with Bloxlink in order to access **{server-name}**.\n\n"
                            f"**How to fix this:** Go to <" + VERIFY_URL + "> to verify with Bloxlink.\n\n"
                            "**Stuck? Watch this video:** <https://www.youtube.com/watch?v=mSbD91Zug5k&t=0s>\n\n"
                            f"Join {SERVER_INVITE} for additional help."
}

ARROW = "\u2192"

MAGIC_ROLES = {
    "Bloxlink Admin": "These users can use ANY Bloxlink command.",
    "Bloxlink Bypass": "Bloxlink will NOT update these users.",
    "Bloxlink Updater": "These users can use /update on others."
}

OWNER = 84117866944663552

HELP_DESCRIPTION = "**Welcome to Bloxlink!**\n\n" \
                   "**Support Server:** https://blox.link/support\n" \
                   "**Website:** https://blox.link/\n" \
                   "**Invite:** https://blox.link/invite\n\n" \
                   "Please use `/setup` to set-up your server.\n" \
                   "**Bloxlink tutorials:** https://blox.link/tutorials/\n" \
                  # "Want sweet perks for your server? Check out our **[Patreon!](https://www.patreon.com/join/bloxlink?)**"


TRANSFER_COOLDOWN = 5

TABLE_STRUCTURE = {
    "bloxlink": [
        "users",
        "guilds",
        "gameVerification",
        "robloxAccounts",
        "commands",
        "miscellaneous",
        "restrictedUsers",
        "addonData",
        "applications",
        "ads",
        "codes",
        "robloxProfiles"
    ],
    "canary": [
        "guilds",
        "addonData",
        "robloxProfiles"
    ],
    "patreon": [
        "refreshTokens",
        "patrons"
    ]
}

LIMITS = {
    "BINDS": {
        "FREE": 60,
        "PREMIUM": 200
    },
    "BACKUPS": 4,
    "RESTRICTIONS": {
        "FREE": 25,
        "PREMIUM": 250
    }
}

PLAYING_STATUS = "/help /invite"

AVATARS = {
    "PRIDE": "https://cdn.discordapp.com/attachments/480614508633522176/730969660010266644/rainbow_resized.png"
}

STREAMERS = (84117866944663552, 194962036784889858, 84388454456127488, 173885028818747395)

if RELEASE == "LOCAL":
    CACHE_CLEAR = 2
else:
    CACHE_CLEAR = 10

TIP_CHANCES = {
    "PROMPT_ERROR": 30,
    "GETROLE_DONATE": 10
}

IGNORED_SERVERS = [
    903359999688990770
]

RBX_STAFF = 0x1
RBX_STAR = 0x2
BLOXLINK_STAFF = 0x4
# 0x8
