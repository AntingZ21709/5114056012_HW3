# Deploying to Streamlit Cloud

This guide provides step-by-step instructions for deploying your Streamlit application to Streamlit Cloud.

## 1. GitHub Repository Setup

1.  **Create a new GitHub repository:** Go to [github.com/new](https://github.com/new) and create a new public repository. Let's call it `spam-classifier-app`.

2.  **Initialize a Git repository locally:** Open your terminal or command prompt, navigate to your project's root directory, and run:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```

3.  **Push your local repository to GitHub:**
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/spam-classifier-app.git
    git branch -M main
    git push -u origin main
    ```
    (Replace `YOUR_USERNAME` with your GitHub username).

## 2. Configure `requirements.txt`

Ensure your `requirements.txt` file lists all the necessary libraries. Your current `requirements.txt` should be sufficient:

```
scikit-learn
pandas
numpy
matplotlib
seaborn
streamlit
joblib
```

## 3. Deploy on Streamlit Cloud

1.  **Sign up or log in:** Go to [share.streamlit.io](https://share.streamlit.io/) and sign up using your GitHub account.

2.  **Create a new app:**
    *   Click the "New app" button.
    *   Choose the repository you just created (`spam-classifier-app`).
    *   Select the `main` branch.
    *   Set the "Main file path" to `app/app.py`.
    *   Click "Deploy!".

Streamlit will now build and deploy your application. This may take a few minutes.

## 4. Update README.md with a Demo Link

Once your app is deployed, Streamlit will provide you with a URL (e.g., `https://your-app-name.streamlit.app`).

1.  **Copy the URL.**

2.  **Edit your `README.md` file:** Add a badge or a simple link to your deployed app. Here are some options:

    **Markdown Badge:**
    ```markdown
    [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-name.streamlit.app)
    ```

    **Simple Link:**
    ```markdown
    [Live Demo](https://your-app-name.streamlit.app)
    ```

3.  **Commit and push the change to your `README.md`:**
    ```bash
    git add README.md
    git commit -m "Add link to live demo"
    git push
    ```

Your `README.md` will now have a link to your live Streamlit application.
