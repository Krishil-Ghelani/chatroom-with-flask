from base import app

print("in app")

if __name__ == '__main__':
    app.run(port=9999, threaded=True)
