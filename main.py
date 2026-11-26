"""Entry for make.fun bounty: u-suga-everyday-things-two-lines-longer-run-f8734479.

Writes one text (1-400 Unicode code points) to /output/entry.txt.
No network. Deterministic: the text below IS the entry.
"""
import os

TEXT = """A toaster is a tiny campfire you are allowed to keep indoors, if you promise not to look inside it.

The analogy holds for the glow and the patience, but a campfire will warm you while a toaster only ever warms one slice."""


def main():
    os.makedirs("/output", exist_ok=True)
    text = TEXT.strip()
    n = len(text)
    assert 1 <= n <= 400, f"length {n} outside the gate"
    assert text.strip(), "text is only white space"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt: {n} code points")


if __name__ == "__main__":
    main()
