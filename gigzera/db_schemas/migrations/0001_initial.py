# Generated by Django 5.1.6 on 2025-02-16 16:20

import db_schemas.models
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('userId', models.CharField(default=db_schemas.models.generate_client_id, editable=False, max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('profilePic', models.ImageField(blank=True, default='client/profile_pics/default_profile.png', null=True, upload_to='client/profile_pics/')),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_role', models.CharField(default='client', max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('social_media', models.URLField(blank=True, null=True)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.CharField(default=db_schemas.models.generate_contact_id, max_length=10, primary_key=True, serialize=False)),
                ('user_type', models.CharField(default='Non_register', max_length=50)),
                ('user_id', models.CharField(default='NR00001', max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('reason', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('userId', models.CharField(default=db_schemas.models.generate_freelancer_id, editable=False, max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_role', models.CharField(default='freelancer', max_length=50)),
                ('profile_summary', models.TextField(blank=True, max_length=512, null=True)),
                ('designation', models.CharField(max_length=50)),
                ('social_media', models.URLField(blank=True, null=True)),
                ('country', models.CharField(max_length=50)),
                ('education', models.CharField(max_length=255)),
                ('certifications', models.CharField(blank=True, max_length=255, null=True)),
                ('experience', models.FloatField()),
                ('skills', models.JSONField(blank=True, default=dict)),
                ('projects_assigned', models.JSONField(blank=True, default=dict)),
                ('profilePic', models.ImageField(blank=True, default='freelancer/profile_pics/default_profile.png', null=True, upload_to='freelancer/profile_pics/')),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyAdmin',
            fields=[
                ('adminId', models.CharField(default=db_schemas.models.generate_admin_id, editable=False, max_length=12, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user_role', models.CharField(default='admin', max_length=50)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('currently_working', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employment_history', to='db_schemas.freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(max_length=255)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
                ('certification_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('certification_url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='db_schemas.freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='OngoingProjects',
            fields=[
                ('ongProjectId', models.CharField(default=db_schemas.models.generate_ongProject_id, editable=False, max_length=12, primary_key=True, serialize=False)),
                ('opportunityId', models.CharField(max_length=20)),
                ('bidId', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=30)),
                ('progress', models.CharField(default='0', max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_schemas.myadmin')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_schemas.client')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_schemas.freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectQuote',
            fields=[
                ('projectQuoteId', models.CharField(default=db_schemas.models.generate_projectquote_id, editable=False, max_length=12, primary_key=True, serialize=False)),
                ('opportunityId', models.CharField(max_length=20)),
                ('budget', models.CharField(max_length=20)),
                ('time_estimation', models.CharField(max_length=20)),
                ('comments', models.CharField(max_length=512)),
                ('admin_bid_status', models.CharField(default='Not confirmed yet', max_length=20)),
                ('client_bid_status', models.CharField(default='Not confirmed yet', max_length=20)),
                ('admin_margin', models.CharField(default='0', max_length=20)),
                ('currency', models.CharField(default='INR', max_length=10)),
                ('revised_budget', models.CharField(default='0', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_schemas.client')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_schemas.freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectsDisplay',
            fields=[
                ('opportunityId', models.CharField(default=db_schemas.models.generate_opportunity_id, editable=False, max_length=12, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('budget', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=50)),
                ('time_zone', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('project_type', models.CharField(max_length=50)),
                ('currency', models.CharField(default='INR', max_length=10)),
                ('description', models.TextField()),
                ('deliverables', models.TextField()),
                ('requirements', models.TextField()),
                ('challenges', models.TextField()),
                ('skills_required', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_schemas.client')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectStatusDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.CharField(default='AD001', max_length=20)),
                ('opportunity_id', models.CharField(max_length=15)),
                ('status', models.CharField(default='Not Started', max_length=20)),
                ('progress', models.CharField(default='0')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_schemas.client')),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_status_set', to='db_schemas.freelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('experience_years', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skill_set', to='db_schemas.freelancer')),
            ],
        ),
    ]
