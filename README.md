# bank-admin-backend

## Backend Coding Test

Create a REST service that can fetch bank details, using the data given in the API’s query parameters. The data is obtained is available at: **https://github.com/snarayanank2/indian_banks**. The services are written using Django and the application is hosted on Heroku. PostgreSQL is used for the backend DB and since the free-tier of Heroku has a limit of 10k rows, **_clever-cloud.com_** was used to host the database.

The usecases of the application:

1. Autocomplete API to return possible matches based on the branch name ordered by IFSC code (ascending order) with limit and offset.
    - Endpoint: /api/branches/autocomplete?q=<>
    - Example: /api/branches/autocomplete?q=RTGS&limit=3&offset=0

2. Search API to return possible matches across all columns and all rows, ordered by IFSC code (ascending order) with limit and offset.
   
    - Endpoint: /api/branches?q=<>
    - Example: /api/branches?q=Bangalore&limit=4&offset=0


## API Urls

1. Autocomplete API - https://aanandhivb-1.herokuapp.com/api/branches/autocomplete?q=ERNAKULAM&limit=3&offset=2

2. Search API - https://aanandhivb-1.herokuapp.com/api/branches?q=TRIVANDRUM&limit=5&offset=1
