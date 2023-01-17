from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for r in self.rooms:
            if r.number == room_number:
                r.take_room(people)
                self.guests += people

    def free_room(self, room_number):
        for r in self.rooms:
            if r.number == room_number:
                self.guests -= r.guests
                r.free_room()

    def status(self):
        tot_guests = 0
        for x in self.rooms:
            tot_guests += x.guests
        text = f"Hotel {self.name} has {tot_guests} total guests\n"
        text += f"Free rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken == False])}\n"
        text += f"Taken rooms: {', '.join([str(x.number) for x in self.rooms if x.is_taken])}"
        return text
