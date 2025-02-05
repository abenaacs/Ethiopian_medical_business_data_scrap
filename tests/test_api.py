from fastapi.testclient import TestClient
from api.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from api.database import Base
from api.models import MedicalBusiness

# Set up a test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[app.get_db] = override_get_db

client = TestClient(app)


class TestAPI(unittest.TestCase):
    def test_create_business(self):
        response = client.post(
            "/businesses/",
            json={"name": "Test Business", "description": "A test business"},
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], "Test Business")

    def test_read_business(self):
        # Create a business first
        client.post(
            "/businesses/",
            json={"name": "Test Business", "description": "A test business"},
        )

        # Retrieve the business
        response = client.get("/businesses/1")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["name"], "Test Business")


if __name__ == "__main__":
    unittest.main()
