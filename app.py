from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    total = None
    average = None
    grade = None

    if request.method == "POST":
        try:
            # Get marks (3 to 5 subjects)
            marks = []

            for i in range(1, 6):
                value = request.form.get(f"sub{i}")
                if value:
                    marks.append(float(value))

            if len(marks) >= 3:
                total = sum(marks)
                average = total / len(marks)

                # Grade calculation
                if average >= 90:
                    grade = "A+"
                elif average >= 80:
                    grade = "A"
                elif average >= 70:
                    grade = "B"
                elif average >= 60:
                    grade = "C"
                elif average >= 50:
                    grade = "D"
                else:
                    grade = "F"
            else:
                grade = "Enter at least 3 subjects"

        except:
            grade = "Invalid input"

    return render_template("index.html", total=total, average=average, grade=grade)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))