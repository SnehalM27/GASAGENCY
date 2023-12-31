# Generated by Django 4.2.4 on 2023-08-14 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[('Gas Leak Repair', 'Gas Leak Repair'), ('Meter Installation', 'Meter Installation'), ('Billing Inquiry', 'Billing Inquiry')], max_length=50)),
                ('request_details', models.TextField()),
                ('file_attachment', models.FileField(blank=True, null=True, upload_to='service_request/')),
                ('submission_timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servicerequest', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_details', models.TextField()),
                ('update_timestamp', models.DateTimeField(auto_now_add=True)),
                ('service_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Services.servicerequest')),
            ],
        ),
    ]
