from datetime import datetime, timedelta

def daterange(start, stop, step=timedelta(days=1), inclusive=False):
    current = start
    while current < stop:
        yield current
        current += step
    if inclusive and current == stop:
        yield current

# usage
start = datetime(2022, 1, 1)
end = datetime(2022, 1, 10)

for date in daterange(start, end):
    print(date)