from main import app, db

class Site(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	public_id = db.Column(db.String(20))
	title = db.Column(db.Text)

	def __init__(self, title, public_id):
		self.public_id = public_id
		self.title = title
