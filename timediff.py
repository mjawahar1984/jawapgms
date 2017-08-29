from datetime import datetime, time as dt_time, timedelta

def time_diff(initial, end):
    if isinstance(initial, dt_time):
        assert isinstance(end, dt_time)
        initial, end = [datetime.combine(datetime.min, t) for t in [initial, end]]
    if initial <= end:
        return end - initial
    else:
        end += timedelta(1)
        assert end > initial
        return end - initial

for time_range in ['08:20:15-10:25:30', '23:59:00-00:01:01']:
    s, e = [datetime.strptime(t, '%H:%M:%S') for t in time_range.split('-')]
    print(time_diff(s, e))
    assert time_diff(s, e) == time_diff(s.time(), e.time())
