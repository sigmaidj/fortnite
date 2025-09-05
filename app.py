from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h2>Mini Proxy Demo</h2>
        <form action="/fetch">
            <input type="text" name="url" placeholder="Enter a URL" style="width:300px;">
            <button type="submit">Fetch</button>
        </form>
    '''

@app.route('/fetch')
def fetch():
    url = request.args.get('url')
    if not url:
        return "Please enter a URL."
    try:
        r = requests.get(url)
        return render_template_string(
            "<h3>Fetched content:</h3><pre>{{content}}</pre>",
            content=r.text[:2000]  # limit to first 2000 chars for safety
        )
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
