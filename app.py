from flask import Flask, request, jsonify
from datetime import datetime
import pytz
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all domains

# Health check endpoint
@app.route('/', methods=['GET'])
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint for deployment monitoring"""
    return jsonify({
        'status': 'healthy',
        'service': 'Dynamic Greeting API',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0'
    })

@app.route('/greeting', methods=['GET'])
def dynamic_greeting():
    """
    Dynamic greeting endpoint that returns personalized greetings based on time of day
    
    Query Parameters:
    - name (str, optional): Name to greet. Default: 'World'
    - timezone (str, optional): Timezone for time calculation. Default: 'UTC'
    - format (str, optional): Response format 'json' or 'text'. Default: 'json'
    - language (str, optional): Language for greeting. Default: 'en'
    """
    # Get query parameters with defaults
    name = request.args.get('name', 'World')
    timezone = request.args.get('timezone', 'UTC')
    format_type = request.args.get('format', 'json')  # 'json' or 'text'
    language = request.args.get('language', 'en')  # Language support
    
    # Validate name parameter (basic sanitization)
    if not name or len(name.strip()) == 0:
        name = 'World'
    else:
        name = name.strip()[:50]  # Limit name length
    
    # Validate format parameter
    if format_type.lower() not in ['json', 'text']:
        return jsonify({'error': 'Invalid format. Use "json" or "text"'}), 400
    
    # Validate timezone
    try:
        tz = pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        return jsonify({'error': f'Invalid timezone: {timezone}. Use standard timezone names like "UTC", "US/Eastern", "Europe/London", etc.'}), 400
    
    # Get current time in specified timezone
    current_time = datetime.now(tz)
    hour = current_time.hour
    
    # Multi-language greetings
    greetings = {
        'en': {
            'morning': 'Good morning',
            'afternoon': 'Good afternoon', 
            'evening': 'Good evening',
            'night': 'Good night'
        },
        'es': {
            'morning': 'Buenos días',
            'afternoon': 'Buenas tardes',
            'evening': 'Buenas tardes',
            'night': 'Buenas noches'
        },
        'fr': {
            'morning': 'Bonjour',
            'afternoon': 'Bon après-midi',
            'evening': 'Bonsoir',
            'night': 'Bonne nuit'
        },
        'de': {
            'morning': 'Guten Morgen',
            'afternoon': 'Guten Tag',
            'evening': 'Guten Abend',
            'night': 'Gute Nacht'
        },
        'hi': {
            'morning': 'सुप्रभात',
            'afternoon': 'नमस्ते',
            'evening': 'शुभ संध्या',
            'night': 'शुभ रात्रि'
        }
    }
    
    # Default to English if language not supported
    if language not in greetings:
        language = 'en'
    
    # Determine greeting based on time of day
    if 5 <= hour < 12:
        greeting_key = 'morning'
    elif 12 <= hour < 17:
        greeting_key = 'afternoon'
    elif 17 <= hour < 21:
        greeting_key = 'evening'
    else:
        greeting_key = 'night'
    
    greeting = greetings[language][greeting_key]
    
    # Format response
    day_name = current_time.strftime('%A')
    date_str = current_time.strftime('%B %d, %Y')
    time_str = current_time.strftime('%H:%M')
    
    message = f"{greeting}, {name}! Today is {day_name}, {date_str}. The current time is {time_str} in {timezone}."
    
    if format_type.lower() == 'text':
        return message, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    else:
        return jsonify({
            'greeting': greeting,
            'message': message,
            'name': name,
            'day': day_name,
            'date': date_str,
            'time': time_str,
            'timestamp': current_time.isoformat(),
            'timezone': timezone,
            'language': language,
            'greeting_type': greeting_key
        })

@app.route('/timezones', methods=['GET'])
def list_timezones():
    """
    Returns a list of commonly used timezones
    """
    common_timezones = [
        'UTC',
        'US/Eastern', 'US/Central', 'US/Mountain', 'US/Pacific',
        'Europe/London', 'Europe/Paris', 'Europe/Berlin', 'Europe/Rome',
        'Asia/Tokyo', 'Asia/Shanghai', 'Asia/Kolkata', 'Asia/Dubai',
        'Australia/Sydney', 'Australia/Melbourne',
        'America/New_York', 'America/Chicago', 'America/Denver', 'America/Los_Angeles',
        'America/Toronto', 'America/Vancouver',
        'Asia/Singapore', 'Asia/Bangkok', 'Asia/Jakarta'
    ]
    
    return jsonify({
        'timezones': common_timezones,
        'note': 'This is a subset of available timezones. You can use any valid pytz timezone name.'
    })

@app.route('/languages', methods=['GET'])
def list_languages():
    """
    Returns supported languages for greetings
    """
    languages = {
        'en': 'English',
        'es': 'Spanish',
        'fr': 'French', 
        'de': 'German',
        'hi': 'Hindi'
    }
    
    return jsonify({
        'supported_languages': languages,
        'default': 'en'
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Endpoint not found',
        'available_endpoints': {
            '/': 'Health check',
            '/health': 'Health check',
            '/greeting': 'Dynamic greeting message',
            '/timezones': 'List of common timezones',
            '/languages': 'List of supported languages'
        }
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)