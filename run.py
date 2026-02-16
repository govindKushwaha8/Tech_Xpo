from app import create_app

app = create_app()

if __name__ == '__main__':
    print("Starting Flask server at http://localhost:5000")
    # Run the app on port 5000
    app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=5000, debug=True)
