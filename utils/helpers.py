from utils.constants import SOURCE_TITLE, SOURCE_URL


def check_source(source: str = None) -> int:
    if source is None:
        raise Exception('You must declare a url or title as a source.')
    if 'https' in source:
        return SOURCE_URL

    return SOURCE_TITLE


def print_if(condition: bool = True, *args):
    if condition:
        print(*args)
