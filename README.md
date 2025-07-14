# 🚀 Flask Calculator – DevOps Practice Project

This is a simple web-based calculator built using **Flask (Python)**, designed to help me learn and practice DevOps tools and workflows.
The goal of this project is not complexity, but learning some basic DevOps practices and tools by actually using them. The app itself has very limited functionality but during the development i practiced Git, learned Contenerization with Docker, learned how to automate development with GitHub Actions, and also how to deploy and automate the deployment to AWS.

---

## 🌐 Live Demo

🖥️ App works under this link:  
👉 [http://flask-calculator-env-1.eba-mni3qxqk.eu-central-1.elasticbeanstalk.com](http://flask-calculator-env-1.eba-mni3qxqk.eu-central-1.elasticbeanstalk.com)

⚠️ Warning: The aplication is running on HTTP protocol, the idea was to learn the basics of deployment automation so I didn't set up any custom domain and HTTPS.

---

## 🧰 Tech Stack

- **Language:** Python(Flask)
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Hosting:** AWS Elastic Beanstalk

---

## 📦 Run Locally (with Docker)

```bash
# Build the Docker image
docker build -t flask-calculator .

# Run the app
docker run -p 5000:5000 flask-calculator
