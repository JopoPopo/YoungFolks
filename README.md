# Streamlit Data App

A dual-purpose web application powered by **Streamlit**. This project integrates statistical data analysis with external API consumption to provide users with insights into environmental water quality and daily astronomical discoveries via NASA.

## 🚀 Features
- **Water Quality Analytics**: Interactive display of statistical information and data trends regarding water safety.
- **NASA APOD Integration**: A dedicated section fetching data from NASA’s "Astronomy Picture of the Day" API.
- **LLM Integration**: Extended functionality utilizing Large Language Models for enhanced user interaction.
- **Responsive UI**: A smooth, user-centric design built entirely in Python.

## 🛠️ Project Structure
- `dashboard.py`: The primary frontend script handling the Streamlit UI and data visualizations.
- `apis.py`: The logic layer responsible for external API requests and data fetching.
- `requirements.txt`: List of dependencies (Streamlit, Requests, etc.).
- `README.md`: Project overview and setup instructions.



# FIU Campus Micro-API (Flask)

A minimal Flask web API developed as part of the MC-SDIR assignment. This project provides information about Florida International University (FIU) campuses using RESTful endpoints.

## 🚀 Features
- **Welcome Endpoint**: Returns a JSON greeting.
- **Data Management**: Retrieve or add campus information (supports GET and POST).
- **Health Check**: Monitor API status.

## 🛠️ Project Structure
- `flaskApp2.py`: The main Flask application containing all route logic.
- `test_flask_api.py`: A python script designed to test demonstrate both **GET** and **POST** functionality 
- `requirements.txt`: List of dependencies (Flask).
- `README.md`: Project documentation and Agile process.

# 📄 AI Document Assistant
An intelligent **RAG (Retrieval-Augmented Generation)** application that allows users to upload documents and query them using Google’s generative models.

### Technical Specifications
* **Model Name:** `gemini-3-flash-preview`
* **Source:** Google Generative AI (GenAI Python SDK)
* **Rationale for Selection:** 
The "Flash" series is optimized for low-latency responses, making the chat experience quick and smooth. 
It also handles large document uploads such as PDFs with ease, allowing for detailed analyses.

### ⚖️ Reflection on Responsible AI
As AI integration becomes standard in software development, the responsibility of the developer shifts from sole implementation to ethical consideration. Responsible AI use requires what some may call a "human-in-the-loop" philosophy, ensuring that models are grounded in factual data to prevent the spread of misinformation through hallucinations. Developers must be transparent when it comes to using AI by clearly defining the model's limitations to users and ensuring that generated outputs are accurate and verifiable.

Furthermore, data privacy and security are critical. Implementing responsible AI means protecting user data through secure API management, minimizing data collection/usage, and being aware of potential biases that may appear in training data. As I grow as a developer, I am committed to building tools that leverage the efficiency of Large Language Models while upholding a high standard of digital ethics, security, accountability.
