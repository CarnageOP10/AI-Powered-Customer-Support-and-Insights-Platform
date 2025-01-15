<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title></title>
</head>
<body>
    <h1>AI-Powered Customer Support and Insights Platform</h1>

<p>This repository contains a Flask-based web application integrated with AI capabilities to manage customer queries effectively. The platform classifies product complaints, determines their severity, and stores the data in a PostgreSQL database for further insights.</p>

<h2>Features</h2>
    <ul>
        <li><strong>Raise Alert Form:</strong> A user-friendly form to collect product complaints and associated details.</li>
        <li><strong>AI-Powered Classification:</strong> Automatically classifies complaints into product types (<code>GPU</code>, <code>CPU</code>, <code>Monitor</code>) and assesses severity on a scale of 0–3 using a structured LLM-based model.</li>
        <li><strong>Database Integration:</strong> Stores complaint data, including AI-generated classifications, in a PostgreSQL database.</li>
        <li><strong>Custom Routes and Templates:</strong> Modularized routes and dynamic HTML templates for seamless navigation and user experience.</li>
    </ul>

<h2>Prerequisites</h2>
    <h3>Software Requirements</h3>
    <ul>
        <li>Python 3.8 or higher</li>
        <li>PostgreSQL 14 or higher</li>
    </ul>

<h3>Python Libraries</h3>
    <p>Install the required Python libraries using pip:</p>
    <pre><code>pip install flask flask_sqlalchemy flask_wtf psycopg2 langchain</code></pre>

<h3>Environment Variables</h3>
    <p>Ensure the following environment variables are set for integrating the AI model:</p>
    <ul>
        <li><code>groq_api_key</code>: API key for Groq</li>
        <li><code>langchain_api_key</code>: API key for LangChain</li>
        <li><code>langchain_endpoint</code>: Endpoint for LangChain</li>
    </ul>

<h2>Getting Started</h2>

<h3>Step 1: Clone the Repository</h3>
    <pre><code>git clone https://github.com/CarnageOP10/AI-Powered-Customer-Support-and-Insights-Platform.git
cd AI-Powered-Customer-Support-and-Insights-Platform
</code></pre>

<h3>Step 2: Set Up the Database</h3>
    <p>Create a PostgreSQL database named <code>querydb</code> on <code>localhost:urport</code> with the necessary credentials:</p>
    <pre><code>CREATE DATABASE querydb;
CREATE USER postgres WITH ENCRYPTED PASSWORD 'ex:Kratos1000Kratos';
GRANT ALL PRIVILEGES ON DATABASE querydb TO postgres;
</code></pre>

<h3>Step 3: Initialize the Database</h3>
    <p>In the Python shell:</p>
    <pre><code>from custom import db
db.create_all()
</code></pre>

<h3>Step 4: Run the Application</h3>
    <p>Start the Flask server:</p>
    <pre><code>python app.py</code></pre>
    <p>Visit the application at <a href="http://127.0.0.1:5000" target="_blank">http://127.0.0.1:5000</a>.</p>

<h2>AI Model Integration</h2>
    <p>The AI model is implemented using <strong>LangChain</strong> and <strong>Groq</strong> to classify complaints:</p>
    <ul>
        <li><strong>Product Type Classification:</strong> Categorizes complaints into <code>GPU</code>, <code>CPU</code>, or <code>Monitor</code>.</li>
        <li><strong>Severity Assessment:</strong> Evaluates severity on a scale from 0 (normal) to 3 (urgent).</li>
        <li><strong>Short Description Generation:</strong> Summarizes the complaint.</li>
    </ul>

<h3>Example Prompt</h3>
    <pre><code>Product description: {query}</code></pre>

<h2>Future Enhancements</h2>
    <ul>
        <li>Add user authentication and role-based access control.</li>
        <li>Integrate real-time analytics for monitoring complaints.</li>
        <li>Implement feedback loops for improving AI classification accuracy.</li>
    </ul>

<h2>Contributors</h2>
    <ul>
        <li><strong>Parth</strong> (<a href="https://github.com/CarnageOP10" target="_blank">@CarnageOP10</a>)</li>
    </ul>
</body>
</html>
