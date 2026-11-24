"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (183 characters) pitching GoatShred: goats rented
to law firms to eat confidential documents. Deterministic: no clock,
no randomness, no network, no input.
"""

import os

PITCH = (
    "GoatShred rents hungry goats to law firms to eat confidential "
    "documents for $300 a visit, because goats shred paper for free, "
    "can't leak files, and fertilize the lawn while they work."
)


def main():
    # The grader mounts /output: clear its contents, never the folder itself.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
