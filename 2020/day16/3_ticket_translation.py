from functools import reduce, wraps
from collections import defaultdict
import operator
import time


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('func:{}  took: {:2.4f} sec'.format(f.__name__, te - ts))
        return result

    return wrap


def _checkinrange(value, field_ranges):
    for field, ranges in field_ranges.items():
        for range in ranges:
            if range[0] <= value <= range[1]:
                return True
    return False


def _checkinfieldrange(ticket, field_ranges, found_fields=[]):
    fields = []
    for field, ranges in field_ranges.items():

        if all(ranges[0][0] <= value <= ranges[0][1] or ranges[1][0] <= value <= ranges[1][1] for value in ticket):
            fields.append(field)

    return fields


@timing
def part1_countinvalidtickets(ticket_data):
    field_ranges = ticket_data['fields']
    return sum(value for ticket in ticket_data['nearyby_tickets'] for value in ticket if
               not _checkinrange(value, field_ranges))


@timing
def part2_productofdepartures(ticket_data):
    field_ranges = ticket_data['fields']

    valid_tickets = [ticket for ticket in ticket_data['nearyby_tickets'] if
                     all(_checkinrange(value, field_ranges) for value in ticket)]

    valid_tickets_length = len(valid_tickets)
    field_positions = defaultdict(list)

    for i in range(len(valid_tickets[0])):
        fields = _checkinfieldrange([valid_tickets[j][i] for j in range(valid_tickets_length)], field_ranges)
        for field in fields:
            field_positions[field].append(i)

    found_positions = []

    # find single postion for each field and
    # remove this positions from other field in while loop untill all fields has one position
    while len(found_positions) < len(field_positions):
        for field, positions in field_positions.items():
            if isinstance(positions, list):
                if len(positions) == 1:
                    field_positions[field] = positions[0]
                    found_positions.append(positions[0])
                elif isinstance(positions, list):
                    field_positions[field] = [x for x in positions if x not in found_positions]

    return reduce(operator.mul, [ticket_data['your_ticket'][pos] for field, pos in field_positions.items() if
                                 field.startswith('departure')])


def read_input(filename):
    with open(filename) as file:
        ticket_data = {'fields': {}, 'your_ticket': [], 'nearyby_tickets': []}
        nearyby_tickets = your_ticket = False
        for line in file:
            if line.strip():
                field = line.strip().split(':')[0]
                if field != 'your ticket' and field != 'nearby tickets' and not nearyby_tickets and not your_ticket:
                    _, data = line.strip().split(':')
                    ticket_data['fields'][field] = tuple(
                        tuple(map(int, x.strip().split('-'))) for x in data.strip().split(' or '))
                elif field == 'your ticket':
                    your_ticket = True
                elif field == 'nearby tickets':
                    nearyby_tickets = True
                    your_ticket = False
                elif your_ticket:
                    ticket_data['your_ticket'] = list(map(int, line.strip().split(',')))
                elif nearyby_tickets:
                    ticket_data['nearyby_tickets'].append(list(map(int, line.strip().split(','))))

    return ticket_data


if __name__ == '__main__':
    # ticket_data = read_input('day16_sample_input2.txt')
    ticket_data = read_input("input1")
    part1_ans = part1_countinvalidtickets(ticket_data)
    print("part1 answer", part1_ans)
    part2_ans = part2_productofdepartures(ticket_data)
    print("part2 answer", part2_ans)
