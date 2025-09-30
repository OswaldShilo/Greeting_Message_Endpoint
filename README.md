<div align="center">

<h1 style="font-family: Arial, sans-serif; font-weight: 700;">
Dynamic Greeting Message API
</h1>
<!-- GIF -->
<p align="center">
  <img src="https://media.giphy.com/media/Cmr1OMJ2FN0B2/giphy.gif" alt="Hello GIF" />
</p>



[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.68%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

### Overview ⚡

A FastAPI-based dynamic greeting service with multilingual support, time awareness, text/JSON output, and easy deployment.

---


### Live Endpoint 🌐

Deployed on Render:  
**https://greeting-message-endpoint.onrender.com**

---

## Features ✅

- Dynamic, time-based greetings
- Multi-language responses (EN, ES, FR, DE, HI)
- Timezone support with pytz
- JSON or text responses
- Health check endpoint
- CORS enabled
- Error handling

---

## API Endpoints

### 1. Health Check
`GET /` or `/health`

```json
{
  "status": "healthy",
  "service": "Dynamic Greeting API",
  "timestamp": "2025-09-30T10:30:00",
  "version": "1.0.0"
}
````

### 2. Dynamic Greeting

`GET /greeting`

**Query Parameters:**

* name (optional)
* timezone (optional)
* format ("json" or "text")
* language ("en", "es", "fr", "de", "hi")

Example:

```
GET /greeting?name=John&timezone=US/Eastern
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

### 3. Timezones

`GET /timezones`

### 4. Supported Languages

`GET /languages`

---

## Greeting Time Ranges

| Period    | Time Range         |
| --------- | ------------------ |
| Morning   | 5:00 AM - 11:59 AM |
| Afternoon | 12:00 PM - 4:59 PM |
| Evening   | 5:00 PM - 8:59 PM  |
| Night     | 9:00 PM - 4:59 AM  |

---

## Supported Languages

| Code | Language | Morning      | Afternoon      | Evening       | Night         |
| ---- | -------- | ------------ | -------------- | ------------- | ------------- |
| en   | English  | Good morning | Good afternoon | Good evening  | Good night    |
| es   | Spanish  | Buenos días  | Buenas tardes  | Buenas tardes | Buenas noches |
| fr   | French   | Bonjour      | Bon après-midi | Bonsoir       | Bonne nuit    |
| de   | German   | Guten Morgen | Guten Tag      | Guten Abend   | Gute Nacht    |
| hi   | Hindi    | सुप्रभात     | नमस्ते         | शुभ संध्या    | शुभ रात्रि    |

---

## Common Timezones

* UTC
* US/Eastern, US/Central, US/Mountain, US/Pacific
* Europe/London, Europe/Paris, Europe/Berlin
* Asia/Tokyo, Asia/Shanghai, Asia/Kolkata, Asia/Dubai
* Australia/Sydney, Australia/Melbourne

---

## Local Development 🛠

**Prerequisites**

* Python 3.11+
* pip

**Setup**

```bash
pip install -r requirements.txt
```

**Run**

```bash
python app.py
```

Server: `http://localhost:5000`

---

## Testing the API

```bash
curl http://localhost:5000/health
curl http://localhost:5000/greeting
curl "http://localhost:5000/greeting?name=Alice&timezone=US/Pacific"
curl "http://localhost:5000/greeting?name=José&timezone=Europe/Madrid&language=es"
curl "http://localhost:5000/greeting?name=Bob&format=text"
```

---

## Deployment

Includes:

* requirements.txt
* Procfile
* runtime.txt

Environment Variables:

* PORT
* PYTHON_VERSION

---

## Project Structure

```
Dynamic_greetingMessage/
├── app.py
├── requirements.txt
├── Procfile
├── runtime.txt
└── README.md
```

---

## Error Handling

* 400 – Invalid params
* 404 – Endpoint not found
* 500 – Internal server error

---

## CORS

Enabled for all domains.

---

## Security

* Input sanitization
* Length restrictions
* Timezone validation
* Clean error responses

---

## Performance

* Lightweight Flask app
* Efficient timezone logic
* Minimal dependencies
* Horizontal scaling ready
  
---

## License

MIT License ✅

---

## Contributing

1. Fork
2. Create branch
3. Add updates
4. Submit pull request

---

## Support

* Inspect error responses
* Use `/timezones` and `/languages`
* Test locally
* Check logs if deployed
