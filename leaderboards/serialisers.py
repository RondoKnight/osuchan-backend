from rest_framework import serializers

from profiles.serialisers import OsuUserSerialiser
from leaderboards.models import Leaderboard, Membership, Invite

class LeaderboardSerialiser(serializers.ModelSerializer):
    owner = OsuUserSerialiser()
    member_count = serializers.IntegerField(source="members.count")

    class Meta:
        model = Leaderboard
        fields = (
            "id",
            "gamemode",
            "access_type",
            "name",
            "description",
            # score criteria
            "allow_past_scores",
            "allowed_beatmap_status",
            "oldest_beatmap_date",
            "newest_beatmap_date",
            "lowest_ar",
            "highest_ar",
            "lowest_od",
            "highest_od",
            "lowest_cs",
            "highest_cs",
            "required_mods",
            "disqualified_mods",
            "lowest_accuracy",
            "highest_accuracy",
            # relations
            "owner",
            # dates
            "creation_time",
            # methods
            "member_count"
        )

class MembershipSerialiser(serializers.ModelSerializer):
    user = OsuUserSerialiser()
    score_count = serializers.IntegerField(source="scores.count")

    class Meta:
        model = Membership
        fields = (
            "id",
            "pp",
            # relations
            "leaderboard",
            "user",
            # dates
            "join_date",
            # methods
            "score_count"
        )

class InviteSerialiser(serializers.ModelSerializer):
    user = OsuUserSerialiser()
    leaderboard = LeaderboardSerialiser()

    class Meta:
        model = Invite
        fields = (
            "id",
            "message",
            # relations
            "leaderboard",
            "user",
            # dates
            "invite_date"
        )