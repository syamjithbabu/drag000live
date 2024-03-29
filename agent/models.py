from django.db import models
from website.models import Dealer,User
from adminapp.models import Agent,PlayTime
from dealer.models import DealerGame
from django.db.models import Sum
from django.utils import timezone
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class DealerPackage(models.Model):
    dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE,null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    package_name = models.CharField(max_length=100)
    single_rate = models.FloatField()
    single_dc = models.FloatField()
    double_rate = models.FloatField()
    double_dc = models.FloatField()
    box_rate = models.FloatField()
    box_dc = models.FloatField()
    super_rate = models.FloatField()
    super_dc = models.FloatField()
    first_prize = models.FloatField()
    first_dc = models.FloatField()
    second_prize = models.FloatField()
    second_dc = models.FloatField()
    third_prize = models.FloatField()
    third_dc = models.FloatField()
    fourth_prize = models.FloatField()
    fourth_dc = models.FloatField()
    fifth_prize = models.FloatField()
    fifth_dc = models.FloatField()
    guarantee_prize = models.FloatField()
    guarantee_dc = models.FloatField()
    box_first_prize = models.FloatField()
    box_first_prize_dc = models.FloatField()
    box_series_prize = models.FloatField()
    box_series_dc = models.FloatField()
    single1_prize = models.FloatField()
    single1_dc = models.FloatField()
    double2_prize = models.FloatField()
    double2_dc = models.FloatField()


    def __str__(self):
        return str(self.package_name)
    
class AgentGameTest(models.Model):
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,null=True)
    customer = models.CharField(max_length=100,null=True)
    time = models.ForeignKey(PlayTime,on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True)
    LSK = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    count = models.IntegerField()
    d_amount = models.FloatField()
    c_amount = models.FloatField()

    def __str__(self):
        return str(self.agent)

    
class AgentGame(models.Model):
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,null=True)
    customer = models.CharField(max_length=100,null=True)
    time = models.ForeignKey(PlayTime,on_delete=models.CASCADE,null=True)
    date = models.DateField(auto_now_add=True)
    LSK = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    count = models.IntegerField()
    d_amount = models.FloatField()
    c_amount = models.FloatField()
    combined = models.BooleanField()

    def __str__(self):
        return str(self.agent)
    
class Bill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.CharField(max_length=100)
    time_id = models.ForeignKey(PlayTime,on_delete=models.CASCADE,null=True)
    date = models.DateField()
    agent_games = models.ManyToManyField(AgentGame)
    dealer_games = models.ManyToManyField(DealerGame)
    total_c_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_d_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_count = models.DecimalField(max_digits=10, decimal_places=0)
    win_amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    total_c_amount_admin = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_d_amount_admin = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    win_amount_admin = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Bill for {self.user} on {self.date}'
    
    def delete(self, using=None, keep_parents=False):
        # First, delete the associated games
        for game in self.agent_games.all():
            game.delete()
        for game in self.dealer_games.all():
            game.delete()
        
        # Then, delete the Bill object itself
        super(Bill, self).delete(using, keep_parents)
    
    def update_totals(self):
        # Calculate and update total_count, total_c_amount, and total_d_amount
        total_count = self.agent_games.aggregate(total_count=Sum('count'))['total_count'] or 0
        total_c_amount = self.agent_games.aggregate(total_c_amount=Sum('c_amount'))['total_c_amount'] or 0
        total_d_amount = self.agent_games.aggregate(total_d_amount=Sum('d_amount'))['total_d_amount'] or 0

        self.total_count = total_count
        self.total_c_amount = total_c_amount
        self.total_d_amount = total_d_amount
        self.save()
    
    def update_totals_dealer(self):
        # Calculate and update total_count, total_c_amount, and total_d_amount
        total_count = self.dealer_games.aggregate(total_count=Sum('count'))['total_count'] or 0
        total_c_amount = self.dealer_games.aggregate(total_c_amount=Sum('c_amount'))['total_c_amount'] or 0
        total_d_amount = self.dealer_games.aggregate(total_d_amount=Sum('d_amount'))['total_d_amount'] or 0

        self.total_count = total_count
        self.total_c_amount = total_c_amount
        self.total_d_amount = total_d_amount
        self.save()
    
class DealerCollectionReport(models.Model):
    date = models.DateField()
    dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE,null=True)
    from_or_to = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.dealer)
    
class DealerLimit(models.Model):
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,null=True)
    dealer = models.ForeignKey(Dealer,on_delete=models.CASCADE,null=True)
    daily_limit = models.FloatField()
    checked_times = models.ManyToManyField(PlayTime)

    def __str__(self):
        return str(self.dealer)

class CustomerAgent(models.Model):
    customer = models.CharField(max_length=100)
    agent = models.ForeignKey(Agent,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.agent)