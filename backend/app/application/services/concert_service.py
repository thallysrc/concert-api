
class ConcertService:
    def __init__(self, concert_repository):
        self.concert_repository = concert_repository

    async def create(self, event_data):
        return self.concert_repository.insert(event_data)

    async def get(self, event_id):
        return self.concert_repository.get_all(event_id)

    async def update(self, event_id, event_data):
        return self.concert_repository.update(event_id, event_data)

    async def delete(self, event_id):
        return self.concert_repository.delete(event_id)