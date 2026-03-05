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
Integrating Large Language Models (LLMs) into document analysis requires a proactive commitment to accuracy and data privacy. 
In this project, I implemented a strict **System Instruction** to mitigate "hallucinations." 
The model is explicitly programmed to answer *only* using the provided text and to admit when information is missing. 
This "grounding" ensures the tool remains a reliable assistant rather than a source of misinformation.
Furthermore, responsible AI use involves rigorous data hygiene. 
By utilizing a `.env` file for API keys and memory-efficient byte-handling for uploads, the application follows the principle of security-by-design. 
As an intern-ready developer, I recognize that while AI can synthesize information rapidly, human oversight is necessary to validate outputs, especially when dealing with data-driven insights.
