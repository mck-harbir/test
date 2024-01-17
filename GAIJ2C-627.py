Generate Code for this requirement: - Users should be able to add a default budget to their account, which will be automatically applied to new transactions.
- Users should be able to remove a default budget from their account, or modify the associated time period or category.
- Users should be able to view and edit their existing budgets, and delete unnecessary budgets.
- Budget categories should not include items at the "Income" or "Transfer" levels, as these categories are set by the system.
- Budget items should be created with the "Budget" account type, and should have lower priority than other account types.
- Budget items should be saved with the same order as they were created.
- Budgets should be displayed in chronological order when sorted by the date they were created.
- Users should not be able to create a budget if they have a high enough account balance.
- Users should not be able to create a budget if they have a high enough unclaimed balance.
- Users should not be able to create a budget if they have a high enough net balance.
- Users should not be able to create a budget if they are currently in debt.



**Bug Fixes**

ISSUE: Transaction search box does not display expected results if the user has entered a query.

**Acceptance Criteria:**
- The transaction search results should display only transactions matching the search query and not display all transactions.
- After a query is entered in the transaction search bar, the displayed transaction information should update to match the result of the search instead of displaying all transactions.
- After a query is entered in the transaction search bar and the user clicks on an item in the search results, the user should be