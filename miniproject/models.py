from django.db import models

# Create your models here.
class League(models.Model):
    l_name = models.CharField(primary_key = True,max_length=255, null=False)
    l_con = models.CharField(max_length=255, null=True)
    l_data = models.IntegerField(null=True)
    
    class Meta:
        db_table = 'LEAGUE'
        managed = False

class Player(models.Model):
    name = models.CharField(primary_key = True,max_length=255,null=False)

    class Meta:
        db_table = 'PLAYER'
        managed = False



class Comment(models.Model):
    c_id = models.IntegerField(primary_key = True,max_length=255,null=False)
    b_id = models.IntegerField(max_length=100)
    t_num = models.IntegerField(max_length=255,null=False)
    u_id = models.CharField(max_length=255,null=False)
    comment = models.CharField(max_length=255,null=False)

    class Meta:
        db_table = 'COMMENT'
        managed = False
    


class Board_title(models.Model):
    t_num = models.IntegerField(primary_key = True,max_length=255,null=False)
    b_id = models.IntegerField(max_length=100, null=False)
    title = models.CharField(max_length=255,null=False)
    u_id = models.CharField(max_length=255,null=False)
    date = models.DateTimeField(null=False)
    content = models.TextField(null=False)
    good = models.IntegerField(max_length=255, null=True)

    class Meta:
        db_table = 'BOARD_TITLE'
        managed = False
    
    