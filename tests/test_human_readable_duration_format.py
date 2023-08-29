seconds_duration = {
    "year": 60 * 60 * 24 * 365,
    "month": 60 * 60 * 24 * 30,
    "day": 60 * 60 * 24,
    "hour": 60 * 60,
    "minute": 60,
    "second": 1
}


def get_durations(seconds, durations=None):
    if durations is None:
        durations = []
    if seconds == 0 and len(durations) == 0:
        return ["now"]
    for key, value in seconds_duration.items():
        if seconds >= value:
            amount = int(seconds / value)
            durations.append(f"{amount} {key if amount == 1 else key + 's'}")
            return get_durations(seconds % value, durations)
    return durations


def format_duration(seconds):
    durations = get_durations(seconds)
    if len(durations) > 1:
        return ", ".join(durations[:-1]) + f" and {durations[-1]}"
    return durations[-1]


def test_human_readable_duration_format():
    assert format_duration(0) == "now"
    assert format_duration(1) == "1 second"
    assert format_duration(62) == "1 minute and 2 seconds"
    assert format_duration(120) == "2 minutes"
    assert format_duration(3600) == "1 hour"
    assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"
