from datetime import datetime

name = "Максим"
location = "Індія"
activity = "Відпочиває"

print(f"{name} Година {activity}  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}. {location} Існує")
