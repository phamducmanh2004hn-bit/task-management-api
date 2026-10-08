from app.models.user import User

def create_user(db, user):
    new_user = User(
        name=user.name,
        email=user.email,
        password=user.password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_user(db, user_id):
    result = db.query(User).filter(User.id == user_id).first()
    return result

def get_users(db):
    return db.query(User).all()

def get_user_tasks(db, user_id):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None
    return db_user.tasks

def update_user(db, user_id, user):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None
    if user.name is not None:
        db_user.name = user.name
    if user.email is not None:
        db_user.email = user.email
    if user.password is not None:
        db_user.password = user.password
    db.commit()
    db.refresh(db_user)

    return db_user

def delete_user(db, user_id):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        return None
    db.delete(db_user)
    db.commit()

    return db_user