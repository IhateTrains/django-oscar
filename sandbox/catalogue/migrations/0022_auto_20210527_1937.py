# Generated by Django 3.1.11 on 2021-05-27 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0021_auto_20201005_0844'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImageStorage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bytes', models.TextField()),
                ('filename', models.CharField(max_length=255)),
                ('mimetype', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='productimage',
            name='original',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='catalogue.ProductImageStorage/bytes/filename/mimetype'),
        ),
    ]