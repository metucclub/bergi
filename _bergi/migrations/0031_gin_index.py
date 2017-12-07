from django.db import migrations

# So we can efficiently search in articles.
# Without an index, postgres makes a linear search which takes forever.
# db_index=True isn't an option, content fields are too big for B-tree indexing.
# See https://czep.net/17/full-text-search.html
def mkgin(apps, schema_editor):
        if schema_editor.connection.vendor != "postgresql":
                return
        migrations.RunSQL("CREATE INDEX tonic_idx ON _bergi_article USING GIN(to_tsvector('turkish', COALESCE(content, '')));")

class Migration(migrations.Migration):
        dependencies = [("_bergi", "0001_initial")]
        operations = [migrations.RunPython(mkgin)]
