from project.guild_members.warrior import Warrior
from project.guild_members.mage import Mage
from project.guild_halls.combat_hall import CombatHall
from project.guild_halls.magic_tower import MagicTower


class GuildMaster:
    def __init__(self):
        self.members = []
        self.guild_halls = []

    def add_member(self, member_type: str, member_tag: str, member_gold: int):
        member_classes = {
            "Warrior": Warrior,
            "Mage": Mage
        }

        if member_type not in member_classes:
            raise ValueError("Invalid member type!")

        if any(member.tag == member_tag for member in self.members):
            raise ValueError(f"{member_tag} has already been added!")

        for guild_hall in self.guild_halls:
            if any(member.tag == member_tag for member in guild_hall.members):
                raise ValueError(f"{member_tag} has already been added!")

        member = member_classes[member_type](member_tag, member_gold)
        self.members.append(member)

        return f"{member_tag} is successfully added as {member_type}."

    def add_guild_hall(self, guild_hall_type: str, guild_hall_alias: str):
        guild_hall_classes = {
            "CombatHall": CombatHall,
            "MagicTower": MagicTower
        }

        if guild_hall_type not in guild_hall_classes:
            raise ValueError("Invalid guild hall type!")

        if any(
            guild_hall.alias == guild_hall_alias
            for guild_hall in self.guild_halls
        ):
            raise ValueError(f"{guild_hall_alias} has already been added!")

        guild_hall = guild_hall_classes[guild_hall_type](guild_hall_alias)
        self.guild_halls.append(guild_hall)

        return (
            f"{guild_hall_alias} is successfully added as a "
            f"{guild_hall_type}."
        )

    def assign_member(self, guild_hall_alias: str, member_type: str):
        guild_hall = next(
            (
                guild_hall
                for guild_hall in self.guild_halls
                if guild_hall.alias == guild_hall_alias
            ),
            None
        )

        if guild_hall is None:
            raise ValueError(
                f"Guild hall {guild_hall_alias} does not exist!"
            )

        member = next(
            (
                member
                for member in self.members
                if member.role == member_type
            ),
            None
        )

        if member is None:
            raise ValueError("No available members of the type!")

        if len(guild_hall.members) >= guild_hall.max_member_count:
            return "Maximum member count reached. Assignment is impossible."

        self.members.remove(member)
        guild_hall.members.append(member)

        return f"{member.tag} was assigned to {guild_hall_alias}."

    def practice_members(self, guild_hall, sessions_number: int):
        for _ in range(sessions_number):
            for member in guild_hall.members:
                member.practice()

        total_skill_level = sum(
            member.skill_level
            for member in guild_hall.members
        )

        return (
            f"{guild_hall.alias} members have "
            f"{total_skill_level} total skill level after "
            f"{sessions_number} practice session/s."
        )

    def unassign_member(self, guild_hall, member_tag: str):
        member = next(
            (
                member
                for member in guild_hall.members
                if member.tag == member_tag
            ),
            None
        )

        if member is None or member.skill_level == 10:
            return "The unassignment process was canceled."

        guild_hall.members.remove(member)
        self.members.append(member)

        return f"Unassigned member {member_tag}."

    def guild_update(self, min_skill_level_value: int):
        for guild_hall in self.guild_halls:
            guild_hall.increase_gold(min_skill_level_value)

        sorted_guild_halls = sorted(
            self.guild_halls,
            key=lambda guild_hall: (
                -len(guild_hall.members),
                guild_hall.alias
            )
        )

        result = [
            "<<<Guild Updated Status>>>",
            f"Unassigned members count: {len(self.members)}",
            f"Guild halls count: {len(self.guild_halls)}"
        ]

        for guild_hall in sorted_guild_halls:
            result.append(f">>>{guild_hall.status()}")

        return "\n".join(result)