# Generated by Django 3.1 on 2022-03-08 09:13

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confidence', models.PositiveSmallIntegerField(choices=[(1, 'Very low'), (2, 'Low'), (3, 'Moderate'), (4, 'High'), (5, 'Very high')])),
                ('penetration', models.PositiveSmallIntegerField(choices=[(1, 'Almost never or never'), (2, 'A few times'), (3, 'Sometimes'), (4, 'Most times'), (5, 'Almost always or always')])),
                ('intercourse', models.PositiveSmallIntegerField(choices=[(1, 'Almost never or never'), (2, 'A few times'), (3, 'Sometimes'), (4, 'Most times'), (5, 'Almost always or always')])),
                ('completion', models.PositiveSmallIntegerField(choices=[(1, 'Extremely difficult'), (2, 'Very difficult'), (3, 'Difficult'), (4, 'Slightly difficult'), (5, 'Not difficult')])),
                ('satisfaction', models.PositiveSmallIntegerField(choices=[(1, 'Almost never or never'), (2, 'A few times'), (3, 'Sometimes'), (4, 'Most times'), (5, 'Almost always or always')])),
                ('score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(25), django.core.validators.MinValueValidator(5)])),
                ('average', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
