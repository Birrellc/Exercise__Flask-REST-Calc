# Rest Calc Exercise

---
## Notes

Testing was Done with [POSTMAN](https://www.postman.com/)

Doing this exercise again in the future after getting abit more Flask & Python experience again I would look to a maybe a class based approach and using flask-restful package instead of the approach taken this time as I feel it is abit convoluted and contain way too many **if** statements.

---

## Endpoints

### app.py

- ```calc/web/add/x/to/y```
- ```calc/web/subtract/x/from/y```
- ```calc/web/multiply/x/by/y```
- ```calc/web/divide/x/by/y```

- ```calc/api/add/x/to/y```
- ```calc/api/subtract/x/from/y```
- ```calc/api/multiply/x/by/y```
- ```calc/api/divide/x/by/y```

- ```calc/web/sum?numbers=10&numbers=5&numbers=3```
- ```calc/web/product?numbers=10&numbers=5&numbers=3```
- ```calc/web/mean?numbers=10&numbers=5&numbers=3```

- ```calc/api/sum?numbers=10&numbers=5&numbers=3```
- ```calc/api/product?numbers=10&numbers=5&numbers=3```
- ```calc/api/mean?numbers=10&numbers=5&numbers=3```

### app_v2.py

- ```calc/web/add/x/y```
- ```calc/web/subtract/x/y```
- ```calc/web/multiply/x/y```
- ```calc/web/divide/x/y```

- ```calc/api/add/x/y```
- ```calc/api/subtract/x/y```
- ```calc/api/multiply/x/y```
- ```calc/api/divide/x/y```

- ```calc/web/sum?numbers=10&numbers=5&numbers=3```
- ```calc/web/product?numbers=10&numbers=5&numbers=3```
- ```calc/web/mean?numbers=10&numbers=5&numbers=3```

- ```calc/api/sum?numbers=10&numbers=5&numbers=3```
- ```calc/api/product?numbers=10&numbers=5&numbers=3```
- ```calc/api/mean?numbers=10&numbers=5&numbers=3```

---

## Questions

### Part 1 - Arithmetic operations on two numbers

#### Q1) - What happens when we call /calc/web/divide/10/by/4

Dividing 10 by 4 returns 2.5 in python (tried in app, and replit if this was meant to recreating a floating point precision see below) depending by how we wish to handle this I could use 1 of 3 functions in python round() if we wish to round 2.5 up to 3 and lower than 2.5 to 2 (this rounds to the nearest INT), ceil() if we want any decimal over 2 to become 3 (rounds up to the next INT) or math floor if we want all decimals to be rounded down (rounds down to the current INT). This all of course if we want to return only ints and not decimal results which is unlikely for a calculator App but I wanted to cover all bases just incase.

Incase this question was related to floating point precision an example of this being **print(0.1 + 0.2)** would return **0.30000000000000004**. This is due to Python float using double percision numbers to store the value which only haves precision of up to 16 decimal places as most decimal fractions cannot be represented exactly as binary fractions which causes the floating point numbers to only be approximated by the binary floating point numbers stored in the machine. This issue is not just limited to Python but also various other programming languages such as C, C++ etc


#### Q1 - a) - Is the answer accurate (enough)?

Yes as the answer returns **2.5** but see following for the solution to the inaccuracy of using float numbers due to floating point precision.

#### Q1 - b) - Can we make it more accurate?

In order to fix the innaccuracy of using **float** I chose to import the **Decimal Module** from python. Decimal is a floating decimal point type with more precision and a smaller range than the float. Unlike machine based binary floating point, the decimal module has a user alterable precision which can be as large as needed for a given problem. The default precision is 28 places. This solution isn't perfect as it still only contains precision up to 28 places but I feel that is fine for this project and also although **float** provides slightly better performance the accuracy of using **Decimal** outways that con.

#### Q2 - a) What happens when we call /calc/web/divide/10/by/4 ?

Originally when dividing by 0 I was getting a 500 server as dividing by 0 in python the interpreter returns **“ZeroDivisionError: division by zero”** error. In order to fix this issue I chose to go with the **Try, Except** method using **ZeroDivisionError** which is a built in exception in python where the second argument of the division is identified as **0** and using this I return a more user friendly response indicating that you cannot divide by zero.

#### Q1 Optional - 1)

Used Decimal for my calculations and my ZeroDevisionError exception handling:

#### Q1 Optional - 2)

Implemented equation to show a more user friendly representation of the calculation

---

### Part 2 - Arithmetic operations on more than two numbers

#### Q1) - Does the calc/web/mean endpoint return an accurate (enough) answer?

Due to the previous questions I was already aware of protecting against floating point issues so as done previously I used the **Decimal Module** instead of float for returning the result of my calculations. Instead I found another issue when using the **mean** endpoint I found that as I was now working fully in Decimals my return values even if they were a full value for example **3** it would return me **3.0**.

#### Q1 - a) - Can we make it more accurate?

For the floating point accuracy issue I used the **Decimal Module** and To fix the issue described above as I wanted my full values to return without a decimal point I created a helper function which I have since passed all my calculations through in my App. The function I created was a simple solution where I would pass the calculated answer (value to the equation) through my function which would take the result and pass it through the equation of **math.ceil(value) - math.floor(value)** and if after this equation was complete and the result was **0** this would identify that this is a full value and not a decimal so we would return without a trailing decimal place otherwise it would return the answer as a decimal still. for example if we had a **value of 2.0** if we pass that into **math.ceil it still remains 2 as the decimal value is 0 and also the same with math.floor as the value would round down anyways** so it would be **2 - 2 = 0** therefor we have a full value so we should return that instead of a decimal.

#### Q2) What happens when we supply decimal numbers as parameters to these endpoints?#

If we were to take our paramaters as integers only the result of doing this would be a ValueError with a 500 response due to there being an error in the application.
I prevented this issue by using **Decimal**.

#### Q2 - a) If the app does not return the correct answer, how can we fix this?

I did not have this issue due to having my using **Decimal** instead of **int**

#### Q2 - Optional 1)

Problems have been fixed in my code.

---

### Part 3 - Using JSON payload data

#### Q1) - What happens if the JSON does not contain a “Numbers” property?

If we submit JSON without the numbers property we will recieve an error as in order to do the calcuation we need the property specified as **Numbers**

_I somehow managed to use JSON payload data using only a GET request when experimenting with POSTMAN earlier in the week but I used POST in the actual app as from my understanding POST should be used to send data in the body._

#### Q1 - a) - How can we handle this?

I fixed this by adding an **if statement** in the **POST REQUEST** section of my code which handles the **JSON Data**.
what this code does is check to see if the json request contains the **Numbers** property and if not we return a 400 response with a JSON message containing a user friendly explaination of the issue.

#### Q2) - What happens if the array in the “Numbers” property is empty, e.g. []

What happened with my code is that if we have the **Numbers** property and an empty array eg **[]** it actually completed the equation with the result of 0 before I added error handling for this.

#### Q2 - a) How can we handle this?

In order to handle this issue I used ```if 'Numbers' in request.json:``` to check if the **Numbers** property was in my code and if it isn't and there are no paramaters in the url to fall back on we will return a user friendly error with ```error_handler('Incorrect JSON data found', 400)```

#### Q2 - Optional 1)

Problems fixed with the methods provided above and in my code.

---

### Part 4 – Return a JSON response

I managed to setup a JSON response to return in api mode for this application the only issue I had was the failed calculation response with False and null responses. I wasn't sure how to go about how to determine if the calculation had failed.

#### Q1 - a) Web and API modes - How could this be implemented without needing to create any additional endpoints or functions within the Flask app?

As stated in the Question this can be done by **varying the url** and also the use of **if statements**. What we will be doing is making the **URL Dynamic**
for example: ```@app.route('/calculate/<request_type>/sum', methods=['GET', 'POST'])``` in this URL we can apply a different methods in place of ```<request_type>``` in our case we will be using **web** where we continue to return the result as a string and **api** where we will jsonify the response to return the result in JSON.

for example:
```if request.method == 'GET' and request_type == 'web'```
```if request.method == 'GET' and request_type == 'api'```
```elif request.method == 'POST' and request_type == 'api':```

#### Q1 - Optional)

I managed to add a way to switch between api and web in my code.

---

## Resources

- [Flask Docs](https://flask.palletsprojects.com/en/2.1.x/)
- [Python Docs](https://docs.python.org/3/)
- [Decimal](https://docs.python.org/3/library/decimal.html)
- [HTTP Methods](https://www.w3schools.com/tags/ref_httpmethods.asp)
- [GET with JSON](https://stackoverflow.com/questions/978061/http-get-with-request-body)

---