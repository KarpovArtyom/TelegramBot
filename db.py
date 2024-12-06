import sqlite3

class BotDB:

    def __init__(self, db_file):
        """Инициализация соединения с БД"""
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def get_brand_car(self, Brand):
        """Получаем модель автомобиля из БД"""
        result = self.cursor.execute("SELECT 'Brand', 'Model' FROM 'cars' WHERE 'Brand' = ?",(Brand))
        return result

    def get_brand_Model(self, Brand):
        """Получаем модель автомобиля из БД"""
        result = self.cursor.execute("SELECT * FROM 'Models' WHERE 'Brand' = ?",(Brand))
        return result

    def close(self):
        """Закрытие соединения с БД"""
        self.conn.close()