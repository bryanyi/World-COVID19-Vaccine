# Generated by Django 3.1.6 on 2021-02-10 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='covidvaccinationdata',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='covidvaccinationdata',
            name='vaccinated',
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='daily_vaccinations',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='daily_vaccinations_per_million',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='daily_vaccinations_raw',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='date',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='iso_code',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='people_fully_vaccinated',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='people_fully_vaccinated_per_hundred',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='people_vaccinated',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='people_vaccinated_per_hundred',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='source_name',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='source_website',
            field=models.CharField(default='N/A', max_length=1000),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='total_vaccinations',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='total_vaccinations_per_hundred',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AddField(
            model_name='covidvaccinationdata',
            name='vaccines',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]
