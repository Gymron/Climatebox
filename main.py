from threading import Thread
import Actions
from Webbased_App import create_app

# app = create_app()

# if __name__ == '__main__':
#     app.run(debug=True)

# t1 = Thread(target=Actions.temp)
# threads = [t1]
t2 = Thread(target=Actions.getValuesAndParseData)
threads = [t2]
# t3 = Thread(target=Actions.watertemp)

# t1.start()
t2.start()
# t3.start()
