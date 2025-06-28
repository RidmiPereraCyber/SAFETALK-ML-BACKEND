# Phishing Detection API

A FastAPI-based service that uses a fine-tuned BERT model to detect potential phishing attempts in text. This API leverages the Hugging Face model "ealvaradob/bert-finetuned-phishing" for accurate phishing detection.

## Features

- Real-time phishing detection
- RESTful API endpoint
- Easy integration with existing applications
- Powered by state-of-the-art BERT model

## Prerequisites

- Python 3.7+
- pip (Python package installer)
- Hugging Face API token

## Installation

1. Clone the repository:
```bash
git clone <your-repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Hugging Face API token:
```
HUGGINGFACE_TOKEN=your_token_here
```

## Usage

1. Start the server:
```bash
uvicorn main:app --reload
```

2. The API will be available at `http://localhost:8000`

3. API Endpoint:
   - URL: `/check-phishing`
   - Method: POST
   - Content-Type: application/json
   - Request Body:
     ```json
     {
         "text": "Your text to check for phishing"
     }
     ```

4. Example using curl:
```bash
curl -X POST "http://localhost:8000/check-phishing" \
     -H "Content-Type: application/json" \
     -d '{"text": "Click here to claim your prize!"}'
```

## API Response

The API returns a JSON response with the following structure:

```json
{
    "status": "ok",
    "prediction": {
        "label": "LABEL_0 or LABEL_1",
        "score": 0.95
    }
}
```

- `status`: "ok" for successful requests, "error" for failed requests
- `prediction`: Contains the model's prediction and confidence score
  - `label`: "LABEL_0" for legitimate text, "LABEL_1" for phishing
  - `score`: Confidence score between 0 and 1

## Security Note

⚠️ **Important**: Never commit your Hugging Face API token to version control. Always use environment variables or a secure configuration management system.

## Error Handling

The API includes basic error handling and will return appropriate error messages if:
- The request format is invalid
- The model fails to process the input
- The API token is invalid or expired

## License

[Your chosen license]

## Contributing

[Your contribution guidelines] 