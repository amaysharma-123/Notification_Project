@web_bp.route('/')
def demo_interface():
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Notification Service Demo</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
    </head>
    <body class="dark">  <!-- Force dark mode by default -->
        <!-- Theme Toggle Switch - Hidden since we want permanent dark mode -->
        <div class="theme-switch" style="display: none;">
            <label class="switch">
                <input type="checkbox" id="themeToggle" checked disabled>
                <span class="slider"></span>
            </label>
            <span class="theme-label">Dark Mode</span>
        </div>

        <h1>Notification Service Demo</h1>

        <!-- Rest of your HTML remains the same -->
        <div class="panel">
            <h2>Send Notification</h2>
            <form id="sendForm">
                <label for="userId">User ID:</label>
                <input type="text" id="userId" name="userId" placeholder="1" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" placeholder="Hello world!" required></textarea>
                
                <label for="type">Type:</label>
                <select id="type" name="type">
                    <option value="email">Email</option>
                    <option value="sms">SMS</option>
                    <option value="push">Push Notification</option>
                </select>
                
                <button type="submit">Send</button>
            </form>
            <div id="sendResult"></div>
        </div>

        <div class="panel">
            <h2>View Notifications</h2>
            <form id="viewForm">
                <label for="viewUserId">User ID:</label>
                <input type="text" id="viewUserId" name="userId" placeholder="Enter user ID">
                <button type="submit">View</button>
            </form>
            
            <div id="notificationsContainer"></div>
        </div>

        <script>
            document.addEventListener('DOMContentLoaded', function() {
                // Permanently set dark mode
                document.body.classList.add('dark');
                localStorage.setItem('theme', 'dark');

                // Remove theme toggle functionality completely
                const themeSwitch = document.querySelector('.theme-switch');
                if (themeSwitch) themeSwitch.remove();

                // Rest of your JavaScript remains the same
                document.getElementById('sendForm').addEventListener('submit', async function(e) {
                    // ... existing send form code ...
                });

                document.getElementById('viewForm').addEventListener('submit', async function(e) {
                    // ... existing view form code ...
                });
            });
        </script>
    </body>
    </html>
    ''')