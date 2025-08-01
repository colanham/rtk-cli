# cli.py

import typer # type: ignore

def main(kanji: str):
    print(f"Kanji passed is: {kanji} ")

if __name__ == "__main__":
    typer.run(main)