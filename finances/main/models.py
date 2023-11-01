import pandas as pd
import psycopg2
from django.db import models


class Currency(models.Model):
    id = models.AutoField(primary_key=True)
    currency_name = models.CharField(max_length=255)
    alphabetic_code = models.CharField(max_length=3)
    numeric_code = models.PositiveIntegerField()

    def __str__(self):
        return self.currency_name

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    @staticmethod
    def import_currency_data():
        import os, sys
        sys.path.append('/home/mk/Desktop/Py88_diploma_Petrochuk_Maksim__finances/finances')
        os.environ['DJANGO_SETTINGS_MODULE'] = 'finances.settings'
        import django
        django.setup()

        conn = psycopg2.connect(database="finances", user="finances_admin", password="peklo5gd!", host="localhost")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT COUNT(*) FROM main_currency"
        )

        fetch = cursor.fetchone()

        if fetch != (0,):
            conn.commit()
            conn.close()
            return 0
        else:
            data = pd.read_excel('/home/mk/Downloads/list-one.xls')

            unique_names = []
            unique_a_codes = []
            unique_n_codes = []

            for index, row in data.iterrows():
                currency__name = row['Currency']
                alphabetic__code = row['Alphabetic Code']
                numeric__code = row['Numeric Code']

                if str(currency__name) in unique_names:
                    pass
                else:
                    unique_names.append(currency__name)
                    unique_a_codes.append(alphabetic__code)
                    unique_n_codes.append(numeric__code)

            print(len(unique_names), len(unique_a_codes), len(unique_n_codes))

            for i in range(0, len(unique_names)):
                name = unique_names[i]
                a_code = unique_a_codes[i]
                n_code = unique_n_codes[i]

                cursor.execute(
                    "INSERT INTO main_currency (currency_name, alphabetic_code, numeric_code) VALUES (%s, %s, %s)",
                    (name, a_code, n_code)
                )

        conn.commit()
        conn.close()

    @staticmethod
    def currency_choices():
        currency_choices = []

        currency_list = Currency.objects.all()

        import os, sys
        sys.path.append('/home/mk/Desktop/Py88_diploma_Petrochuk_Maksim__finances/finances')
        os.environ['DJANGO_SETTINGS_MODULE'] = 'finances.settings'
        import django
        django.setup()

        conn = psycopg2.connect(database="finances", user="finances_admin", password="peklo5gd!", host="localhost")
        cursor = conn.cursor()

        for i in range(0, len(currency_list)):
            currency = currency_list[i]

            cursor.execute(
                "SELECT * FROM main_currency WHERE currency_name = VALUES %s", currency
            )

            res = cursor.fetchone()
            print(res)

        return currency_choices


Currency.import_currency_data()
# Currency.currency_choices()
