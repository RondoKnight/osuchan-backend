# Generated by Django 3.0 on 2020-03-28 01:36

from django.db import migrations

def create_score_filters(apps, schema_editor):
    Leaderboard = apps.get_model("leaderboards", "Leaderboard")
    ScoreFilter = apps.get_model("profiles", "ScoreFilter")

    for leaderboard in Leaderboard.objects.all():
        # if has any non-default score filters, create score_filter
        if (leaderboard.allowed_beatmap_status != 1
            or leaderboard.oldest_beatmap_date != None
            or leaderboard.newest_beatmap_date != None
            or leaderboard.oldest_score_date != None
            or leaderboard.newest_score_date != None
            or leaderboard.lowest_ar != None
            or leaderboard.highest_ar != None
            or leaderboard.lowest_od != None
            or leaderboard.highest_od != None
            or leaderboard.lowest_cs != None
            or leaderboard.highest_cs != None
            or leaderboard.required_mods != 0
            or leaderboard.disqualified_mods != 0
            or leaderboard.lowest_accuracy != None
            or leaderboard.highest_accuracy != None):
            leaderboard.score_filter = ScoreFilter.objects.create(
                allowed_beatmap_status=leaderboard.allowed_beatmap_status,
                oldest_beatmap_date=leaderboard.oldest_beatmap_date,
                newest_beatmap_date=leaderboard.newest_beatmap_date,
                oldest_score_date=leaderboard.oldest_score_date,
                newest_score_date=leaderboard.newest_score_date,
                lowest_ar=leaderboard.lowest_ar,
                highest_ar=leaderboard.highest_ar,
                lowest_od=leaderboard.lowest_od,
                highest_od=leaderboard.highest_od,
                lowest_cs=leaderboard.lowest_cs,
                highest_cs=leaderboard.highest_cs,
                required_mods=leaderboard.required_mods,
                disqualified_mods=leaderboard.disqualified_mods,
                lowest_accuracy=leaderboard.lowest_accuracy,
                highest_accuracy=leaderboard.highest_accuracy
            )

            leaderboard.save()

def delete_score_filters(apps, schema_editor):
    Leaderboard = apps.get_model("leaderboards", "Leaderboard")
    
    for leaderboard in Leaderboard.objects.all():
        if leaderboard.score_filter is not None:
            leaderboard.score_filter.delete()
            leaderboard.score_filter = None
            leaderboard.save()

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0010_scorefilter'),
        ('leaderboards', '0007_auto_20200328_1236'),
    ]

    operations = [
        migrations.RunPython(create_score_filters, delete_score_filters)
    ]
