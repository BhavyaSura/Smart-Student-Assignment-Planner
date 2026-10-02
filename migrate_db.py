import sqlite3
import os
DATABASE = os.environ.get(
    "DATABASE_PATH",
    os.path.join("instance", "planner.db")
)

def get_columns(cursor):
    cursor.execute("PRAGMA table_info(assignment)")
    return {row[1] for row in cursor.fetchall()}


def migrate():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    columns = get_columns(cursor)

    # Older versions used "name" instead of "title".
    if "title" not in columns and "name" in columns:
        cursor.execute(
            "ALTER TABLE assignment RENAME COLUMN name TO title"
        )
        columns = get_columns(cursor)

    # Add missing assignment detail columns.
    if "course" not in columns:
        cursor.execute(
            "ALTER TABLE assignment ADD COLUMN course VARCHAR(100)"
        )

    if "due_date" not in columns:
        cursor.execute(
            "ALTER TABLE assignment ADD COLUMN due_date VARCHAR(20)"
        )

    if "priority" not in columns:
        cursor.execute(
            "ALTER TABLE assignment ADD COLUMN priority VARCHAR(20)"
        )

    if "estimated_time" not in columns:
        cursor.execute(
            "ALTER TABLE assignment ADD COLUMN estimated_time VARCHAR(50)"
        )

    if "status" not in columns:
        cursor.execute(
            """
            ALTER TABLE assignment
            ADD COLUMN status VARCHAR(30)
            NOT NULL DEFAULT 'Not Started'
            """
        )

    connection.commit()
    connection.close()

    print("Database migration completed successfully.")


if __name__ == "__main__":
    migrate()