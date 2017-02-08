# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-02-06 08:53
from __future__ import unicode_literals

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
            name='AccessLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.AccessLevel')),
            ],
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('target_type', models.CharField(choices=[('alert_target_agent', 'Agent'), ('alert_target_cont', 'Contractor')], default='alert_target_cont', max_length=32)),
                ('body', models.TextField(max_length=5000)),
                ('is_read', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('premium_adjustment', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('bid_status_active', 'Active'), ('bid_status_expired', 'Expired'), ('bid_status_revoked', 'Revoked')], default='bid_status_active', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=256)),
                ('address_2', models.CharField(blank=True, max_length=256, null=True)),
                ('access_instructions', models.TextField(blank=True, max_length=1024, null=True)),
                ('phone_number_2', models.CharField(blank=True, max_length=32, null=True)),
                ('post_code', models.IntegerField()),
                ('preferred_schedule', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('quoted_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cost_adjustment', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('base_cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('priority_level', models.IntegerField()),
                ('completed', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('booking_status_active', 'Active'), ('booking_status_rescheduled', 'Rescheduled'), ('booking_status_cancelled', 'Cancelled')], max_length=30)),
                ('comment_private', models.TextField(blank=True, max_length=1000, null=True)),
                ('comment_public', models.TextField(blank=True, max_length=1000, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phone_number', models.CharField(max_length=32)),
                ('email_address', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('phone_number', models.CharField(max_length=32)),
                ('post_ranges_raw', models.CharField(default='[]', max_length=128)),
                ('active', models.BooleanField(default=True)),
                ('categories', models.ManyToManyField(blank=True, to='booking.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NPSRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nps_id', models.IntegerField()),
                ('is_received', models.BooleanField(default=False)),
                ('nps', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Consumer')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('perm_action_create', 'Create'), ('perm_action_read', 'Read'), ('perm_action_update', 'Update'), ('perm_action_delete', 'Delete')], max_length=30)),
                ('location', models.CharField(choices=[('perm_location_bookings', 'Bookings'), ('perm_location_bids', 'Bids'), ('perm_location_topups', 'Topups'), ('perm_location_accounts', 'Account Settings')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Preferred',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_ranges_raw', models.CharField(default='[]', max_length=128)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Category')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Contractor')),
            ],
        ),
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Suburb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('trans_type_buy', 'Buy'), ('trans_type_redeem', 'Redeem')], max_length=30)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('source_type', models.CharField(choices=[('trans_source_agent', 'Agent'), ('trans_source_contractor', 'Contractor')], max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('trans_status_pending', 'Pending'), ('trans_status_committed', 'Committed'), ('trans_status_cancelled', 'Cancelled')], default='trans_status_pending', max_length=30)),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
                ('contractor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='booking.Contractor')),
                ('source_agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Agent')),
                ('target_bid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Bid')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='permission',
            unique_together=set([('action', 'location')]),
        ),
        migrations.AddField(
            model_name='booking',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Category'),
        ),
        migrations.AddField(
            model_name='booking',
            name='consumer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Consumer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.Booking'),
        ),
        migrations.AddField(
            model_name='booking',
            name='subtypes',
            field=models.ManyToManyField(blank=True, to='booking.SubType'),
        ),
        migrations.AddField(
            model_name='booking',
            name='suburb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Suburb'),
        ),
        migrations.AddField(
            model_name='bid',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='booking.Booking'),
        ),
        migrations.AddField(
            model_name='bid',
            name='contractor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='booking.Contractor'),
        ),
        migrations.AddField(
            model_name='agent',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='booking.Permission'),
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accesslevel',
            name='default_permissions',
            field=models.ManyToManyField(blank=True, to='booking.Permission'),
        ),
    ]
