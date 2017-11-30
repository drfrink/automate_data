from django.db import models

# Create your models here.
class DailyTickerData(models.Model):
	symbol = models.CharField(max_length=10, db_index=True)
	open_quote = models.DecimalField(max_digits=19, decimal_places=10)
	high_quote = models.DecimalField(max_digits=19, decimal_places=10)
	low_quote = models.DecimalField(max_digits=19, decimal_places=10)
	close_quote = models.DecimalField(max_digits=19, decimal_places=10)
	volume_quote = models.DecimalField(max_digits=19, decimal_places=10)
	quote_time = models.DateField(db_index=True)

class DailyRocTickerData(models.Model):
	symbol = models.CharField(max_length=10, db_index=True)
	roc = models.DecimalField(max_digits=19, decimal_places=10)
	time_period = models.IntegerField(db_index=True)
	quote_time = models.DateField(db_index=True)