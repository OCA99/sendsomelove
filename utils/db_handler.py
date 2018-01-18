from random import randint
from sqlalchemy import or_
from main import app,db
from .models import *
from .values import *

def IDExists(id):
    query = Site.query.filter_by(public_id=id).first()
    return (query == None)


def createID(length=6):
    ret = ""
    i = 0
    for i in range(length):
        n = randint(0, 35)
        if n > 25:
            n += 22
        else:
            n += 97
        ret = ret[:i] + str(chr(n)) + ret[i + 1:]
    return ret


def newSite(title):
	public_id = createID(8)
	site = Site(title, public_id)
	db.session.add(site)
	db.session.commit()
	return public_id