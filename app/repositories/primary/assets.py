from .db import db_session

from ...models.asset import Asset

def save_asset(asset: Asset):
    """Save an asset to the database."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO assets (uuid, filename, metadata, path, content_type, content_hash, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (asset.uuid, asset.filename, asset.metadata, asset.path, asset.content_type, asset.content_hash, asset.status)
        )
        connection.commit()

def get_asset_by_id(asset_id: str) -> Asset | None:
    """Retrieve an asset by its ID."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM assets WHERE uuid = ?",
            (asset_id,)
        )
        result = cursor.fetchone()
        if result:
            return Asset(**result)
        return None

def check_is_duplicate_asset(content_hash: str) -> bool:
    """Check if an asset with the same content hash already exists."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT * FROM assets WHERE content_hash = ?",
            (content_hash,)
        )
        result = cursor.fetchone()
        return result is not None

def get_all_assets(page: int = 0, page_size: int = 100) -> list[Asset]:
    """Retrieve all assets."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM assets LIMIT ? OFFSET ?", (page_size, page * page_size))
        return [Asset(**row) for row in cursor.fetchall()]

def update_asset_text(asset: Asset):
    """Update the extracted text of an existing asset in the database."""
    with db_session() as connection:
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE assets SET extracted_text = ? WHERE uuid = ?",
            (asset.extracted_text, asset.uuid)
        )
        connection.commit()