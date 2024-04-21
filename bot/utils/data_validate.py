from sqlalchemy.exc import NoResultFound

from bot.models.models import User, session


def validate_data(message):
    try:
        user = session.query(User).filter(User.id == message.from_user.id).one()
        if user.name != message.from_user.first_name or user.username != message.from_user.username:
            user.name = message.from_user.first_name
            user.username = message.from_user.username
            session.commit()
    except NoResultFound:
        user = User(
            id=message.from_user.id,
            name=message.from_user.first_name,
            username=message.from_user.username,
        )
        session.add(user)
        session.commit()
    finally:
        session.close()
