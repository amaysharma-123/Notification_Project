from flask import Blueprint, request, jsonify
from services.queue_manager import notification_queue, notifications_db

api_bp = Blueprint('api', __name__)

@api_bp.route('/notifications', methods=['POST'])
def create_notification():
    data = request.json
    if not data or 'user_id' not in data or 'message' not in data:
        return jsonify({"error": "Missing user_id or message"}), 400

    n_type = data.get('type', 'in-app').lower()
    if n_type not in ('email', 'sms', 'in-app'):
        return jsonify({"error": "Invalid type. Use email/sms/in-app"}), 400

    # Add to queue
    notification_queue.append((data['user_id'], data['message'], n_type))
    
    # Store notification
    if data['user_id'] not in notifications_db:
        notifications_db[data['user_id']] = []
    
    notifications_db[data['user_id']].append({
        'message': data['message'],
        'type': n_type,
        'status': 'queued'
    })

    return jsonify({
        "status": "queued",
        "queue_position": len(notification_queue),
        "user_id": data['user_id']
    }), 202

@api_bp.route('/users/<user_id>/notifications', methods=['GET'])
def get_notifications(user_id):
    return jsonify(notifications_db.get(user_id, []))