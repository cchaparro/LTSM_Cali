import os  
from  simple_app import app



if __name__=='__main__':
    app.debug = True
    host=os.environ.get('IP', 'localhost')
    port= int(os.environ.get('PORT', 8080))
    app.run(host=host,port=port)
                                                                                                                                    