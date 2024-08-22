"""
File: cli.py
Author: Laurence Kuhlburger
Email: laurence.kuhlburger@gmail.com
Github: https://github.com/laurencekuhl
Description: cli
"""

import click
from mercedes_universe import Creature, Werewolf, City
import datetime

@click.group()
def cli():
    """Mercedes Universe CLI."""

@cli.group()
def create():
    """Create various entities in the Mercedes Universe."""


@create.command()
@click.option("--name", prompt="Name of the creature", help="The name of the creature.")
@click.option(
    "--gender", prompt="Gender of the creature", help="The gender of the creature."
)
@click.option(
    "--birthday",
    prompt="Birthday of the creature (YYYY-MM-DD)",
    help="The birthday of the creature.",
)
def creature(name: str, gender: str, birthday: str):
    """Create a new creature."""
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
    new_creature = Creature(name, gender, birthday)
    click.echo(f"Creature created: {new_creature}")


@create.command()
@click.option("--name", prompt="Name of the werewolf", help="The name of the werewolf.")
@click.option(
    "--gender", prompt="Gender of the werewolf", help="The gender of the werewolf."
)
@click.option(
    "--birthday",
    prompt="Birthday of the werewolf (YYYY-MM-DD)",
    help="The birthday of the werewolf.",
)
@click.option(
    "--fur-color",
    prompt="Fur color of the werewolf",
    help="The fur color of the werewolf.",
)
@click.option(
    "--dominance",
    prompt="Dominance of the werewolf (True/False)",
    help="The dominance of the werewolf.",
)
@click.option("--pack", prompt="Pack of the werewolf", help="The pack of the werewolf.")
@click.option("--city", prompt="City of the werewolf", help="The city of the werewolf.")
def werewolf(  # pylint: disable=too-many-arguments
    name: str,
    gender: str,
    birthday: str,
    fur_color: str,
    dominance: str,
    pack: str,
    city: str,
):
    """Create a new werewolf."""
    birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
    dominance = dominance.lower() == "true"
    city_obj = City(city)
    new_werewolf = Werewolf(
        name, gender, birthday, fur_color, dominance, pack, city_obj
    )
    city_obj.add_inhabitant(new_werewolf)
    click.echo(f"Werewolf created: {new_werewolf}")


if __name__ == "__main__":
    cli()