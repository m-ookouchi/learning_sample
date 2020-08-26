from django.db import models
import json

class app_storage_tables(models.Model):
    table_id = models.AutoField('id', primary_key=True)
    table_name = models.CharField('name')
    table_columns = models.BinaryField('columns')

    columns = json.decoder.JSONDecoder(self.table_columns)

class app_storage_data(models.Model):
    data_id = models.AutoField('id', primary_key=True)
    table_id = models.IntegerField('table_id')
    data = models.BinaryField('data')

    items = json.decoder.JSONDecoder(data)

