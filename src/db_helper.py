import mysql.connector
class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''       
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="dg_assignment_employees"
        )

        cursor=mydb.cursor()
        cursor.execute("select max(salary) from salaries")
        res=cursor.fetchall()               
        return res[0][0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="",
          database="dg_assignment_employees"
        )

        cursor=mydb.cursor()
        cursor.execute("select min(salary) from salaries")
        res=cursor.fetchall()               
        return res[0][0]        

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)