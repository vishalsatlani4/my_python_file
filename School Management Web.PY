from flask import Flask, request

app = Flask(__name__)

# List to store students
student = []

# HTML page
html_page = """
<h1>School Admission System</h1>

<form method="POST">
    <input type="text" name="name" placeholder="Enter student name" required>
    <br><br>

    <button type="submit" name="action" value="add">Add</button>
    <button type="submit" name="action" value="remove">Remove</button>
</form>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        name = request.form["name"]
        action = request.form["action"]

        if action == "add":
            student.append(name)
            message = f"{name} added successfully."

        elif action == "remove":
            if name in student:
                student.remove(name)
                message = f"{name} removed successfully."
            else:
                message = f"{name} not found."

    return f"""
    {html_page}
    <h3>{message}</h3>
    <h3>Current Students: {student}</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)