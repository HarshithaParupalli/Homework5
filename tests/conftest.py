import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of records to generate")

@pytest.fixture(scope="session")
def fake_records(request):
    num_records = request.config.getoption("--num_records")
    records = []
    for _ in range(num_records):
        a = fake.random_int(min=1, max=100)
        b = fake.random_int(min=1, max=100)
        operation = fake.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
        records.append((a, b, operation))
    return records
