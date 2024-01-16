Generate Code for this requirement: Additional Notes:
The rating system should handle the following cases:
- When a user clicks on a movie rating for the first time, a new MovieRating object should be created to store the user rating in the database.
- When a user clicks on a movie rating for the second time, an existing MovieRating object should be found and the rating should be updated.
- If a user clicks on a movie or TV show rating after the time window has expired, a new rating record should be created.
- If a user clicks on a movie rating for the first time, the user should be redirected to a success page.
- If a user clicks on a movie rating and is not logged in, they should be redirected to the login page.
- If a user clicks on a movie rating for the