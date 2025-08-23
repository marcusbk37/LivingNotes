from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import os
from dotenv import load_dotenv

# Import the real Composio SDK
try:
    from composio import Composio
    print("✅ Composio imported successfully!")
except ImportError as e:
    print(f"❌ Composio import failed: {e}")
    print("Please install composio-sdk: pip install composio-sdk")
    exit(1)

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Composio configuration
COMPOSIO_AUTH_CONFIG_ID = os.environ.get('COMPOSIO_AUTH_CONFIG_ID')

# Initialize Composio client
composio_client = Composio()

class GoogleDocsEnhancer:
    def __init__(self):
        self.is_connected = False
        self.current_doc = None
        self.connection_id = None
        self.user_id = "livingnotes-user-001"  # Simple user ID for demo
    
    def connect_to_google_docs(self): # working
        """Connect to Google Docs via Composio using OAuth2"""
        try:
            if not COMPOSIO_AUTH_CONFIG_ID:
                return {"success": False, "error": "Composio auth config ID not configured"}
            
            print(f"🔗 Initiating connection with auth_config_id: {COMPOSIO_AUTH_CONFIG_ID}")
            print(f"🔗 User ID: {self.user_id}")
            
            # Initiate OAuth2 connection using Composio SDK
            connection_request = composio_client.connected_accounts.initiate(
                user_id=self.user_id,
                auth_config_id=COMPOSIO_AUTH_CONFIG_ID,
            )
            
            print(f"✅ Connection request created: {connection_request.id}")
            print(f"🔗 Redirect URL: {connection_request.redirect_url}")
            
            # Store the connection request for later verification
            session['connection_request_id'] = connection_request.id
            
            return {
                "success": True, 
                "message": "OAuth2 initiated successfully",
                "redirect_url": connection_request.redirect_url,
                "connection_id": connection_request.id
            }
                
        except Exception as e:
            print(f"❌ Connection initiation error: {e}")
            import traceback
            traceback.print_exc()
            return {"success": False, "error": str(e)}

enhancer = GoogleDocsEnhancer()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/connect', methods=['POST'])
def connect_google_docs():
    """Connect to Google Docs"""
    try:
        result = enhancer.connect_to_google_docs()
        if result['success']:
            session['connected'] = True
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/verify-connection', methods=['POST'])
def verify_connection():
    """Verify OAuth2 connection completion"""
    try:
        connection_request_id = session.get('connection_request_id')
        if not connection_request_id:
            return jsonify({"success": False, "error": "No connection request found"}), 400
        
        print(f"⏳ Waiting for connection {connection_request_id} to complete...")
        
        try:
            # Get the connected account
            connected_account = composio_client.connected_accounts.get(connection_request_id)
            print(f"✅ Got connected account: {connected_account}")
            print(f"📊 Account status: {connected_account.status}")
            # so this is working... good...
            
            # Check for both 'connected' and 'ACTIVE' statuses
            if connected_account.status in ['connected', 'ACTIVE']:
                enhancer.is_connected = True
                enhancer.connection_id = connection_request_id
                return jsonify({
                    "success": True,
                    "message": "Successfully connected to Google Docs!",
                    "connection_id": connection_request_id
                })
            else:
                return jsonify({
                    "success": False,
                    "error": f"Connection failed: {connected_account.status}"
                }), 400
                
        except Exception as check_error:
            print(f"❌ Check error: {check_error}")
            return jsonify({
                "success": False,
                "error": f"Verification failed: {str(check_error)}"
            }), 500
            
    except Exception as e:
        print(f"Verification error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/status')
def get_status():
    """Get connection status"""
    return jsonify({
        "connected": enhancer.is_connected,
        "current_doc": enhancer.current_doc
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
