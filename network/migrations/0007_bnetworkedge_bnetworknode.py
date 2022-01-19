# Generated by Django 2.2.5 on 2022-01-19 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20220117_1906'),
    ]

    operations = [
        migrations.CreateModel(
            name='BNetworkEdge',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('source', models.CharField(max_length=30)),
                ('target', models.CharField(max_length=30)),
                ('edge_type', models.CharField(max_length=30)),
                ('database', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'b_network_edge',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BNetworkNode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('indegree', models.IntegerField(blank=True, null=True)),
                ('outdegree', models.IntegerField(blank=True, null=True)),
                ('degree', models.IntegerField(blank=True, null=True)),
                ('control_type', models.IntegerField()),
                ('is_sensitive', models.IntegerField()),
                ('control_type_pnas', models.IntegerField()),
                ('is_essential_gene', models.IntegerField()),
                ('is_evolutionary_mouse', models.IntegerField()),
                ('is_evolutionary_fish', models.IntegerField()),
                ('is_evolutionary_fly', models.IntegerField()),
                ('is_evolutionary_worm', models.IntegerField()),
                ('is_evolutionary_yeast', models.IntegerField()),
                ('is_cell_signaling_signaling_protein', models.IntegerField()),
                ('is_cell_signaling_membrane_receptors', models.IntegerField()),
                ('is_cell_signaling_kinases', models.IntegerField()),
                ('is_cell_signaling_transcription_factors', models.IntegerField()),
                ('is_protein_abundance_high_copy_number', models.IntegerField()),
                ('is_protein_abundance_moderate_copy_number', models.IntegerField()),
                ('is_protein_adundance_low_copy_number', models.IntegerField()),
                ('is_protein_adundance_very_low_copy_number', models.IntegerField()),
                ('is_post_translational_modification_acetylation', models.IntegerField()),
                ('is_post_translational_modification_phosphorylation_ps_pt', models.IntegerField()),
                ('is_post_transaltional_modification_phosphorylation_py', models.IntegerField()),
                ('is_post_translational_modification_ubiquitination', models.IntegerField()),
                ('is_disease_genes_cancer_driver', models.IntegerField()),
                ('is_disease_genes_cancer1', models.IntegerField()),
                ('is_disease_genes_omim', models.IntegerField()),
                ('is_drug_target_therapeutic_targets', models.IntegerField()),
                ('is_drug_target_fda_approved', models.IntegerField()),
                ('is_drug_target_druggable', models.IntegerField()),
                ('is_regulators_of_cell_proliferation_go_genes', models.IntegerField()),
                ('is_regulatior_of_cell_proliferation_stop_genes', models.IntegerField()),
                ('is_immune_genes_core_ctl_genes', models.IntegerField()),
                ('is_immune_genes_car_genes', models.IntegerField()),
                ('is_immune_genes_checkpoint_genes', models.IntegerField()),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'b_network_node',
                'managed': False,
            },
        ),
    ]
