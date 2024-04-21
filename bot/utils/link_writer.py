from bot.models.models import Link, session


def fill_link(message, url, file_name):
    username = message.from_user.username
    new_link = Link(link=url, username=username, file_name=file_name)
    session.add(new_link)
    session.commit()
