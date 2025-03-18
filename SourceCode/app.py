from flask import Flask, render_template, request
import random  # For generating random accuracies (simulated)

app = Flask(__name__)

# Simulating results for different methods
def get_accuracy_results(selected_method, dataset_name):
    # Simulated accuracies for different methods
    methods = {
        "BGEO-TVFL": random.uniform(90, 95),
        "BWOA": random.uniform(85, 90),
        "BGWO": random.uniform(80, 85),
        "ACO": random.uniform(75, 80),
        "ABC": random.uniform(70, 75),
    }

    # Simulated time taken for execution
    time_taken = random.uniform(1.0, 5.0)  # Time in seconds

    # Check if the selected method is valid
    if selected_method in methods:
        accuracy = methods[selected_method]
        return {selected_method: round(accuracy, 2)}, round(time_taken, 2)
    else:
        # Return an error message if the method is invalid
        return {"Error": f"Method '{selected_method}' not found"}, round(time_taken, 2)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Retrieve the selected method and dataset
        selected_method = request.form.get('method')
        file = request.files.get('dataset')

        if file and selected_method:
            dataset_name = file.filename
            # Save the uploaded file (optional)
            file.save(f"upload/{dataset_name}")

            # Simulate results for the dataset and selected method
            accuracy_results, time_taken = get_accuracy_results(selected_method, dataset_name)

            # Redirect to the result page with necessary data
            return render_template(
                'result.html',
                dataset=dataset_name,
                method=selected_method,
                results=accuracy_results,  # Pass as a dictionary
                time=time_taken
            )

    # Render the upload page if GET request
    return render_template('upload.html')


@app.route('/flowchart')
def flowchart():
    return render_template('flowchart.html')

@app.route('/modelevaluationmetrics')
def modelevaluationmetrics():
    return render_template('modelevaluationmetrics.html')

if __name__ == '__main__':
    app.run(debug=True)
