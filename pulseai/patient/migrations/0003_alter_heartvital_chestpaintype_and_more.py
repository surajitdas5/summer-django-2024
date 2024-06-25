# Generated by Django 5.0.6 on 2024-06-24 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_heartvital_heart_disease_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartvital',
            name='ChestPainType',
            field=models.CharField(choices=[('TA', 'Typical Angina'), ('ATA', 'Atypical Angina'), ('NAP', 'Non-Anginal Pain'), ('ASY', 'Asymptomatic')], max_length=255, verbose_name='Chest Pain Type'),
        ),
        migrations.AlterField(
            model_name='heartvital',
            name='ExerciseAngina',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=255, verbose_name='Exercise Angina'),
        ),
        migrations.AlterField(
            model_name='heartvital',
            name='FastingBS',
            field=models.CharField(choices=[('0', 'Less than or equal to 120'), ('1', 'More than to 120')], max_length=255, verbose_name='Fasting Blood Suger'),
        ),
        migrations.AlterField(
            model_name='heartvital',
            name='MaxHR',
            field=models.IntegerField(verbose_name='Maximum Heart Rate'),
        ),
        migrations.AlterField(
            model_name='heartvital',
            name='RestingBP',
            field=models.IntegerField(verbose_name='Resting Blood Presure'),
        ),
        migrations.AlterField(
            model_name='heartvital',
            name='RestingECG',
            field=models.CharField(choices=[('Normal', 'Normal'), ('ST', 'Having ST-T wave abnormality'), ('LVH', "Showing probable or definite left ventricular hypertrophy by Estes' criteria")], max_length=255, verbose_name='Resting ECG Condition'),
        ),
    ]
