from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

answer_dict={
                "1": ["Black"],
                "2": ["mouse"],
                "3": ["smelly"]
            }




#ADD stories data here!
stories = [
    {
        "inputs": 1,
        "title": "Guess the word!",
        "story": '<span class="rep_input">_____</span> Hint: It is a colour',
        "words": ["Black"],
        "story_id": "1"
    },
    {
        "inputs": 1,
        "title": "Guess the word!",
        "story": '<span class="rep_input">_____</span> Hint: It is a small animal',
        "words": ["Mouse"],
        "story_id": "2"
    },
    {
        "inputs": 1,
        "title": "Guess the word!",
        "story": '<span class="rep_input">_____</span> Hint: It is an adjective that describes bad odors',
        "words": ["Smelly"],
        "story_id": "3"
    }
]




@app.route("/")
def index():
    return render_template("index.html")
    

#ADD "/get-story" API here!!
@app.rout("/get-story")


def get_story():
    return jsonify({
        "status": "success",
        "story": random.choice(stories) 
    })


@app.route("/post-answers", methods=["POST"])
def post_answers():
    story_id = request.json.get("story_id")
    values = request.json.get("values")
    answers = answer_dict.get(story_id)
    index, score = 0, 0
    while index < len(values):
        if values[index].lower() == answers[index].lower():
            score += 1
        index += 1
    return jsonify({
        "status": "success",
        "result": f"{score} / {len(values)}"
    })

if __name__ == "__main__":
    app.run(debug=True)