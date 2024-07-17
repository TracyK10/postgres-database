from app import app
from models import db, User

with app.app_context():
    print('Deleting existing users...')
    User.query.delete()
    
    print('Creating users...')
    Tracy = User(username='Tracy', email='deofi@bawanu.by')
    Jane = User(username='Jane', email='gebkef@vardewow.hk')
    Malakai = User(username='Malakai', email='dudoffon@fa.az')
    
    print('Adding users to transactions...')
    db.session.add_all([Tracy, Jane, Malakai])
    
    print("Committing transaction...")
    db.session.commit()
    
    print('Complete')
    