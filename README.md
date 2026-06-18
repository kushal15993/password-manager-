# 🔐 Password Manager - Flask Web Application

A secure password manager built with Flask and Python that encrypts and stores your passwords locally.

## Features

✅ **Secure Password Storage** - Passwords encrypted using Fernet (AES) encryption  
✅ **User-Friendly Interface** - Clean, modern UI for managing passwords  
✅ **Search Functionality** - Quickly find passwords by website or username  
✅ **Database Integration** - SQLite database for persistent storage  
✅ **Full CRUD Operations** - Create, Read, Update, and Delete passwords  
✅ **Date Tracking** - Automatically tracks when passwords were added  

## Tech Stack

- **Backend:** Flask (Python web framework)
- **Database:** SQLite with SQLAlchemy ORM
- **Encryption:** Cryptography library (Fernet)
- **Frontend:** HTML5, CSS3
- **Version Control:** Git

## Installation & Setup

### 1. Clone or Download the Project
```bash
cd password_manager
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

The app will run on `http://localhost:5000`

## How to Use

1. **Home Page** - View all saved passwords
2. **Add Password** - Click "Add Password" to store new credentials
3. **View Password** - Click "View" to see decrypted password
4. **Search** - Use search bar to find passwords quickly
5. **Delete** - Remove passwords you no longer need

## Security Features

- **Encryption:** All passwords are encrypted with Fernet (symmetric encryption)
- **Secret Key:** Automatically generated and stored in `secret.key` file
- **Local Storage:** Everything stays on your machine - no cloud upload
- **Session Management:** Flask session handling for security

## File Structure

```
password_manager/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── secret.key            # Encryption key (auto-generated, KEEP SAFE!)
├── database.db           # SQLite database (auto-created)
└── templates/
    ├── base.html         # Base template with navigation
    ├── index.html        # Home page - list all passwords
    ├── add_password.html # Form to add new password
    └── view_password.html# View decrypted password
```

## Important Security Notes ⚠️

1. **BACKUP YOUR SECRET KEY!**
   - Without `secret.key`, you cannot decrypt your passwords
   - Store it somewhere safe (encrypted backup)

2. **BACKUP YOUR DATABASE!**
   - Keep `database.db` backed up regularly
   - Store backups in secure location

3. **DO NOT SHARE:**
   - Your `secret.key` file
   - Your `database.db` file
   - Your GitHub repository if making it public

## Deployment Options

### Option 1: Deploy on Render.com (Free)
1. Push to GitHub (make sure to add `secret.key` and `database.db` to `.gitignore`)
2. Create account on Render.com
3. Connect GitHub repo
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`

### Option 2: Deploy on Heroku (Paid)
Similar process - Heroku provides free tier alternatives

### Option 3: Deploy on PythonAnywhere
Easy Python hosting with free tier available

## Future Enhancement Ideas

- User authentication system
- Password strength checker
- Two-factor authentication
- Password generation feature
- Export/Import functionality
- Dark mode theme
- Mobile app version

## Resume Points

When adding this to your resume, highlight:
✅ Built a full-stack Flask web application  
✅ Implemented encryption using cryptography library  
✅ Designed database schema with SQLAlchemy ORM  
✅ Created responsive UI with HTML/CSS  
✅ Implemented CRUD operations  
✅ Demonstrates cybersecurity best practices  

## Code Quality

- Clean, well-commented code
- PEP 8 compliant
- Modular structure
- Proper error handling
- Security best practices

## License

Feel free to use this for learning and portfolio purposes.

## Questions?

For issues or improvements, refer to Flask documentation: https://flask.palletsprojects.com/
