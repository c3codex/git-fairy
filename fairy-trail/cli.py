import click
import subprocess

@click.group()
def cli():
    """✨ Git Fairy CLI — call her with commands!"""
    pass

@cli.command()
@click.argument("message", default="✨ Git Fairy auto-commit")
def summon(message):
    """Summon the fairy to add, commit, and push with a message."""
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    cli()
