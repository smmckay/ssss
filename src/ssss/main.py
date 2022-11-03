import click


def print_hi(name):
    print(f"Hi, {name}")


@click.command(name="ssss")
@click.argument(
    "site_root_dir",
    type=click.Path(
        exists=True, file_okay=False, dir_okay=True, readable=True, writable=False
    ),
)
def run(site_root_dir: str):
    """Generate a static site from your YAML and Markdown."""
    print_hi(site_root_dir)
    # load templates
    # load pages
    # load posts
    # render pages
    # render posts
    # render index
    # copy assets
    # done!


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    run()
