# from flask_app.controllers import...
from flask_app import app

if __name__=="__main__":
    app.run(debug=True, port = 5001) 
    
    
#1. INSERT queries will return the ID NUMBER of the row inserted
#2. SELECT queries will return the data from the database as a LIST OF DICTIONARIES
#3. UPDATE and DELETE queries will return nothing
#4. If the query fails the method will return FALSE