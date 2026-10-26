
"""Manage a simple pet shelter and its adoption records."""

import secrets
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE pets (
        id INTEGER PRIMARY KEY,
        name TEXT,
        species TEXT,
        age INTEGER,
        adopted INTEGER
    )
    """
)

ADOPTION_COUNT = 0


def register_pet(name, species, age, tags=None):
    """Register a pet and return its updated list of tags."""
    if tags is None:
        tags = []

    conn.execute(
        "INSERT INTO pets (name, species, age, adopted) VALUES (?, ?, ?, 0)",
        (name, species, age),
    )
    tags.append(species)
    return tags


def adopt(pet_id):
    """Mark a pet as adopted and update the adoption count."""
    global ADOPTION_COUNT
    conn.execute("UPDATE pets SET adopted = 1 WHERE id = ?", (pet_id,))
    ADOPTION_COUNT += 1


def adoption_code():
    """Generate a random adoption code."""
    return f"PET-{secrets.randbelow(9000) + 1000}"


def oldest_available():
    """Return the name of the oldest available pet, if one exists."""
    row = conn.execute(
        "SELECT name, age FROM pets WHERE adopted = 0 ORDER BY age DESC"
    ).fetchone()
    return row[0] if row else None


def clear_unadopted():
    """Remove all pets that have not been adopted."""
    conn.execute("DELETE FROM pets WHERE adopted = 0")


def shelter_status():
    """Return the shelter's current activity status."""
    if ADOPTION_COUNT > 0:
        return "active"
    return "quiet"


def main():
    """Run the pet shelter demonstration."""
    register_pet("Bruno", "dog", 7)
    register_pet("Mitzi", "cat", 3)
    register_pet("Kiwi", "parrot", 12)
    adopt(1)
    print(oldest_available(), adoption_code(), shelter_status())
    clear_unadopted()


if __name__ == "__main__":
    main()
