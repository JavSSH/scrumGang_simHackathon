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
        if any(goal in user_text for goal in ["lose weight", "weight loss", "slim down"]):
            return jsonify({
                "response": (
                    "To support weight loss, choose high-fiber foods such as vegetables, fruits, and whole grains.\n"
                    "Try swapping sugary drinks with water or unsweetened tea. "
                    "I can also check calories for you — ask me 'calories in chicken rice'."
                )
            })

        if any(goal in user_text for goal in ["gain muscle", "build muscle", "bulk"]):
            return jsonify({
                "response": (
                    "To build muscle, aim for protein with every meal.\n"
                    "Great options include chicken breast, tofu, eggs, Greek yogurt, or salmon.\n"
                    "Ask me about any food to get protein details!"
                )
            })

        if "low carb" in user_text or "keto" in user_text:
            return jsonify({
                "response": (
                    "For a low-carb pattern, choose foods like eggs, fish, leafy vegetables, tofu, "
                    "and nuts.\n"
                    "Remember: evidence shows healthy fats and fiber are important even on low-carb diets."
                )
            })

        if 'recipe' in user_text or 'protein' in user_text:
            return jsonify({"response": "How about a Grilled Salmon with Quinoa and Asparagus?"})
        
        if 'banana' in user_text:
            return jsonify({"response": "A medium banana has about 105 calories!"})
        
        if 'pizza' in user_text or 'burger' in user_text:
            return jsonify({"response": "Yum! Enjoy it in moderation. Add a salad for extra fiber!"})
        
        if 'hello' in user_text or 'hey' in user_text or ' hi ' in f" {user_text} ":
            return jsonify({"response": "Hello! Ready to eat healthy today? "})
        result = rag.search(user_text)

        if result and result["food"] != "Unknown":
            evidence_statement = (
                "This information is based on standard nutritional databases used in healthcare and dietetics."
            )

            return jsonify({
                "response":
                    f"Here’s what I found:\n\n"
                    f"**{result['food']}**\n"
                    f"Calories: {result['calories']}\n"
                    f"Protein: {result['protein']}g\n"
                    f"Carbs: {result['carbohydrates']}g\n"
                    f"Fat: {result['fat']}g\n\n"
                    f"*{evidence_statement}*"
            })


        return jsonify({
            "response": (
                "I couldn’t find that food. Try asking: 'calories in chicken rice' or "
                "'is brown rice healthier than white rice?'."
            )
        })

    except Exception as e:
        return jsonify({"response": "Oops! Something went wrong."})


if __name__ == "__main__":
    print("STEP 6: Starting Flask server...")
    app.run(debug=True, use_reloader=True)