1. Install MySQL and create a new database named 'ece568project'
2. Replace username and password parameters with your owns in the following code. (Default is 'root' and 'mysql'.)
   conn = pymysql.connect("localhost", "root", "mysql", "ece568project")
   You need to alter THREE lines: db_init.py line 5; get_stock.py line 59; get_stock.py line 69.
3. Install 'mymysql' package with pip: 'python3 -m pip install PyMySQL' and 'alpha_vantage' package with pip: 'pip install alpha_vantage'.
4. Change the stock symbol in main.py as you like. (Up to 5 requests per minute and 500 requests per day) 
5. Run main.py