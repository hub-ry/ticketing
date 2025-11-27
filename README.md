# ticketing

## The Goal

Create a custom and modular system to do the ticketing for events (or anything really) which works across devices without needing an internet connection. Originally being created for the Purdue Grand Prix.


## The Plan (Ruhaan's Perspective - this is very open to change)

### QR Codes

Reference Link I am using (https://www.fielddrive.com/blog/qr-code-tickets)

The data stored in a QR code is generally harder to scan and replicate given the fact that data points have been translated to pixels and stored in a non-intuitive format. Furthermore, a scanner will increase the line speed on the day of the event given that the access times of the data and verification will be faster as no manual work is needed for the fetching process.

The QR Code can be modified to hold any piece of information, however the parameters I am thinking include:

1. First Name
2. Last Name
3. Ticket Number (Unique)
4. Some unique hash/code/crypt unique to the ticket to increase safety (One that wont require the customer to remember anything, purely back-end)
5. A cool graphic of the Purdue Grand Prix logo, Purdue P, or a kart in the middle (customizable in the future)
6. If possible set a use-limit on the QR codes (I guess something in the back-end, an update to a boolean would suffice)

The next obvious question is how to provide the QR codes to the customers

1. We could make an entire web-app for ticketing and directly give access to the customers to download the ticket
2. An easier way could be emailing/texting/both the ticket to the customers after their registration has been complete
(That's all I could think of right now)


