from flask import Flask, render_template, redirect, request, jsonify

app = Flask(__name__)

# Main/Home Page
@app.route("/")
def index():
    return render_template("index.html")

# Features Page
@app.route("/features")
def features():
    return render_template("features.html")

# About Us Page
@app.route("/about")
def about():
    return render_template("about.html")

# API route to handle chat messages
@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_text = data.get('message', '').lower()
    
    # Simple Rule-Based Logic (Harcoded for now to test frontend logic)
    if 'recipe' in user_text or 'protein' in user_text:
        response = "How about a Grilled Salmon with Quinoa and Asparagus? It's rich in Omega-3 and high protein!"
    
    elif 'calorie' in user_text or 'fat' in user_text:
        response = "I can help calculate that. A medium banana usually has about 105 calories. Are you tracking macros?"
    
    elif 'pizza' in user_text or 'burger' in user_text:
        response = "Tasty choice! Remember, balance is key. Maybe add a side salad to get some fiber? 🥗"

    # Added spaces to ' hi ' to ensure it matches the whole word, not just a substring
    elif 'hello' in user_text or 'hey' in user_text or 'yo' in user_text or ' hi ' in f" {user_text} ":
        response = "Hello! Ready to eat healthy today? 🍎"
        
    else:
        response = "I'm still learning! Could you ask me about recipes, calories, or specific foods?"

    return jsonify({'response': response})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)