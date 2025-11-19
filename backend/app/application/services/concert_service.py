
class ConcertService:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    async def create_concert(self, event_data):
        return self.event_repository.add_event(event_data)

    def get_event(self, event_id):
        return self.event_repository.get_event_by_id(event_id)

    def update_event(self, event_id, event_data):
        return self.event_repository.update_event(event_id, event_data)

    def delete_event(self, event_id):
        return self.event_repository.delete_event(event_id)