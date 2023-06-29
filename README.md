# AI Phishing Detection

This Python script utilizes artificial intelligence to detect phishing URLs. It interacts with the ChatGPT API to determine if a given URL is a phishing URL. If it is determined to be a phishing URL, it retrieves the IP address of the URL using ip-api.com and saves it to a database.

## Prerequisites

- Python 3.x
- Dependencies: `urllib`, `socket`, `g4f` (GPT-4), `requests`, `json`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/lopekinz/AI-phishing-detector.git
```

2. Install the required dependencies:

```bash
pip install urllib3 socket g4f requests
```

3. No OpenAI Token needed. thanks to [xtekky](https://github.com/xtekky/gpt4free)

## Usage

1. Run the `AI-Phishing.py` script:

```bash
python AI-Phishing.py
```

2. The script will iterate over established connections and check if they are open URLs.
3. If a URL is detected, it will interact with the ChatGPT API to determine if it is a phishing URL.
4. The script will print the URL and the phishing result (True/False) obtained from the API.
5. If the URL is determined to be a phishing URL, it will retrieve the IP address and save it to the `database.json` file.


## AI Responses & Proof of Concept
![alt text](https://github.com/LopeKinz/AI-Phishing-Detector/blob/main/IMG_2426.png?raw=true)
## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

