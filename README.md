# Dynamic Greeting Message API

A Flask web service that provides personalized greeting messages based on time of day, timezone, and language preferences. Perfect for deployment on Render or any cloud platform.

## Features

- **Dynamic Greetings**: Time-based greetings (morning, afternoon, evening, night)
- **Multi-language Support**: English, Spanish, French, German, and Hindi
- **Timezone Aware**: Support for any valid pytz timezone
- **Multiple Response Formats**: JSON or plain text responses
- **Health Check Endpoint**: For monitoring and deployment validation
- **CORS Enabled**: Ready for frontend integration
- **Error Handling**: Comprehensive error responses with helpful messages

## API Endpoints

### 1. Health Check
- **GET** `/` or `/health`
- Returns service status and basic information

**Response:**
```json
{
  "status": "healthy",
  "service": "Dynamic Greeting API",
  "timestamp": "2025-09-30T10:30:00",
  "version": "1.0.0"
}
```

### 2. Dynamic Greeting
- **GET** `/greeting`
- Returns personalized greeting based on current time

**Query Parameters:**
- `name` (optional): Name to greet (default: "World")
- `timezone` (optional): Timezone for time calculation (default: "UTC")
- `format` (optional): Response format "json" or "text" (default: "json")
- `language` (optional): Language code "en", "es", "fr", "de", "hi" (default: "en")

**Example Requests:**
```
GET /greeting
GET /greeting?name=John&timezone=US/Eastern
GET /greeting?name=Maria&timezone=Europe/Madrid&language=es
GET /greeting?name=Pierre&timezone=Europe/Paris&language=fr&format=text
```

**JSON Response Example:**
```json
{
  "greeting": "Good morning",
  "message": "Good morning, John! Today is Monday, September 30, 2025. The current time is 06:30 in US/Eastern.",
  "name": "John",
  "day": "Monday",
  "date": "September 30, 2025",
  "time": "06:30",
  "timestamp": "2025-09-30T06:30:00-04:00",
  "timezone": "US/Eastern",
  "language": "en",
  "greeting_type": "morning"
}
```

**Text Response Example:**
```
Good morning, John! Today is Monday, September 30, 2025. The current time is 06:30 in US/Eastern.
```

### 3. Available Timezones
- **GET** `/timezones`
- Returns list of commonly used timezones

### 4. Supported Languages
- **GET** `/languages`
- Returns list of supported languages with their codes

## Greeting Time Ranges

- **Morning**: 5:00 AM - 11:59 AM
- **Afternoon**: 12:00 PM - 4:59 PM  
- **Evening**: 5:00 PM - 8:59 PM
- **Night**: 9:00 PM - 4:59 AM

## Supported Languages

| Code | Language | Morning | Afternoon | Evening | Night |
|------|----------|---------|-----------|---------|-------|
| en   | English  | Good morning | Good afternoon | Good evening | Good night |
| es   | Spanish  | Buenos días | Buenas tardes | Buenas tardes | Buenas noches |
| fr   | French   | Bonjour | Bon après-midi | Bonsoir | Bonne nuit |
| de   | German   | Guten Morgen | Guten Tag | Guten Abend | Gute Nacht |
| hi   | Hindi    | सुप्रभात | नमस्ते | शुभ संध्या | शुभ रात्रि |

## Common Timezones

- UTC
- US/Eastern, US/Central, US/Mountain, US/Pacific
- Europe/London, Europe/Paris, Europe/Berlin
- Asia/Tokyo, Asia/Shanghai, Asia/Kolkata, Asia/Dubai
- Australia/Sydney, Australia/Melbourne

## Local Development

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)

### Setup
1. Clone or download the project
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running Locally
```bash
python app.py
```

The service will start on `http://localhost:5000`

### Testing the API
```bash
# Health check
curl http://localhost:5000/health

# Basic greeting
curl http://localhost:5000/greeting

# Personalized greeting with timezone
curl "http://localhost:5000/greeting?name=Alice&timezone=US/Pacific"

# Multi-language greeting
curl "http://localhost:5000/greeting?name=José&timezone=Europe/Madrid&language=es"

# Text format response
curl "http://localhost:5000/greeting?name=Bob&format=text"
```

## Deployment

This Flask application is ready for deployment on various cloud platforms. The project includes:

- `requirements.txt` - All necessary Python dependencies
- `Procfile` - Process configuration for deployment platforms
- `runtime.txt` - Python version specification

### Environment Variables

For production deployment, you may want to set:
- `PORT` - Server port (automatically configured by most platforms)
- `PYTHON_VERSION` - Python version to use

## Project Structure

```
Dynamic_greetingMessage/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # Process file for deployment
├── runtime.txt        # Python version specification
└── README.md          # This documentation
```

## Error Handling

The API includes comprehensive error handling:

- **400 Bad Request**: Invalid timezone or format parameters
- **404 Not Found**: Endpoint not found with helpful endpoint list
- **500 Internal Server Error**: Server-side errors

## CORS Support

Cross-Origin Resource Sharing (CORS) is enabled for all domains, making it easy to integrate with frontend applications.

## Security Features

- Input sanitization for name parameter
- Length limits on user inputs
- Safe timezone validation
- Proper error responses without exposing internal details

## Performance Considerations

- Lightweight Flask application
- Efficient timezone calculations
- Minimal external dependencies
- Ready for horizontal scaling

## License

This project is open source and available under the MIT License.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For issues or questions:
1. Check the error responses - they include helpful messages
2. Verify timezone names using the `/timezones` endpoint
3. Test locally before deploying
4. Check application logs for any deployment issues