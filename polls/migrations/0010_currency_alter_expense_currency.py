# Generated by Django 4.2.3 on 2024-03-12 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_alter_expense_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='USD', max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='expense',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.currency'),
        ),
    ]