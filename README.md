# EmailNERTrips
The objective of the MOKB-construction project is to extract structured information from unstructured text written in natural language.  The purpose of doing so is to store the structured information in a database and query it using database access languages such as SQL, which cannot be applied to free text.
For example, consider an email chain in which employees discuss, among other things, a planned trip. The MOKB-construction software will extract from the text a record with fields:

Who (the entity taking the trip, maybe a group of people), From-location, Departure-time, Departure-date, To-location, Arrival-time, arrival-date etc.

By extracting such information from the emails of a company a relation of trips can be extracted, and later queried by SQL. Observe that the email texts cannot be queried in this fashion.
