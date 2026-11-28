import sqlite3
from datetime import datetime
from dataclasses import dataclass

@dataclass
class TemperatureModel:
    timestamp: datetime 
    temp_c: float
    
    def __post_init__(self):
        if not isinstance(self.timestamp, datetime):
            raise TypeError("timestamp must be a datetime")

        if isinstance(self.temp_c, bool) or not isinstance(self.temp_c, (int, float)):
            raise TypeError("temp_c must be a number")

        if not -273.15 <= self.temp_c <= 1000:
            raise ValueError("temp_c is outside the valid range")

        self.temp_c = float(self.temp_c)


class TemperatureRepository:
    def __init__(self, db_name='temps.db'):
        self.conn = sqlite3.connect(db_name)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute(
                '''
                    CREATE TABLE IF NOT EXISTS temperature(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        timestamp TEXT NOT NULL,
                        temp_c REAL NOT NULL
                    )
                '''
            )

    def post(self, temp: TemperatureModel) -> int:
        with self.conn:
            cursor = self.conn.execute(
                '''
                    INSERT into temperature (timestamp, temp_c) 
                    VALUES (?, ?)
                ''', 
                (temp.timestamp.isoformat(), temp.temp_c)
            )
        return cursor.lastrowid

    def get_by_id(self, record_id: int) -> TemperatureModel | None:
        with self.conn:
            cursor = self.conn.execute(
                '''
                    SELECT timestamp, temp_c 
                    FROM temperature 
                    WHERE id = ?
                ''', (record_id, )
            )
        record = cursor.fetchone()
        if record is None:
            return None    

        return TemperatureModel(
            timestamp=datetime.fromisoformat(record['timestamp']), 
            temp_c=record['temp_c']
        )

    def delete_all(self) -> int:
        with self.conn:
            cursor = self.conn.execute(
                '''
                    DELETE FROM temperature
                '''
            )
        return cursor.rowcount


    def delete_by_id(self, record_id: int) -> int:
        with self.conn:
            cursor = self.conn.execute(
                '''
                    DELETE FROM temperature
                    WHERE id = ?
                ''', 
                (record_id,)
            )
        return cursor.rowcount







