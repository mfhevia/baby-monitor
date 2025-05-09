from app.infrastructure.models import DiaperChangeModel
from fastapi.testclient import TestClient
from app.api.main import app

client = TestClient(app)


def test_create_baby(session):
    # # Arrange: crea una instancia
    # new_baby = Baby(name="Mario Jr", birth_date="2025-05-01")

    # # Act: guarda en la db
    # session.add(new_baby)
    # session.commit()
    # session.refresh(new_baby)

    # Assert: comprueba que se guardó correctamente
    # assert new_baby.id is not None
    # assert new_baby.name == "Mario Jr"
    body = {
        "type": "pee",
        "date": "2025-04-20T10:38:05.652Z"
    }

    response = client.post(
        '/diaper-changes',
        # headers=headers,
        json=body
    )
    assert response.status_code == 201
    data = response.json()
    print(data)
