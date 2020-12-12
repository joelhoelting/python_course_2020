from datetime import datetime, timezone, timedelta

print(datetime.now())
print(datetime.now(timezone.utc))

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)
print(today, tomorrow)
