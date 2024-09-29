from faker import Faker
fake = Faker()

def generate_unique_email():
    """Генерирует уникальный email адрес"""
    return fake.email()
