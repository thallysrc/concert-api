
class ConcertService:
    def __init__(self, event_repository):
        self.event_repository = event_repository

    def create_event(self, event_data):
        # Business logic for creating an event
        return self.event_repository.add_event(event_data)

    def get_event(self, event_id):
        # Business logic for retrieving an event
        return self.event_repository.get_event_by_id(event_id)

    def update_event(self, event_id, event_data):
        # Business logic for updating an event
        return self.event_repository.update_event(event_id, event_data)

    def delete_event(self, event_id):
        # Business logic for deleting an event
        return self.event_repository.delete_event(event_id)