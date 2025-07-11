from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0002_userselectedtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Soft_Skills',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='emotive_copy',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
