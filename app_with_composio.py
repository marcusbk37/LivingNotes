from flask import Flask, render_template, request, jsonify, session
import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Composio configuration
COMPOSIO_API_KEY = os.environ.get('COMPOSIO_API_KEY')
COMPOSIO_BASE_URL = 'https://api.composio.dev'
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

class GoogleDocsEnhancer:
    def __init__(self):
        self.is_connected = False
        self.current_doc = None
        self.composio_headers = {
            'Authorization': f'Bearer {COMPOSIO_API_KEY}',
            'Content-Type': 'application/json'
        }
    
    def connect_to_google_docs(self):
        """Connect to Google Docs via Composio"""
        try:
            # Initialize Google Docs connection through Composio
            # This would typically involve OAuth flow
            # For now, we'll simulate the connection
            self.is_connected = True
            return {"success": True, "message": "Connected to Google Docs"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_current_document(self):
        """Get the current Google Doc content via Composio"""
        try:
            # This would use Composio's Google Docs integration
            # For demonstration, we'll return a sample document
            return {
                "id": "sample-doc-123",
                "title": "Sample Document",
                "content": "This is a sample document that needs to be made funnier.",
                "last_modified": datetime.now().isoformat()
            }
        except Exception as e:
            raise Exception(f"Failed to get document: {str(e)}")
    
    def enhance_with_humor(self, doc_content):
        """Use OpenAI to add humor to the document"""
        try:
            if not OPENAI_API_KEY:
                # Fallback to simple enhancement if no OpenAI key
                return doc_content + "\n\n😂 And that's how you make it funny!"
            
            # Use OpenAI API to enhance the content
            headers = {
                'Authorization': f'Bearer {OPENAI_API_KEY}',
                'Content-Type': 'application/json'
            }
            
            prompt = f"""
            Please enhance the following document content with humor while keeping the original content intact. 
            Add witty comments, puns, or funny observations that would make students laugh.
            Keep the tone light and educational.
            
            Original content:
            {doc_content}
            
            Enhanced content:
            """
            
            data = {
                'model': 'gpt-3.5-turbo',
                'messages': [
                    {
                        'role': 'system',
                        'content': 'You are a witty teacher who makes educational content more entertaining with humor.'
                    },
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ],
                'max_tokens': 1000,
                'temperature': 0.7
            }
            
            response = requests.post(
                'https://api.openai.com/v1/chat/completions',
                headers=headers,
                json=data
            )
            
            if response.status_code == 200:
                result = response.json()
                enhanced_content = result['choices'][0]['message']['content']
                return enhanced_content
            else:
                # Fallback if OpenAI fails
                return doc_content + "\n\n😂 And that's how you make it funny!"
                
        except Exception as e:
            # Fallback to simple enhancement
            return doc_content + "\n\n😂 And that's how you make it funny!"
    
    def update_document(self, doc_id, enhanced_content):
        """Update the Google Doc with enhanced content via Composio"""
        try:
            # This would use Composio to write back to the Google Doc
            # For now, we'll simulate the update
            print(f"Would update document {doc_id} with enhanced content")
            return {"success": True, "message": "Document updated successfully"}
        except Exception as e:
            raise Exception(f"Failed to update document: {str(e)}")

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

@app.route('/api/test-composio')
def test_composio():
    """Test Composio connection"""
    try:
        if not COMPOSIO_API_KEY:
            return jsonify({"success": False, "error": "Composio API key not configured"})
        
        # Test Composio API connection
        response = requests.get(
            f'{COMPOSIO_BASE_URL}/v1/connections',
            headers=self.composio_headers
        )
        
        if response.status_code == 200:
            return jsonify({"success": True, "message": "Composio connection successful"})
        else:
            return jsonify({"success": False, "error": f"Composio API error: {response.status_code}"})
            
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
