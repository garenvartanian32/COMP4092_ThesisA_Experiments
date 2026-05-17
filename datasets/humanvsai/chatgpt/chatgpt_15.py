import time

def refresh_hamster(refresh_secs):
    # Load today's activity
    today_activity = load_today_activity()
    print('Today activity:', today_activity)
    
    # Check last activity
    last_activity = check_last_activity()
    print('Last activity:', last_activity)
    
    # Wait for refresh_secs seconds
    time.sleep(refresh_secs)
