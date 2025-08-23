from flask import Flask, render_template, request, jsonify, session
import os
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Composio integration will be added here
# For now, we'll simulate the functionality

class GoogleDocsEnhancer:
    def __init__(self):
        self.is_connected = False
        self.current_doc = None
    
    def connect_to_google_docs(self):
        """Connect to Google Docs via Composio"""
        # This would use Composio's Python SDK
        # For now, we'll simulate the connection
        self.is_connected = True
        return {"success": True, "message": "Connected to Google Docs"}
    
    def get_current_document(self):
        """Get the current Google Doc content"""
        # This would use Composio to fetch the current document
        return {
            "id": "sample-doc-123",
            "title": "Sample Document",
            "content": "This is a sample document that needs to be made funnier.",
            "last_modified": datetime.now().isoformat()
        }
    
    def enhance_with_humor(self, doc_content):
        """Use LLM to add humor to the document"""
        # This would integrate with an LLM service
        # For now, we'll simulate the enhancement
        enhanced_content = doc_content + "\n\n😂 And that's how you make it funny!"
        return enhanced_content
    
    def update_document(self, doc_id, enhanced_content):
        """Update the Google Doc with enhanced content"""
        # This would use Composio to write back to the document
        return {"success": True, "message": "Document updated successfully"}

enhancer = GoogleDocsEnhancer()

@app.route('/')
def landing():
    """Landing page"""
    return render_template('landing.html')

@app.route('/auth')
def auth():
    """Authentication page"""
    return render_template('auth.html')

@app.route('/app')
def index():
    """Main application page"""
    return render_template('index.html')

@app.route('/api/connect', methods=['POST'])
def connect_google_docs():
    """Connect to Google Docs"""
    try:
        result = enhancer.connect_to_google_docs()
        session['connected'] = True
        return jsonify(result)
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@app.route('/api/enhance', methods=['POST'])
def enhance_document():
    """Enhance the current document with humor"""
    try:
        if not enhancer.is_connected:
            return jsonify({"success": False, "error": "Not connected to Google Docs"}), 400
        
        # Get current document
        doc = enhancer.get_current_document()
        
        # Enhance with humor
        enhanced_content = enhancer.enhance_with_humor(doc['content'])
        
        # Update the document
        result = enhancer.update_document(doc['id'], enhanced_content)
        
        return jsonify({
            "success": True,
            "message": "Document enhanced successfully!",
            "original_content": doc['content'],
            "enhanced_content": enhanced_content
        })
        
    except Exception as e:
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
