import click
import cligj
import json

from poly_point_simplify import poly_point_simplify as process_features


@click.command()
@cligj.features_in_arg
@cligj.sequence_opt
@cligj.use_rs_opt
@click.option("--min-area", '-m', type=float, required=True)
def main(features, sequence, use_rs, min_area):
    if sequence:
        for feature in process_features(features, min_area):
            if use_rs:
                click.echo(b'\x1e', nl=False)
            click.echo(json.dumps(feature))
    else:
        click.echo(json.dumps(
            {'type': 'FeatureCollection',
             'features': list(process_features(features, min_area))}))
