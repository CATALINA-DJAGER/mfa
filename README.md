# MFA #

## In this mega awesome project i automate sending letters to travellers with check-in details for aircompanies that don't provide electronic boarding passes. As an example I am taking the aircompany Bees Airlines (7B).
## Staging:
- open Travellizy Admin site
- open Check-in list for the actual date
- parse this list for e-mail addresses and aircompany names
- from that info choose all of the e-mail addresses related to 7B aircompany
- open e-mail app
- paste all of the e-mail adresses vhosen earlier to Bcc
- make the letter using template (html script already exists)
- add the aircompany name to the template
- send the letters
- go back to Travellizy Admin site
- open Check-in list for actual date
- change the orders 7B fro the actual date to status 'Done' (there are three possible status options: Check-in, Cancelled, Done)

## Models:
* CheckIn (status, aircompany, traveller)
* Aircompany (code, name)
* Traveller (email)
traveller email (traveller, email)
* Email (template)
* Template (html script, aircompany name)
