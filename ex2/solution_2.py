class AirTicket:
    def __init__(self, passenger_name, _from, to, date_time, flight, seat, _class, gate):
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __str__(self):
        return (
            f"|{self.passenger_name:<16}"
            f"|{self._from:<4}"
            f"|{self.to:<3}"
            f"|{self.date_time:<16}"
            f"|{self.flight:<20}"
            f"|{self.seat:<4}"
            f"|{self._class:<3}"
            f"|{self.gate:<4}|"
            )

class Load:
    data = []

    @staticmethod
    def write(text):
        with open(text, 'r', encoding="utf8") as file:
            next(file)
          
            for line in file:
                values = line.strip().split(';')[:-1]
                Load.data.append(AirTicket(*values))
