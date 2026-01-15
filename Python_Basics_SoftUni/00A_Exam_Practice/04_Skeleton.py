quota_minutes = int(input()) * 60
quota_seconds = int(input())
track_meters = float(input())
time_for_100_track_meters = int(input())

quota_total_time = quota_minutes + quota_seconds
delay = (track_meters / 120) * 2.5

marin_time = ((track_meters / 100) * time_for_100_track_meters) - delay

if marin_time <= quota_total_time:
    print(f"Marin Bangiev won an Olympic quota!\nHis time is {marin_time:.3f}.")

else:
    print(f"No, Marin failed! He was {marin_time - quota_total_time:.3f} second slower.")