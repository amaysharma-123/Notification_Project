from collections import deque
import threading
from services.notification import NotificationService

notification_queue = deque()
notifications_db = {}

def process_queue():
    while True:
        if notification_queue:
            user_id, message, n_type = notification_queue.popleft()
            
            # Send notification
            success = False
            if n_type == 'email':
                success = NotificationService.send_email(user_id, message)
            elif n_type == 'sms':
                success = NotificationService.send_sms(user_id, message)
            else:
                success = NotificationService.send_in_app(user_id, message)
            
            # Update status
            for notif in notifications_db.get(user_id, []):
                if notif['message'] == message and notif['status'] == 'queued':
                    notif['status'] = 'sent' if success else 'failed'
                    break
        
        time.sleep(2)  # Process every 2 seconds

def start_queue_processor():
    threading.Thread(target=process_queue, daemon=True).start()