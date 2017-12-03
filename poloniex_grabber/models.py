from django.db import models

# Create your models here.

class PoloniexCoinPairDataRaw(models.Model):
	coin_pair = models.CharField(max_length=10, db_index=True)
	last = models.DecimalField(max_digits=19, decimal_places=10)
	lowest_ask = models.DecimalField(max_digits=19, decimal_places=10)
	highest_bid = models.DecimalField(max_digits=19, decimal_places=10)
	percent_change = models.DecimalField(max_digits=19, decimal_places=10)
	base_volume = models.DecimalField(max_digits=19, decimal_places=10)
	quote_volume = models.DecimalField(max_digits=19, decimal_places=10)
	is_frozen = models.IntegerField()
	high_24hr = models.DecimalField(max_digits=19, decimal_places=10)
	low_24hr = models.DecimalField(max_digits=19, decimal_places=10)
	created_at = models.DateTimeField(db_index=True)

