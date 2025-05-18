import time

class NotificationService:
    @staticmethod
    def send_email(user_id, message, max_retries=3):
        for attempt in range(max_retries):
            try:
                print(f" [Attempt {attempt+1}/{max_retries}] Email to {user_id}: {message}")
                time.sleep(1)
                if "fail" not in message.lower():
                    return True
                raise Exception("Simulated failure")
            except Exception as e:
                if attempt == max_retries - 1:
                    print(f" Email failed after {max_retries} tries")
                    return False
                time.sleep(2)

    @staticmethod
    def send_sms(user_id, message, max_retries=2):
        for attempt in range(max_retries):
            print(f" [Attempt {attempt+1}/{max_retries}] SMS to {user_id}: {message}")
            time.sleep(0.5)
            if "fail" not in message.lower():
                return True
        print(f" SMS failed after {max_retries} tries")
        return False

    @staticmethod
    def send_in_app(user_id, message):
        print(f" In-App to {user_id}: {message}")
        return True