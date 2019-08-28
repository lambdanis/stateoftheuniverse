from datetime import datetime

import pytest

from widgets.sun import get_sun_info


def datetimes_equal_minutes(dt1, dt2):
    """Assert that two datetimes are equal with precision to minutes."""
    return datetime(*dt1.timetuple()[:5]) == datetime(*dt2.timetuple()[:5])


@pytest.mark.parametrize('dt, lat, lon, expected', [
    # Cambridge, before sunrise
    (datetime(2019, 8, 27, 4, 0), 52.2, 0.11667,
     (datetime(2019, 8, 27, 5, 1), datetime(2019, 8, 27, 18, 59))),
    # Cambridge, after sunrise
    (datetime(2019, 8, 27, 16, 0), 52.2, 0.11667,
     (datetime(2019, 8, 27, 5, 1), datetime(2019, 8, 27, 18, 59))),
])
def test_sun_info(dt, lat, lon, expected):
    result = get_sun_info(dt, lat, lon)
    assert datetimes_equal_minutes(result[0], expected[0])
    assert datetimes_equal_minutes(result[1], expected[1])
