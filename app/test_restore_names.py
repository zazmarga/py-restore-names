import pytest

from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list[dict]:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    return users


def test_restore_names(users_template: list[dict]) -> None:
    restore_names(users_template)
    for user in users_template:
        assert user["first_name"] == user["full_name"].split()[0]
