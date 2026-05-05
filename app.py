from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    total = None
    average = None
    grade = None
    error = None

    if request.method == "POST":
        marks = []

        # Collect marks from form (sub1 to sub5)
        for i in range(1, 6):
            value = request.form.get(f"sub{i}")

            if value:  # only if user entered something
                try:
                    mark = float(value)

                    # Validate range
                    if 0 <= mark <= 100:
                        marks.append(mark)
                    else:
                        error = "Marks must be between 0 and 100"
                        return render_template("index.html", error=error)

                except ValueError:
                    error = "Please enter valid numeric values"
                    return render_template("index.html", error=error)

        # Ensure at least 3 subjects
        if len(marks) < 3:
            error = "Enter at least 3 subjects"
            return render_template("index.html", error=error)

        # Calculations
        total = sum(marks)
        average = total / len(marks)

        # Grade logic
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

    return render_template(
        "index.html",
        total=total,
        average=average,
        grade=grade,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))