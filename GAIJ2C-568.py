Generate Code for this requirement: Important Notes:
- Use cases for this feature include creating and reading a watchlist, adding and removing items to a watchlist, and checking if an item is on the watchlist.
- You should take into consideration the following scenarios when designing this feature:
    - Adding a movie to the watchlist.
    - Adding a TV show to the watchlist.
    - Adding an episode to the watchlist.
    - Viewing the watchlist.
    - Removing an item from the watchlist.
    - Updating the watchlist.
    - Reading the watchlist for a person.
- Make sure the API endpoints are well-documented and provide clear instructions on how to use them.
- Provide a testing strategy to ensure the functionality of the features.


Given I am a logged in user with an existing watchlist
When I add a movie to my watchlist
Then the movie should be added to my watchlist
And the watchlist item should have the correct attributes and values
And the movie should be accessible through the watchlist API
And the watchlist count should be updated
And I should be able to retrieve the movie from the watchlist

Given I am a logged in user with an existing watchlist
When I add a TV show to my watchlist
Then the TV show should be added to my watchlist
And the watchlist item should have the correct attributes and values
And the TV show should be accessible through the watchlist API
And the watchlist count should be updated
And I should be able to retrieve the TV show from the watchlist

Given I am a logged in user with an existing watchlist
When I add an episode to my watchlist
Then the episode should be added