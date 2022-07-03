# Generated by Django 4.0.5 on 2022-07-03 19:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('finances', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetSharedWith',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='budget',
            name='shared_with',
            field=models.ManyToManyField(blank=True, related_name='shared_budgets', through='finances.BudgetSharedWith', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='budgetsharedwith',
            name='budget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.budget'),
        ),
        migrations.AddField(
            model_name='budgetsharedwith',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
