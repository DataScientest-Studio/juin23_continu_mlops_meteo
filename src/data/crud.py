from sqlalchemy.orm import Session

from data import models, schemas



def get_weatherAUS_data(db: Session):
    return db.query(models.WeatherAUS).all()


def get_weatherSYDNEY_data(db: Session):
    return db.query(models.WeatherAUS).filter(models.WeatherAUS.Location == 'Sydney').limit(5).all()
