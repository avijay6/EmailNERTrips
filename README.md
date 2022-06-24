# EmailNERTrips
The objective of the MOKB-construction project is to extract structured information from unstructured text written in natural language.  The purpose of doing so is to store the structured information in a database and query it using database access languages such as SQL, which cannot be applied to free text.
For example, consider an email chain in which employees discuss, among other things, a planned trip. The MOKB-construction software will extract from the text a record with fields:

Who (the entity taking the trip, maybe a group of people), From-location, Departure-time, Departure-date, To-location, Arrival-time, arrival-date etc.

By extracting such information from the emails of a company a relation of trips can be extracted, and later queried by SQL. Observe that the email texts cannot be queried in this fashion.


Emailchainextract python code 
It extracts the email chain documents and stores in a text file. The documents mentioned in the text file are the ones that need to be trained

Emailproc python 
It gets the email messages from different emails and writes into each line which can be fed into the slot filling tool for prediction




INSTRUCTIONS ON RUNNING THE SCRIPTS:

1. Download the files using the scripts from download_scripts.py
2. After downloading the files and saving it to a folder, use the getting travel relevant emails python script to get the travel relevant emails from this list. This step is to make your labelling easy by assuming that trips may be present in these filtered emails. We are using a keyword based search for getting the travel relevant emails.
3. Now we get a list of travel relevant emails.
4. Read through each email from this list to find a valid trip and label the attributes appropriately. 
5. The list of labels we need are TRAVELPER, FROMLOC, TOLOC, DEPARTDATE, DEPARTIME, ARRIVDATE, ARRIVTIME
6. You also need to tokenize each labelled document and write to a csv file with the attributes: Emailno, Sentno, Words, Labels. You can use the script tokenize and write to csv python script for this purpose. 
7. Write the label in the last column of this csv file in BIO format. (B-beginning, I-inside, O-outside of entity)
For example: Senator Barack Obama continues his overseas trip with, today travelling to Israel and the West Bank.

Barack B-TRAVELPER
Obama I-TRAVELPER
Israel B-TOLOC
West B-TOLOC
Bank I-TOLOC
