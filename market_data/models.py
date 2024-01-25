from django.db import models

class scraping_log(models.Model):
    table_name=models.CharField(max_length=100,default='')
    status=models.CharField(max_length=100,default='')
    no_of_data_available=models.CharField(max_length=100,default='')
    no_of_data_scraped=models.CharField(max_length=100,default='')
    total_record_count=models.CharField(max_length=40,default='')
    reason=models.CharField(max_length=100,default='')
    comments=models.CharField(max_length=100,default='')
    trade_date=models.CharField(max_length=100,default='')
    Scraped_on=models.CharField(max_length=100,default='')
    

    class Meta:
        db_table = 'scraping_log_bse_nse'
