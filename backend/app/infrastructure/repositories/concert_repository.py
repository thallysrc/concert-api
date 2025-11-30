from app.infrastructure.models.concert_model import Concert
from datetime import datetime, date


class ConcertRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    def insert(self, concert_data):
        self.db_session.add(concert_data)
        self.db_session.commit()
        self.db_session.refresh(concert_data)
        return concert_data

    def update(self, concert_id: int, data):
        concert = self.get_by_id(concert_id)
        if not concert:
            return None

        for key, value in data.items():
            setattr(concert, key, value)

        self.db_session.commit()
        self.db_session.refresh(concert)
        return concert

    def delete(self, concert_id):
        concert = self.get_by_id(concert_id)
        if concert:
            self.db_session.delete(concert)
            self.db_session.commit()
        return concert

    def get_by_id(self, concert_id):
        return self.db_session.query(Concert).filter(Concert.id == concert_id).first()

    def get(self, filter_params):
        query = self.db_session.query(Concert)

        if filter_params.get("name"):
            query = query.filter(Concert.name.ilike(f"%{filter_params.get("name")}%"))

        return query.all()
