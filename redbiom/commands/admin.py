import click

from . import cli


@cli.group()
def admin():
    """Update database, etc."""
    pass


@admin.command(name='create-context')
@click.option('--name', required=True, type=str,
              help="The name of the context, e.g., deblur@150nt")
@click.option('--description', required=True, type=str,
              help=("Default quality filtering, followed by application of "
                    "Deblur with a trim length of 150nt."))
def create_context(name, description):
    """Create context for sample data."""
    import redbiom.admin
    redbiom.admin.create_context(name, description)


@admin.command(name='load-observations')
@click.option('--table', required=True, type=click.Path(exists=True),
              help="The filepath to the table to load.")
@click.option('--context', required=True, type=str,
              help="The name of the context to load into.")
def load_observations(table, context):
    """Load observation to sample mappings."""
    import redbiom.admin
    redbiom.admin.load_observations(table, context)


@admin.command(name='load-sample-data')
@click.option('--table', required=True, type=click.Path(exists=True),
              help="The filepath to the table to load.")
@click.option('--context', required=True, type=str,
              help="The name of the context to load into.")
def load_sample_data(table, context):
    """Load nonzero entries per sample."""
    import redbiom.admin
    redbiom.admin.load_sample_data(table, context)


@admin.command(name='load-sample-metadata')
@click.option('--metadata', required=True, type=click.Path(exists=True),
              help="The filepath to the sample metadata to load.")
def load_sample_metadata(metadata):
    """Load sample metadata."""
    import redbiom.admin
    n_loaded = redbiom.admin.load_sample_metadata(metadata)
    click.echo("Loaded %d samples" % n_loaded)
