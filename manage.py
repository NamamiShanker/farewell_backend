from project import create_app, populate_db

app = create_app()
populate_db(app)

if __name__ == "__main__":
    app.run()