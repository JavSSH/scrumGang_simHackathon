from flask import Flask, render_template, request, jsonify
from data_loader import load_nutrition_data
from rag import NutritionRAG

print("STEP 1: App started loading...")

app = Flask(__name__)

print("STEP 2: Importing data...")
df = load_nutrition_data()
print("STEP 3: Data loaded!")

print("STEP 4: Initializing RAG...")
rag = NutritionRAG(df)
print("STEP 5: RAG ready!")
# Main/Home Page
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/features")
def features():
    return render_template("features.html")

@app.route("/about")
def about():
    return render_template("about.html")



@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_text = data.get('message', '').lower()

   
    try:
        result = rag.search(user_text)
        if result and result["food"] != "Unknown":
            return jsonify({
                "response": f"Here’s what I found:\n\n"
                            f"🍽️ **{result['food']}**\n"
                            f"🔥 Calories: {result['calories']}\n"
                            f"💪 Protein: {result['protein']}g\n"
                            f"🥔 Carbs: {result['carbohydrates']}g\n"
                            f"🧈 Fat: {result['fat']}g"
            })
    except:
        pass

    
    if 'recipe' in user_text or 'protein' in user_text:
        response = "How about a Grilled Salmon with Quinoa and Asparagus?"
    elif 'calorie' in user_text:
        response = "A medium banana has about 105 calories!"
    elif 'pizza' in user_text or 'burger' in user_text:
        response = "Yum! Remember to balance with fiber 🥗."
    elif 'hello' in user_text or 'hey' in user_text or ' hi ' in f" {user_text} ":
        response = "Hello! Ready to eat healthy today? 🍎"
    else:
        response = "I couldn’t find that food in my database. Try asking: 'calories in chicken rice'."

    return jsonify({'response': response})


if __name__ == "__main__":
    print("STEP 6: Starting Flask server...")
    app.run(debug=True, use_reloader=True)
