# 🎭 LivingNotes - Google Docs Humor Enhancement

A hackathon project that transforms boring Google Docs into comedy gold using Python, Flask, and Composio integration! Make schoolwork engaging enough to compete against Instagram and Tiktok.

## 🚀 Features

- **Simple Web Interface**: Clean, modern UI with just two buttons
- **Google Docs Integration**: Seamless connection via Composio
- **AI-Powered Enhancements**: Uses OpenAI to add any style of enhancement (sarcastic humor, anime storytelling, poetry/rhyming, etc.) based on custom user prompts
- **Real-time Updates**: Directly edits your Google Docs
- **Preserves Original Content**: Keeps your work intact while adding humor
- **Python Backend**: Robust Flask server with API endpoints

## 🛠️ Tech Stack

- **Backend**: Python 3.8+, Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Integration**: Composio (for Google Docs API)
- **AI**: OpenAI GPT-3.5-turbo for humor generation
- **Styling**: Modern gradient design with smooth animations

## 📁 Project Structure

```
LivingNotes/
├── app.py                    # Basic Flask application
├── app_with_composio.py      # Enhanced version with Composio integration
├── requirements.txt          # Python dependencies
├── env.example              # Environment variables template
├── templates/
│   └── index.html           # Main web interface
└── README.md                # This file
```

## 🎯 How It Works

1. **Connect**: User clicks "Connect Google Docs" to authenticate via Composio
2. **Select**: User opens their Google Doc (or we detect the current one)
3. **Enhance**: User clicks "Make My Doc Funny!" to trigger AI enhancement
4. **Transform**: OpenAI GPT analyzes the document and adds humor while preserving content
5. **Update**: Enhanced content is directly written back to the Google Doc via Composio

## 🔧 Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables

Copy `env.example` to `.env` and fill in your API keys:

```bash
cp env.example .env
```

Edit `.env` with your actual API keys:
```env
SECRET_KEY=your-secret-key-here
COMPOSIO_API_KEY=your-composio-api-key-here
OPENAI_API_KEY=your-openai-api-key-here
```

### 3. Get API Keys

#### Composio API Key
1. Sign up at [Composio](https://composio.dev)
2. Create a new project
3. Configure Google Docs integration
4. Get your API key from the dashboard

#### OpenAI API Key
1. Sign up at [OpenAI](https://platform.openai.com)
2. Create an API key
3. Add billing information (required for API usage)

### 4. Run the Application

#### Basic Version (Simulated)
```bash
python app.py
```

#### Enhanced Version (With Composio)
```bash
python app_with_composio.py
```

The application will be available at `http://localhost:5001`

## 🔧 Composio Integration

The app uses Composio to:
- Authenticate with Google Docs
- Read document content
- Write enhanced content back to documents
- Handle OAuth flow seamlessly

### Required Composio Setup

1. **Google Docs Connection**: Set up Google Docs integration in Composio
2. **API Endpoints**: Configure endpoints for:
   - Document reading
   - Document writing
   - User authentication
3. **Permissions**: Ensure proper scopes for document access

## 🎨 UI Features

- **Responsive Design**: Works on desktop and mobile
- **Status Indicators**: Real-time connection and processing status
- **Loading Animations**: Smooth feedback during operations
- **Error Handling**: Clear error messages for troubleshooting
- **Modern Aesthetics**: Gradient backgrounds and smooth transitions
- **Content Preview**: See enhanced content before it's applied

## 🚀 API Endpoints

- `GET /` - Main application page
- `POST /api/connect` - Connect to Google Docs
- `POST /api/enhance` - Enhance document with humor
- `GET /api/status` - Get connection status
- `GET /api/test-composio` - Test Composio connection

## 🔮 Future Enhancements

- **Batch Processing**: Enhance multiple documents at once
- **Collaboration**: Share funny documents with classmates
- **Analytics**: Track which documents get the most laughs

## 🎪 Hackathon Goals

- ✅ Simple, intuitive interface
- ✅ Google Docs integration via Composio
- ✅ AI-powered humor enhancement with OpenAI
- ✅ Real-time document updates
- ✅ Modern, attractive design
- ✅ Python backend with Flask
- ✅ RESTful API endpoints

## 📝 Development Notes

### Current Implementation
- The basic version (`app.py`) includes simulated API calls
- The enhanced version (`app_with_composio.py`) includes actual Composio and OpenAI integration
- Both versions work for demonstration purposes

### Production Considerations
- Add proper error handling and logging
- Implement rate limiting for API calls
- Add user authentication and session management
- Use environment-specific configurations
- Add comprehensive testing

## 🐛 Troubleshooting

### Common Issues

1. **Composio Connection Fails**
   - Verify your Composio API key is correct
   - Check that Google Docs integration is properly configured
   - Ensure proper OAuth scopes are set

2. **OpenAI API Errors**
   - Verify your OpenAI API key is valid
   - Check your OpenAI account has sufficient credits
   - Ensure the API key has proper permissions

3. **Flask Server Issues**
   - Check all dependencies are installed: `pip install -r requirements.txt`
   - Verify environment variables are set correctly
   - Check port 5000 is available

## 🤝 Contributing

This is a hackathon project! Feel free to:
- Add new features
- Improve the UI/UX
- Enhance the humor algorithms
- Add more integration options
- Optimize performance

## 📄 License

This project is created for educational and hackathon purposes.

---

**Made with ❤️ for making education more entertaining!**
