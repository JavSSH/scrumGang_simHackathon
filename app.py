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

# About Page
@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_text = data.get('message', '').lower()

    try:
        diet_myths = {
            "detox": (
                "Detox diets are a myth.\n"
                "Your liver and kidneys already remove toxins naturally. "
                "There is no scientific evidence that detox juices or cleanses speed this up.\n\n"
                "Tip: Support natural detox by drinking water and eating fiber-rich foods like fruits and vegetables."
            ),
            "carbs make you fat": (
                "Carbs do NOT inherently make you fat.\n"
                "Weight gain happens when you eat more calories than you burn, regardless of macronutrient.\n\n"
                "Tip: Choose whole grains (brown rice, oats) for more fiber and stable energy."
            ),
            "no carbs after 6": (
                "Eating carbs after 6pm does NOT cause weight gain.\n"
                "There is no biological mechanism for this, what matters is total daily calories.\n\n"
                "Tip: Focus on balanced meals rather than timing."
            ),
            "spot reduce": (
                "It’s impossible to 'spot reduce' fat in one area.\n"
                "Fat loss happens across the whole body based on genetics and overall energy balance.\n\n"
                "Tip: Combine balanced diet + physical activity to reduce overall fat."
            ),
            "brown sugar": (
                "Brown sugar is NOT healthier than white sugar.\n"
                "They have almost identical calories and effects on blood sugar.\n\n"
                "Tip: Reduce total added sugar instead of swapping types."
            ),
            "fat free": (
                "Fat-free does NOT mean healthy.\n"
                "Many fat-free products contain extra sugar to improve taste.\n\n"
                "Tip: Choose whole foods with natural healthy fats like nuts, avocado, or olive oil."
            ),
            "bread unhealthy": (
                "Bread is not inherently unhealthy.\n"
                "Wholegrain bread provides fiber, vitamins, and long-lasting energy.\n\n"
                "Tip: Choose wholemeal or multigrain options."
            )
        }

        for myth in diet_myths:
            if myth in user_text:
                return jsonify({"response": diet_myths[myth]})

        if any(goal in user_text for goal in ["lose weight", "weight loss", "slim down"]):
            return jsonify({
                "response": (
                    "For healthy weight loss:\n"
                    "1) Fill half your plate with vegetables\n"
                    "2) Choose whole grains for fiber\n"
                    "3) Eat lean protein like chicken, eggs, tofu\n"
                    "4) Reduce sugary drinks\n\n"
                    "Ask me the calories of any food!"
                )
            })

        if any(goal in user_text for goal in ["gain muscle", "build muscle", "bulk"]):
            return jsonify({
                "response": (
                    "To gain muscle:\n"
                    "1) Aim for 1.2 to 2.0 g of protein per kg of body weight\n"
                    "2) Include protein in every meal (chicken, tofu, fish, Greek yogurt)\n"
                    "3) Combine with strength training\n\n"
                    "Want protein info for a food?"
                )
            })

        if "low carb" in user_text or "keto" in user_text:
            return jsonify({
                "response": (
                    "For a low-carb pattern:\n"
                    "1) Focus on eggs, tofu, fish, meat\n"
                    "2) Include fiber from leafy vegetables\n"
                    "3) Avoid processed 'keto snacks' as they're often high in saturated fat.\n\n"
                    "I can check carbs for any food!"
                )
            })

        if 'recipe' in user_text or 'protein' in user_text:
            return jsonify({"response": "Try Grilled Salmon with Quinoa and Asparagus, which is high in protein & balanced!"})

        if 'calorie' in user_text:
            return jsonify({"response": "A medium banana has about 105 calories, based on standard nutrition databases."})

        if 'pizza' in user_text or 'burger' in user_text:
            return jsonify({"response": "Enjoy it occasionally. Add veggies or a salad to boost fiber!"})

        if 'hello' in user_text or 'hey' in user_text or 'hi' in user_text.split():
            return jsonify({"response": "Hello! I can check calories, debunk diet myths, or suggest healthier swaps."})

        result = rag.search(user_text)

        if result and result["food"] != "Unknown":
            evidence_note = (
                "Values sourced from standard nutritional references used in healthcare and dietetics."
            )

            return jsonify({
                "response":
                    f"Here’s what I found:\n\n"
                    f"{result['food']}\n"
                    f"Calories: {result['calories']}\n"
                    f"Protein: {result['protein']}g\n"
                    f"Carbs: {result['carbohydrates']}g\n"
                    f"Fat: {result['fat']}g\n\n"
                    f"*{evidence_note}*"
            })

        return jsonify({
            "response": (
                "I couldn't find that food.\n"
                "Try asking:\n"
                "• 'calories in chicken rice'\n"
                "• 'is sugar bad for you?'\n"
                "• 'healthy snacks ideas'\n"
                "I'm here to give evidence-based nutrition guidance!"
            )
        })

    except Exception:
        return jsonify({"response": "Oops! Something went wrong, please try again!"})
    
if __name__ == "__main__":
    print("STEP 6: Starting Flask server...")
    app.run(debug=True, use_reloader=True)
