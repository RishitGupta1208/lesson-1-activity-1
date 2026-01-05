import random
from datetime import datetime, timedelta
start=datetime(2024,1,1)
end=datetime(2026,6,7)
random_date=start+timedelta(days=random.randint(0,(end-start).days))
print(random_date)