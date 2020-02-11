# Consumption application API using Django REST Framework
## Problem Statement:
 - Using Django and DRF, build an API that can create and retrieve usage information for electricity and water usage.
 - On a daily basis the API will called to store the date and time, type (water, electicity, rainfall) and the amount.
 - The 'type' filed should be customisable in the Admin Panel so that the API is extendable, to collect other data such as rainfall.
 - When creating an entry for a type, return the data that was posted to the API and the total amount of the current month of the type.
 - The list view of the API should allow for filtering by type and by date ranges.
 - Extra points for:
  - Deployment
  - Containerisation
  - CI/CD
 - Use testing throughout.
 
