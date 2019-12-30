# Generated by Django 3.0.1 on 2019-12-30 17:47

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('paciente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uso_aparelho', models.CharField(blank=True, choices=[('sim', 'SIM'), ('nao', 'NAO')], max_length=3, null=True, verbose_name='ja_usou')),
                ('tempo_uso', models.DateField(verbose_name='Desde')),
                ('fabricante', models.CharField(blank=True, max_length=100, null=True, verbose_name='Fabricante')),
                ('tecnologia', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tecnologia')),
                ('dt_iprf', models.DateField(verbose_name='data_iprf')),
                ('dt_tpf', models.DateField(verbose_name='data_iprf')),
                ('mono_od', models.CharField(blank=True, max_length=10, null=True, verbose_name='Mono_OD')),
                ('mono_oe', models.CharField(blank=True, max_length=10, null=True, verbose_name='Mono_OE')),
                ('mono_od_db', models.CharField(blank=True, max_length=10, null=True, verbose_name='Mono_OD_dB')),
                ('mono_oe_db', models.CharField(blank=True, max_length=10, null=True, verbose_name='Mono_OE_dB')),
                ('dis_od', models.CharField(blank=True, max_length=10, null=True, verbose_name='Dis_OD')),
                ('dis_oe', models.CharField(blank=True, max_length=10, null=True, verbose_name='Dis_OE')),
                ('dis_od_db', models.CharField(blank=True, max_length=10, null=True, verbose_name='Dis_OD_dB')),
                ('dis_oe_db', models.CharField(blank=True, max_length=10, null=True, verbose_name='Dis_OE_dB')),
                ('lrf_od', models.CharField(blank=True, max_length=10, null=True, verbose_name='LRF_OD')),
                ('lrf_oe', models.CharField(blank=True, max_length=10, null=True, verbose_name='LRF_OE')),
                ('mono_s_aasi', models.CharField(blank=True, max_length=10, null=True, verbose_name='s/_AASI')),
                ('mono_c_aasi', models.CharField(blank=True, max_length=10, null=True, verbose_name='c/_AASI')),
                ('sss_s_aasi', models.CharField(blank=True, max_length=10, null=True, verbose_name='s/_AASI')),
                ('sss_c_aasi', models.CharField(blank=True, max_length=10, null=True, verbose_name='c/_AASI')),
                ('dis_s_aasi', models.CharField(blank=True, max_length=10, null=True, verbose_name='s/_AASI')),
                ('dis_c_aasi', models.CharField(blank=True, max_length=10, null=True, verbose_name='c/_AASI')),
                ('hhia_od_c_aasi', models.CharField(blank=True, max_length=10, null=True, verbose_name='HHIA_c/_AASI')),
                ('hhia_od_s_aasi', models.CharField(blank=True, max_length=10, null=True, verbose_name='HHIA_s/_AASI')),
                ('hhia_oe_c_aasi', models.CharField(blank=True, max_length=10, null=True, verbose_name='HHIA_c/_AASI')),
                ('hhia_oe_s_aasi', models.CharField(blank=True, max_length=10, null=True, verbose_name='HHIA_s/_AASI')),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='paciente.Paciente')),
            ],
            managers=[
                ('objetos', django.db.models.manager.Manager()),
            ],
        ),
    ]