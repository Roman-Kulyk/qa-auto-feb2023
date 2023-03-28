from src.config.config import config


def test_user_age_is_43(user):
    assert user.age == 43


def test_user_age_is_50(user):
    assert user.age == 50

    
def test_config():
    print(config.get("BASE_URL"))