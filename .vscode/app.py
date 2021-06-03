from flask import Flask, g
from database import get_db

app = Flask(__name__)

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
@app.route('/member', methods=['GET'])
def get_members():
    return 'This returns all the members'

@app.route('/member/<int:member_id>', methods=['GET'])    
def get_member(member_id):
    return 'This returns one member'

@app.route('/member', methods=['POST'])
def add_member():
    return 'adds member'

@app.route('/member/<int:member_id>', methods=['PUT','PATCH'])
def edit_member(member_id):
    return 'edit member'


@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    return 'delete member'

if __name__ == '__main__':
    app.run(debug=True)

