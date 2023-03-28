# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'django_migrations'


class ExtendedPythagorian(models.Model):
    team_name = models.OneToOneField('LeagueTable', models.DO_NOTHING, db_column='team_name', primary_key=True)
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    matches = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    loses = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    goals_against = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    expected_wins = models.IntegerField(blank=True, null=True)
    expected_draws = models.IntegerField(blank=True, null=True)
    expected_loses = models.IntegerField(blank=True, null=True)
    expected_points = models.IntegerField(blank=True, null=True)
    delta_points_extended = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'extended_pythagorian'
        unique_together = (('team_name', 'year_start', 'year_end'),)


class Fixtures(models.Model):
    match_id = models.IntegerField(primary_key=True)
    home_team = models.ForeignKey('Team', models.DO_NOTHING,related_name='home_team', db_column='home_team', blank=True, null=True)
    away_team = models.ForeignKey('Team', models.DO_NOTHING,related_name='away_team', db_column='away_team', blank=True, null=True)
    home_goals = models.IntegerField(blank=True, null=True)
    away_goals = models.IntegerField(blank=True, null=True)
    datetime = models.DateField(blank=True, null=True)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'fixtures'


class League(models.Model):
    league_name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'league'


class LeagueTable(models.Model):
    league_name = models.ForeignKey(League, models.DO_NOTHING, db_column='league_name', blank=True, null=True)
    team_name = models.OneToOneField('Team', models.DO_NOTHING, db_column='team_name', primary_key=True)
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    matches = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    loses = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    goals_against = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    xgoals = models.FloatField(blank=True, null=True)
    npx_goals = models.FloatField(blank=True, null=True)
    xassists = models.FloatField(blank=True, null=True)
    npx_goals_against = models.FloatField(blank=True, null=True)
    npx_goals_difference = models.FloatField(blank=True, null=True)
    ppda = models.FloatField(blank=True, null=True)
    oppda = models.FloatField(blank=True, null=True)
    dc = models.IntegerField(blank=True, null=True)
    odc = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'league_table'
        unique_together = (('team_name', 'year_start', 'year_end'),)


class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=50)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'player'


class PlayerDefensiveStats(models.Model):
    team_name = models.OneToOneField('Rosters', models.DO_NOTHING, db_column='team_name', primary_key=True)
    id = models.IntegerField()
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    tackles_per_game = models.FloatField(blank=True, null=True)
    interceptions_per_game = models.FloatField(blank=True, null=True)
    fouls_per_game = models.FloatField(blank=True, null=True)
    offsides_won_per_game = models.FloatField(blank=True, null=True)
    clearances_per_game = models.FloatField(blank=True, null=True)
    dribbled_past_per_game = models.FloatField(blank=True, null=True)
    outfielder_blocks_per_game = models.FloatField(blank=True, null=True)
    own_goal = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'player_defensive_stats'
        unique_together = (('team_name', 'id', 'year_start', 'year_end'),)


class PlayerOffensiveStats(models.Model):
    team_name = models.OneToOneField('Rosters', models.DO_NOTHING, db_column='team_name', primary_key=True)
    id = models.IntegerField()
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    dribbles_per_game = models.FloatField(blank=True, null=True)
    fouled_per_game = models.FloatField(blank=True, null=True)
    offsides_per_game = models.FloatField(blank=True, null=True)
    dispossessed_per_game = models.FloatField(blank=True, null=True)
    bad_control_per_game = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'player_offensive_stats'
        unique_together = (('team_name', 'id', 'year_start', 'year_end'),)


class PlayerPassingStats(models.Model):
    team_name = models.OneToOneField('Rosters', models.DO_NOTHING, db_column='team_name', primary_key=True)
    id = models.IntegerField()
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    key_passes_per_game = models.FloatField(blank=True, null=True)
    passes_per_game = models.FloatField(blank=True, null=True)
    crosses_per_game = models.FloatField(blank=True, null=True)
    long_ball_per_game = models.FloatField(blank=True, null=True)
    through_balls_per_game = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'player_passing_stats'
        unique_together = (('team_name', 'id', 'year_start', 'year_end'),)


class PlayerSummaryStats(models.Model):
    team_name = models.OneToOneField('Rosters', models.DO_NOTHING, db_column='team_name', primary_key=True)
    id = models.IntegerField()
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    games = models.CharField(max_length=50, blank=True, null=True)
    start_games = models.IntegerField(blank=True, null=True)
    sub_games = models.IntegerField(blank=True, null=True)
    mins = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    yellow_cards = models.IntegerField(blank=True, null=True)
    red_cards = models.IntegerField(blank=True, null=True)
    shot_per_game = models.FloatField(blank=True, null=True)
    pass_success_percentage = models.FloatField(blank=True, null=True)
    aerials_won = models.FloatField(blank=True, null=True)
    man_of_the_match = models.IntegerField(blank=True, null=True)
    who_scored_rating = models.FloatField(blank=True, null=True)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'player_summary_stats'
        unique_together = (('team_name', 'id', 'year_start', 'year_end'),)


class Rosters(models.Model):
    team_name = models.OneToOneField('Team', models.DO_NOTHING, db_column='team_name', primary_key=True)
    id_player = models.ForeignKey(Player, models.DO_NOTHING, db_column='id_player')
    year_start = models.IntegerField()
    year_end = models.IntegerField()

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'rosters'
        unique_together = (('team_name', 'id_player', 'year_start', 'year_end'),)


class SimplePythagorian(models.Model):
    team_name = models.OneToOneField(LeagueTable, models.DO_NOTHING, db_column='team_name', primary_key=True)
    year_start = models.IntegerField()
    year_end = models.IntegerField()
    matches = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    draws = models.IntegerField(blank=True, null=True)
    loses = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    goals_against = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    expected_points = models.IntegerField(blank=True, null=True)
    delta_points_extended = models.IntegerField(blank=True, null=True)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'simple_pythagorian'
        unique_together = (('team_name', 'year_start', 'year_end'),)


class Team(models.Model):
    team_name = models.CharField(primary_key=True, max_length=50)

    class Meta:
        app_label = 'playground'
        managed = False
        db_table = 'team'
