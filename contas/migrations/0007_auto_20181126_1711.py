# Generated by Django 2.1.3 on 2018-11-26 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0006_auto_20181126_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transacao',
            old_name='categoria',
            new_name='pagamento',
        ),
    ]
