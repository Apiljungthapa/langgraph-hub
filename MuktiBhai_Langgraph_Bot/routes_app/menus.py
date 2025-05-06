data={
    "/Menu": {
        "title": "Hello world",
        "Greeting": "Namaste!",
        "Header": "I am your Virtual Assistant.  How may I help you?",
        "subHeader": "Please do not share any confidential information such as Account Details, Password, Pin and OTP etc...",
        "type": "hamburger",
        "mascot": "images/menu/mascot.png",
        "data": [
            {
                "title": "Banking Services",
                "payload": "/banking_services",
                "icon": "images/icons/problem.png",
            },
            {
                "title": "Digital Services",
                "payload": "/digital_services",
                "icon": "images/icons/digital-services.png",
            },
            {
                "title": "ATM/Branch",
                "payload": "/location",
                "icon": "images/icons/atmlocation.png",
            },
            {"title": "Forex", "payload": "/forex", "icon": "images/icons/forex.png"},
            {
                "title": "Working Hours",
                "payload": "/working_hours",
                "icon": "images/icons/workinghrs.png"
            },
            {
                "title": "Contact Us",
                "payload": "/contact",
                "icon": "images/icons/support.png"
            },
            {
                "title": "Feedback",
                "payload": "/feedback",
                "icon": "images/icons/feedback.png"
            },
            {
                "title": "Complaint",
                "payload": "/complaint",
                "icon": "images/icons/complaint.png"
            }
        ]
    },

  "/banking_services": {
    "type": "quick_reply",
    "title": "What type of Banking Queries do you have? Please select options below:",
    "subtitle": "What do you have query about ?",
    "data": [
      {
        "title": "Loan Account",
        "payload": "/loan"
      },
      {
        "title": "Saving Account",
        "payload": "/saving_account"
      },
      {
        "title": "Fixed Deposit",
        "payload": "/fixed_deposit"
      },
      
    ]
  },

  "/digital_services": {
    "type": "quick_reply",
    "title": "What do you want to know about digital services? Please choose below:",
    "data": [
      {
        "title": "Mobile Banking Services",
        "payload": "/mobile_banking"
      },
      {
        "title": "Internet Banking Services",
        "payload": "/e_banking"
      },
      {
        "title": "Smart App",
        "payload": "/smart_app"
      },
      {
        "title": "ATM Card",
        "payload": "/atm_card"
      },
      {
        "title": "E-Commerce Activation Application",
        "payload": "/ecommerce"
      },
      {
        "title": "Mobile Banking Registration Application",
        "payload": "/mbanking"
      },
      {
        "title": "New Debit Card Request",
        "payload": "/debitcard"
      },
      {
        "title": "QR Registration Application",
        "payload": "/qr"
      }
    ]
  },
  
  "/smart_app": {
    "type": "procedure_accordiance",
    "title": "There are some steps to open 'MNBBL SMART APP' ",
    "subtitle": "Follow these steps:",
    "accordian": False,
    "datalist": [
      {
        "title": "1. Please download our MNBBL SMART from PLAYSTORE for Android users and APPSTORE for Apple users."
      },
      {
        "title": "2. After that click on ' Unable to login, Tap here!' then click on ' Not Activate Yet' after that click on 'Activate Service', then"
      }
    ],
    "droplist": [
      {
        "title": "3. Please enter your Registered mobile number and Account number",
        "text": "accordiance paragraph"
      },
      {
        "title": "4. After that please enter the password and transaction pin which is remembered always. Note: Please do not share your transaction pin and password with others!",
        "text": "accordiance paragraphm2"
      },
      {
        "title": "4. After successfully registration, you can log in by entering your mobile number and password and, if you are still having a problem then please contact to our nearest branch.",
        "text": "accordiance paragraphm2"
      }
    ],
    "button": {
      "title": "Download app",
      "link": "https://play.google.com/store/apps/details?id=com.f1soft.muktinathmobilebanking&hl=en&gl=US"
    }
  },
  "/mobile_banking": {
    "type": "contextinner",
    "title": "Deposit Queries",
    "clickIconPrev": { "payload": "Banking Queries" },
    "subtitle": "What types of mobile banking queries do you have?",
    "data": [
      {
        "title": "Mobile Banking Registration",
        "payload": "How can i sign up for mobile banking"
      },
      {
        "title": "What are the documents required for registration of new mobile banking?",
        "payload": "What are the documents required for mobile banking?"
      },
      {
        "title": "How can I open my new MNBBL smart app after registration?",
        "payload": "/smart_app"
      },
      {
        "title": "What is the charge for password reset?",
        "payload": "What is the charge for password reset?"
      },
      {
        "title": "How can I reset my password?",
        "payload": "How can I reset my password?"
      },
      {
        "title": "Do I need any document for password reset?",
        "payload": "Do I need any document for password reset?"
      },
      {
        "title": "How much does it cost for renew mobile banking?",
        "payload": "How much does it cost for renew mobile banking?"
      },
      {
        "title": "What I have to do to renew my Mobile banking?",
        "payload": "What I have to do to renew my Mobile banking?"
      },
      {
        "title": "How can I link to wallet?",
        "payload": "How can I link to wallet?"
      },
      {
        "title": "What are the charges to link in the wallet?",
        "payload": "What are the charges to link in the wallet?"
      },
      {
        "title": "Is there mobile banking transaction limit",
        "payload": "mobile banking transaction limit"
      },
      {
        "title": "How many transaction can I perform in a day?",
        "payload": "How many transaction can I perform in a day?"
      },
      {
        "title": "How I can find my recharge number?",
        "payload": "How I can find my recharge number in Muktinath Bikas Bank?"
      }
    ]
  },
  "/e_banking": {
    "type": "contextinner",
    "title": "Deposit Queries",
    "clickIconPrev": { "payload": "Banking Queries" },
    "subtitle": "What types of Internet banking queries do you have?",
    "data": [
      {
        "title": "Internet Banking Registration",
        "payload": "How can i sign up for internet banking"
      },
      {
        "title": "What are the documents required for registration of new internet banking?",
        "payload": "What are the documents required for internet banking?"
      },
      {
        "title": "What is the charge of registration for Internet Banking?",
        "payload": "What is the charge of Internet Banking?"
      },
      {
        "title": "How can I open my new e-banking after registration?",
        "payload": "How can I open my new e-banking after registration?"
      },
      {
        "title": "How can I reset my password?",
        "payload": "How can I reset my password?"
      },
      {
        "title": "Do I need any document for password reset?",
        "payload": "Do I need any document for password reset?"
      },
      {
        "title": "How much does it cost for renew internet banking?",
        "payload": "How much does it cost for renew internet banking?"
      },
      {
        "title": "What do I have to do to renew my internet banking?",
        "payload": "What do I have to do to renew my internet banking?"
      },
      {
        "title": "How can I link to wallet?",
        "payload": "How can I link to wallet?"
      },
      {
        "title": "What are the charges to link in the wallet?",
        "payload": "What are the charges to link in the wallet?"
      },
      {
        "title": "Is there mobile banking transaction limit",
        "payload": "mobile banking transaction limit"
      },
      {
        "title": "How many transaction can I perform in a day?",
        "payload": "How many transaction can I perform in a day?"
      },
      {
        "title": "How I can find my recharge number?",
        "payload": "How I can find my recharge number?"
      }
    ]
  },
  "/atm_card": {
    "type": "quick_reply",
    "title": "What do you want to know about ATM card? Please choose below:",
    "data": [
      {
        "title": "Transaction Limit",
        "payload": "/atmlimit"
      },
      {
        "title": "ATM Charge",
        "payload": "/atmcharge"
      },
      {
        "title": "Block/Unblock/Close",
        "payload": "/atmblock"
      }
    ]
  },
  "/atmcharge": {
    "type": "quick_reply",
    "title": "ATM cash withdrawal from MNBBL ATMs is free. However, for withdrawals from other ATMs, a charge of NPR 15 applies for transactions exceeding 5 in a month. In India, the charge is NPR 250 per transaction.",
    "data": []
  },
  "/atmblock": {
    "type": "form",
    "subtype": "Received",
    "action": "/rest/v1/problem/",
    "formCategory": { "type": "Digital Services", "action": "Email_Postform" },
    "title": " Card Block/Unblock Request",
    "data": [
      {
        "label": "Full name",
        "placeholder": "Enter full name",
        "id": "fullName",
        "type": "text",
        "validation": { "required": True, "name": True }
      },
      {
        "label": "Email Address",
        "placeholder": "Enter email address",
        "id": "emailAddress",
        "type": "email",
        "validation": { "required": True, "email": True }
      },
      {
        "label": "Mobile Number",
        "placeholder": "Enter mobile number",
        "id": "mobileNumber",
        "type": "number",
        "validation": { "required": True, "mobile": True }
      },
      {
        "label": "Account Number",
        "placeholder": "Enter Account number",
        "id": "accountnumber",
        "type": "number",
        "validation": { "required": True, "account": True }
      },
      {
        "label": "ATM Number",
        "placeholder": "Enter ATM number",
        "id": "atmnumber",
        "type": "number",
        "validation": { "required": True, "account": True }
      },
      {
        "type": "dropdown",
        "placeholder": "Choose your request..",
        "label": "Request",
        "id": "droper",
        "validation": { "required": False },
        "data": [{ "for": "Block" }, { "for": "Unblock" }]
      }
    ],
    "buttons": {
      "data": [
        { "text": "Cancel", "type": "cancel" },
        { "text": "Submit", "type": "submit" }
      ]
    }
  },
  "/atmlimit": {
    "type": "table",
    "data": [
      {
        "<b>ATM & POS Limit</b>": "Per Transaction Limit (ATM)<hr>Daily Transaction Limit (ATM)<hr>Monthly Transaction Limit (ATM)<hr>Per Transaction Limit (POS)<hr>Daily Transaction Limit (POS)<hr>Monthly Transaction Limit (POS)",
        "<b>Within Nepal</b>": "NPR 25,000<hr>NPR 100,000<hr>NPR 400,000<hr>NPR 50,000<hr>NPR 300,000<hr>NPR 600,000",
        "<b>In India</b>": "INR 10,000<hr>INR 10,000<hr>INR 100,000<hr>NPR 50,000<hr>NPR 100,000<hr>NPR 160,000"
      }
    ]
  },
  # "/demat_crn": {
  #   "type": "quick_reply",
  #   "title": "Dear Customer, you can open 'Demat Account' online for free. To open demat account, please click the button below.",
  #   "data": [
  #     {
  #       "title": "Demant Online",
  #       "link": "https://demat.muktinathcapital.com/Demataccount"
  #     }
  #   ]
  # },
  "/fixed_deposit": {
    "type": "contextinner",
    "title": "Deposit Queries",
    "clickIconPrev": { "payload": "Banking Queries" },
    "subtitle": "What types of queries do you have?",
    "data": [
      {
        "title": "What types of deposits are available ?",
        "payload": "What types of deposits are available?"
      },
      { "title": "How do I open an FD ?", "payload": "How do I open an FD?" },
      {
        "title": "Can I apply for FD online ?",
        "payload": "Can I apply for FD online?"
      },
      {
        "title": "What are various deposit time slots available ?",
        "payload": "What are various deposit time slots available?"
      },
      {
        "title": "Which deposit has the highest interest rate ?",
        "payload": "Which deposit has the highest interest rate?"
      },
      {
        "title": "Can I get a loan against a fixed deposit?",
        "payload": "Can I get a loan against a fixed deposit?"
      }
    ]
  },
  "/saving_account": {
    "type": "contextinner",
    "title": "Account Queries",
    "clickIconPrev": { "payload": "Banking Queries" },
    "subtitle": "What type of query do you have?",
    "data": [
      {
        "title": "Type of saving accounts",
        "payload": "/saving_products"
      },
      {
        "title": "Type of  Premium saving accounts",
        "payload": "Types of  premium saving accounts"
      },
      {
        "title": "Can I open my account ?",
        "payload": "Can I open my account ?"
      },
      {
        "title": "Can I open my account online ?",
        "payload": "Can I open my account online ?"
      },
      {
        "title": "Which saving account offers the highest interest rate ?",
        "payload": "Which saving account offers the highest interest rate ?"
      },
      {
        "title": "Is there any maximum and minimum balance requirement ?",
        "payload": "Is there any maximum and minimum balance requirement ?"
      },
      {
        "title": "What is the procedure to add/modify/remove a nominee ?",
        "payload": "What is the procedure to add/modify/remove a nominee ?"
      },
      {
        "title": "Can a foreign national open account ?",
        "payload": "Can a foreign national open account ?"
      },
      {
        "title": "How often interest is credited to my account ?",
        "payload": "How often interest is credited to my account ?"
      },
      {
        "title": "How can I check my balance when I am at home ?",
        "payload": "How can i check my balance when am at home ?"
      },
      {
        "title": "I want to close my account.",
        "payload": "/complaint_feedback{\"complaint_type\":\"complaint\"}"
      },
      {
        "title": "I want to change scheme of the account.",
        "payload": "change scheme of the account "
      }
    ]
  },
  "/loan": {
    "type": "quick_reply",
    "title": "What do you want to know about Loans? Please choose below:",
    "subtitle": "What do you want to know about loan?",
    "data": [
      {
        "title": "Interest/Base Rate",
        "link": "https://muktinathbank.com.np/interest-rates"
      },
      { "title": "Loan Products", "payload": "/loan_products" },
      { "title": "Loan Online", "payload": "/loan_online" }
    ]
  },
  "/loan_products": {
    "type": "detailDrawer",
    "title": "We have various kinds of loan products available, which one are you seeking?",
    "data": [
      {
        "title": "Housing Loan",
        "subtitle": "Do you want to take a housing loan…!!! If you are willing to take a housing loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a housing loan at a correct interest rate.",
        "img": "images/Mukti/home-loan.jpg",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Housing Loan",
                "subtitle": "Housing loan",
                "paragraph": "Do you want to take a housing loan…!!! If you are willing to take a housing loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a housing loan at a correct interest rate.",
                "subtitle1": [
                  {
                    "title": "Interest Rate: ",
                    "listitem": [{ "text": "Base Rate (7.59%) + Premium up to 4.00%" }]
                  },
                  {
                    "title": "Documents Required for Housing Loan",
                    "listitem": [
                      { "text": "Passport size photographs of Applicant" },
                      { "text": "Applicant's Citizenship certificate" },
                      { "text": "Certified income source" },
                      {
                        "text": "Photographs and Citizenship certificate of Guarantors"
                      },
                      {
                        "text": "Purchase agreement/deed ( In case of purchase of land/building)"
                      },
                      {
                        "text": "Land ownership certificate (Lal Purja) with ownership type"
                      },
                      { "text": "Blue Print" },
                      { "text": "Malpot Receipt" },
                      { "text": "Four Boundary Certified(Char Killa)" },
                      { "text": "House Construction Approval (Map)" },
                      {
                        "text": "Building Construction Permission Letter from competent authority (If applicable)"
                      }
                    ]
                  },
                  {
                    "title": "How to apply for Housing Loan?",
                    "subtitle": "Application form for Housing Loan, Click button below. You can download the form online and can print it. Fill out all the details with the required attachments and submit it to your nearest branch. You can collect the application form from the nearest branch and hand it out personally."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/loan-application"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "Personal Loan",
        "subtitle": "Do you want to take a personal loan…!!! If you are willing to take a personal loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a personal loan at a correct interest rate.",
        "img": "images/Mukti/personalloan1.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Personal Loan",
                "subtitle": "Personal loan",
                "paragraph": "Do you want to take a personal loan…!!! If you are willing to take a personal loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a housing loan at a correct interest rate.",
                "subtitle1": [
                  {
                    "title": "Interest Rate:",
                    "listitem": [{ "text": "Base Rate (7.59%) + Premium up to 4.00%" }]
                  },
                  {
                    "title": "Documents Required for Personal Loan",
                    "listitem": [
                      { "text": "Passport size photographs of Applicant" },
                      { "text": "Applicant’s Citizenship certificate" },
                      {
                        "text": "Photographs and Citizenship certificate of Guarantors"
                      },
                      {
                        "text": "Land ownership certificate (Lal Purja) with ownership type"
                      },
                      { "text": "Certified income source" },
                      { "text": "Blue Print" },
                      { "text": "Malpot Receipt" },
                      { "text": "Four Boundary Certified(Char Killa)" },
                      {
                        "text": "House Construction Approval(Map) or Completion certificate ( In Case of Building) from relevant office."
                      }
                    ]
                  },
                  {
                    "title": "How to apply for Personal Loan?",
                    "subtitle": "Application form for Personal loan, Click the button below. You can download the form online and can print it. Fill out all the details with the required attachments and submit it to your nearest branch.You can collect the application form from the nearest branch and hand it out personally. Visit the nearest branch for assistance and clarity."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/loan-application"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "Share Loan",
        "subtitle": "Do you want to take a Share loan…!!! If you are willing to take a Share loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Share loan at a correct interest rate.",
        "img": "images/Mukti/shareloan1.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Share Loan",
                "subtitle": " Share Loan",
                "paragraph": "Do you want to take Share loan…!!! If you are willing to take Share loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Share loan at a correct interest rate.",
                "subtitle1": [
                  {
                    "title": "Interest Rate:",
                    "listitem": [
                      {
                        "text": "Base Rate (7.59%) + Premium up to 4.00% per annum"
                      },
                      {
                        "text": "The interest rate will be as prescribed by the bank from time to time."
                      },
                      {
                        "text": "48 hours processing time for Loan after submission of all documents.."
                      }
                    ]
                  },
                  {
                    "title": "Documents Required for Share Loan",
                    "listitem": [
                      { "text": "Copy of Citizenship Certificate" },
                      { "text": "Complete Loan Application Form" },
                      { "text": "Complete Know Your Customer(KYC) form" },
                      {
                        "text": "Recently Taken passport size photo of the debtor and the householder"
                      },
                      {
                        "text": "Map of the residence of the debtor and the householder"
                      },
                      {
                        "text": "Article of Association and Memorandum of Association (In case of Company)"
                      },
                      {
                        "text": "Copy of citizenship of the debtor and the householder"
                      },
                      { "text": "Gross share certificate" },
                      { "text": "DMAT statement" },
                      { "text": "PAN Card" }
                    ]
                  },
                  {
                    "title": "How to apply for Share Loan?",
                    "subtitle": "Application form for Share Loan, Click button below. You can download form online and can print it. Fill out all the details with the required attachments and submit it to your nearest branch. You can collect the application form from the nearest branch and hand it out personally. Visit the nearest branch for assistance and clarity."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/loan-application"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "BUSINESS/ INDUSTRIAL LOAN",
        "subtitle": "Do you want to take a Business/Industrial loan…!!! If you are willing to take a Business/Industrial loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Business/Industrial loan at a correct interest rate.",
        "img": "images/Mukti/business-loan.jpg",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Business/Industrial Loan",
                "subtitle": " Business/Industrial Loan",
                "paragraph": "Do you want to take a Business/Industrial loan…!!! If you are willing to take a Business/Industrial loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Business/Industrial loan at a correct interest rate",
                "subtitle1": [
                  {
                    "title": "Interest Rate:",
                    "listitem": [
                      {
                        "text": "Base Rate (7.59%) + Premium up to 4.00% per annum"
                      }
                    ]
                  },
                  {
                    "title": "Documents Required for Business/Industrial Loan",
                    "listitem": [
                      { "text": "Passport size photographs of Applicant" },
                      { "text": "Applicant's Citizenship certificate" },
                      {
                        "text": "Photographs and Citizenship certificate of Guarantors"
                      },
                      { "text": "Firm registration certificate" },
                      { "text": "PAN registration certificate(If any)" },
                      {
                        "text": "Article of Association and Memorandum of Association (In case of Company)"
                      },
                      {
                        "text": "Balance sheet, Cash flow, P&L a/c, Stock (Audited report  and projected report of 3 yrs)"
                      },
                      { "text": "Minute of BOD (In case of Company)" },
                      {
                        "text": "In-case of New company/Firm  Feasibility Report"
                      },
                      {
                        "text": "Land ownership certificate (Lal Purja) with ownership type"
                      },
                      { "text": "Blue Print" },
                      { "text": "Malpot Receipt (Tiro Tireko Rasid)" },
                      { "text": "Four Boundary Certified(Char Killa)" },
                      {
                        "text": "House Construction Approval (Map) or Completion certificate ( In Case of Building) from relevant Municipality/VDC office)"
                      }
                    ]
                  },
                  {
                    "title": "How to apply for Business/Industrial Loan",
                    "subtitle": "Application form for Business/Industrial Loan, Click button below. You can download the form online and can print it. Fill out all the details with the required attachments and submit it to your nearest branch. You can collect the application form from the nearest branch and hand it out personally. Visit the nearest branch for assistance and clarity."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/loan-application"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "Agriculture Loan",
        "subtitle": "Do you want to take an Agri loan…!!! If you are willing to take an Agri loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers an Agri loan at a correct interest rate.",
        "img": "images/Mukti/muktinath-agriculture.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Agriculture Loan",
                "subtitle": "Agriculture Loan",
                "paragraph": "Do you want to take an Agri Loan…!!! If you are willing to take an Agri loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers an Agri Loan in correct interest rate.",
                "subtitle1": [
                  {
                    "title": "Interest Rate:",
                    "listitem": [{ "text": "Base Rate (7.59%) + Premium up to 2.00% per annum" }]
                  },
                  {
                    "title": "Documents Required for Agriculture Loan",
                    "listitem": [
                      { "text": "Passport size photographs of Applicant" },
                      { "text": "Applicant’s Citizenship certificate" },
                      {
                        "text": "Photographs and Citizenship certificate of Guarantors"
                      },
                      { "text": "Firm registration certificate" },
                      { "text": "PAN registration certificate(If any)" },
                      {
                        "text": "Article of association and memorandum of association (In case of Company)"
                      },
                      {
                        "text": "Balance sheet, Cash flow, P&L a/c, Stock (Audited report Min. 3 yrs)"
                      },
                      { "text": "Minute of BOD (If company)" },
                      {
                        "text": "Land ownership certificate (Lal Purja) with ownership type"
                      },
                      { "text": "Blue Print" },
                      { "text": "Malpot Receipt" },
                      { "text": "Four Boundary Certified(Char Killa)" }
                    ]
                  },
                  {
                    "title": "How to apply for Agriculture Loan?",
                    "subtitle": "Application form for opening Account, Click button below. You can download form online and can print it. Fill out all the details with the required attachments and submit it to your nearest branch. You can collect the application form from the nearest branch and hand it out personally. Visit the nearest branch for assistance and clarity."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/loan-application"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "Real Estate Loan",
        "subtitle": "Do you want to take a Real Estate loan…!!! If you are willing to take a Real Estate loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Real Estate loan at a correct interest rate.",
        "img": "images/Mukti/realestateloan1.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Real Estate Loan",
                "subtitle": "Real Estate Loan",
                "paragraph": "Do you want to take a Real Estate Loan…!!! If you are willing to take a Real Estate loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Real Estate loan in correct interest rate.",
                "subtitle1": [
                  {
                    "title": "Interest Rate:",
                    "listitem": [{ "text": "Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "Documents Required for Real Estate Loan",
                    "listitem": [
                      { "text": "Passport size photographs of Applicant" },
                      { "text": "Applicant’s Citizenship certificate" },
                      {
                        "text": "Photographs and Citizenship certificate of Guarantors"
                      },
                      { "text": "Firm registration certificate" },
                      { "text": "PAN registration certificate(If any)" },
                      {
                        "text": "Article of association and memorandum of association (In case of Company)"
                      },
                      {
                        "text": "Balance sheet, Cash flow, P&L a/c, Stock (Audited report Min. 3 yrs)"
                      },
                      { "text": "Minute of BOD (For Company)" },
                      { "text": "Business Planning & Proposal (For New Firm)" },
                      {
                        "text": "Land ownership certificate (Lal Purja) with ownership type"
                      },
                      { "text": "Malpot Receipt" },
                      { "text": "Four Boundary Certified(Char Killa)" },
                      {
                        "text": "House Construction Approval (Map) or Completion certificate (In-Case of Building) from the relevant Municipality/VDC Office."
                      }
                    ]
                  },
                  {
                    "title": "How to apply for Real Estate loan?",
                    "subtitle": "Application form for Real Estate loan, Click button below. You can download form online and can print it. Fill out all the details with the required attachments and submit it to your nearest branch. You can collect the application form from the nearest branch and hand it out personally. Visit the nearest branch for assistance and clarity."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/loan-application"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      
      {
        "title": "Auto Loan",
        "subtitle": "Do you want to take an Auto Loan…!!! If you are willing to take an Auto Loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers an Auto Loan at a correct interest rate.",
        "img": "images/Mukti/autoLoan.jpg",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Auto Loan",
                "subtitle": "Auto Loan",
                "paragraph": "Do you want to take Auto Loan…!!! If you are willing to take Auto Loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers an Auto Loan in correct interest rate.",
                "subtitle1": [
                  {
                    "title": "Features and Benefits of Auto Loan with MBB",
                    "listitem": [{ "text": "Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "Documents Required for Auto Loan",
                    "listitem": [
                      { "text": "Passport size photographs of Applicant" },
                      { "text": "Applicant’s Citizenship certificate" },
                      { "text": "Certified income source" },
                      {
                        "text": "Photographs and Citizenship certificate of Guarantors"
                      },
                      { "text": "Quotation of vehicle from authorized dealer" },
                      {
                        "text": "Updated Blue Book in case of second-hand vehicle"
                      },
                      { "text": "Other supporting documents on demand" }
                    ]
                  },
                  {
                    "title": "Fee Charges",
                    "listitem": [
                      { "text": "Administrative Charge – 1 %" },
                      {
                        "text": "CIC Charge – Rs. 282.50 per inquiry (For No Transaction Report) Rs. 621.50 per inquiry (For Transaction Report)"
                      },
                      { "text": " Rs. 621.50 per inquiry (For Transaction Report)" }
                    ]
                  },
                  {
                    "title": "How to apply for Auto Loan?",
                    "subtitle": "Application form for Auto Loan, Click the button below. You can download the form online and can print it. Fill out all the details with the required attachments and submit them to your nearest branch. You can collect the application form from the nearest branch and hand it out personally."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/loan-application"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "Hire Purchase Loan",
        "subtitle": "Do you want to take a Hire purchase Loan…!!! If you are willing to take a Hire purchase loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Hire purchase Loan at a correct interest rate.",
        "img": "images/Mukti/auto-loan-2.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Hire purchase loan",
                "subtitle": "Hire purchase loan",
                "paragraph": "Do you want to take a Hire purchase Loan…!!! If you are willing to take a Hire purchase loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Hire purchase Loan in correct interest rate.",
                "subtitle1": [
                  {
                    "title": "Interest Rate:",
                    "listitem": [{ "text": "Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "Documents Required for Hire Purchase Loan",
                    "listitem": [
                      { "text": "Passport size photographs of Applicant" },
                      { "text": "Applicant’s Citizenship certificate" },
                      {
                        "text": "Photographs and Citizenship certificate of Guarantors"
                      },
                      { "text": "Quotation from authorized dealer." },
                      {
                        "text": "Copy of blue book, route permit, Vehicle fitness certificate, etc. (where applicable)"
                      },
                      {
                        "text": "Additional Collateral can be used as per the need."
                      }
                    ]
                  },
                  {
                    "title": "How to apply for Hire Purchase Loan?",
                    "subtitle": "Application form for Hire Purchase Loan, Click button below. You can download form online and can print it. Fill out all the details with the required attachments and submit it to your nearest branch. You can collect the application form from the nearest branch and hand it out personally. Visit the nearest branch for assistance and clarity."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/loan-application"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "More Loans",
        "subtitle": "Do you want to know about more Loans…!!! If you are willing to take a loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Loan at a correct interest rate.",
        "img": "images/Mukti/otherloans.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About More loans",
                "subtitle": "More loan Details",
                "paragraph": "Do you want to know about more Loans…!!! If you are willing to take a loan, take it from Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Loan at a correct interest rate.",
                "subtitle1": [
                  {
                    "title": "Mortgage Loan",
                    "listitem": [{ "text": "Interest rate of Mortgage Loan: Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "Professional Loan",
                    "listitem": [{ "text": "Interest rate of Professional Loan: Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "Muktinath Sulav Byawasaya Loan",
                    "listitem": [{ "text": "Interest rate of Muktinath Sulav Byawasaya Loan: Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "Consumer Loan",
                    "listitem": [{ "text": "Interest rate of Consumer Loan: Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "Gold Loan",
                    "listitem": [{ "text": "Interest rate of Gold Loan: Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "Other Loan",
                    "listitem": [{ "text": "Interest rate of Other Loan: Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "All Small & Micro Credit Products",
                    "listitem": [{ "text": "Interest rate of All Small & Micro Credit Products: Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "Wholesale Loan to MFIs",
                    "listitem": [{ "text": "Interest rate of Wholesale Loan to MFIs: Base Rate (7.59%) + Premium up to 2.00% per annum" }]
                  },
                  {
                    "title": "Wholesale Loan Others",
                    "listitem": [{ "text": "Interest rate of Wholesale Loan Others: Base Rate (7.59%) + Premium up to 4.00% per annum" }]
                  },
                  {
                    "title": "Loan Against Fixed Deposit (upto 90.00%)",
                    "listitem": [{ "text": "Interest rate of Loan Against Fixed Deposit (upto 90.00%): Coupon Rate Plus 2.00% or Base Rate (7.59%) whichever is higher" }]
                  },

                  
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/loan-application"
                    }
                  ]
                }
              }
            }
          ]
        }
      }
    ]
  },
  "/loan_online": {
    "type": "general_reply_with_reletedqueries",
    "title": [
      "Dear customer, you can apply for loans easily through online by clicking the link below:"
    ],
    "link": [
      {
        "title": "Apply Loan",
        "link": "https://www.muktinathbank.com.np/online/loan-application"
      }
    ],
    "reletedqueries": {
      "title": "Related Question...",
      "queries": [
        {
          "title": "How long will it take to get a loan through online?",
          "payload": "How long will it take to get a loan through online?"
        }
      ]
    }
  },
  "/saving_products": {
    "type": "detailDrawer",
    "title": "We have a variety of saving products to suit your various needs. Which one would you like to know more?",
    "data": [
      {
  "title": "Muktinath Sarvotkrishta Bachat Khata",
  "subtitle": "Home General Banking Deposit Premium Savings Muktinath Sarvotkrishta Bachat Khata",
  "img": "images/Mukti/mnbblsarvotkristha.jpg",
  "button": {
    "contents": [
      {
        "title": "View Details",
        "id": "btn1",
        "Details": {
          "title": "Details About Muktinath Sarvotkrishta Bachat Khata",
          "subtitle": "Muktinath Sarvotkrishta Bachat Khata",
          "paragraph": "Muktinath Sarvotkrishta Bachat Khata offers ample banking solutions for saving. Saving must become a priority, not just a thought. Pay yourself first.",
          "subtitle1": [
            {
              "title": "Features of Muktinath Sarvotkrishta Bachat Khata",
              "listitem": [
                { "text": "Minimum balance: Rs. 10,000.00" },
                { "text": "Any branch banking service" },
                { "text": "Free cheque book" }
              ]
            },
            {
              "title": "Facilities of Muktinath Sarvotkrishta Bachat Khata",
              "listitem": [
                { "text": "VISA Debit Card" },
                { "text": "Free Mobile banking for the first year only" },
                { "text": "Internet Banking" }
              ]
            },
            {
              "title": "Requirements for Muktinath Sarvotkrishta Bachat Khata",
              "listitem": [
                { "text": "Passport-sized photo" },
                { "text": "Copy of Citizenship Certificate" }
              ]
            },
            {
              "title": "Interest Rate and Payment Details",
              "listitem": [
                { "text": "Interest rate: 4.50% per annum" },
                { "text": "Payment: Monthly Basis" },
                { "text": "Minimum balance: Rs. 10,000" }
              ]
            }
          ],
          "button": {
            "contents": [
              {
                "title": "Application Form",
                "link": "https://www.muktinathbank.com.np/online/online/preliminary-form/muktinath-sarvotkrishta-bachat-khata"
              }
            ]
          }
        }
      }
    ]
  }
},
      
      {
        "title": "Muktinath Ashirwad Bachat Khata",
        "subtitle": "Money looks better in the bank than in your wallet…!!! If you are willing to save money, save it in Muktinath Bikash Bank Limited. Muktinath Bikash Bank Limited offers a Muktinath Ashirwad Bachat Khata that assures your money is securely saved for your future needs.",
        "img": "images/Mukti/muktinathashirwadbachatkhata.jpg",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Muktinath Ashirwad Bachat Khata",
                "subtitle": "Gold Saving Account",
                "paragraph": "Money looks better in the bank than in your wallet…!!! If you are willing to save money, save it in Muktinath Bikash Bank Limited. Muktinath Bikash Bank Limited offers a Muktinath Ashirwad Bachat Khata that ensures your savings grow safely.",
                "subtitle1": [
                  {
                    "title": "Features of Muktinath Ashirwad Bachat Khata",
                    "listitem": [
                      { "text": "Minimum Balance: NPR 50,000/-" },
                      { "text": "Interest Payment: Quarterly" },
                      { "text": "Any Branch Banking Service: Free" },
                      { "text": "Cheque Book: Free" }
                    ]
                  },
                  {
                    "title": "Facilities of Muktinath Ashirwad Bachat Khata",
                    "listitem": [
                      { "text": "Visa Debit Card Free for 1st Year" },
                      { "text": "Mobile Banking Free for 1st Year" },
                      { "text": "Internet Banking Free for 1st Year" },
                      { "text": "Locker Fee: No deposit charge required" }
                    ]
                  },
                  {
                    "title": "Interest Rate",
                    "subtitle": "Muktinath Ashirwad Bachat Khata (Gold): 5.00% (Quarterly Basis)"
                  },
                  {
                    "title": "Documents Required for Muktinath Ashirwad Bachat Khata",
                    "listitem": [
                      { "text": "Passport size photograph" },
                      { "text": "Citizenship/Passport" }
                    ]
                  }
                 
                ]
              }
            }
          ]
        }
      },
      {
        "title": "Muktinath Sajilo Bachat Khata",
        "subtitle": "Experience the ease of banking with Muktinath Sajilo Bachat Khata. Muktinath Bikash Bank Limited offers a flexible and accessible savings account that ensures your money grows without any minimum balance requirement.",
        "img": "images/Mukti/sajilobachatkhata.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Muktinath Sajilo Bachat Khata",
                "subtitle": "Muktinath Sajilo Bachat Khata",
                "paragraph": "Enjoy a hassle-free banking experience with Muktinath Sajilo Bachat Khata. With no minimum balance requirement, this account is designed to provide convenience and accessibility to meet your financial needs.",
                "subtitle1": [
                  {
                    "title": "Features of Muktinath Sajilo Bachat Khata",
                    "listitem": [
                      { "text": "Minimum Balance: Nil" },
                      { "text": "Interest Payment: Quarterly" },
                      { "text": "Any Branch Banking Service: Free" },
                      { "text": "Cheque Book Facility: Free" }
                    ]
                  },
                  {
                    "title": "Facilities of Muktinath Sajilo Bachat Khata",
                    "listitem": [
                      { "text": "Visa Debit Card" },
                      { "text": "Mobile Banking" },
                      { "text": "Internet Banking" },
                      { "text": "Free Demat Registration" }
                    ]
                  },
                  {
                    "title": "Interest Rate",
                    "subtitle": "Muktinath Sajilo Bachat Khata: 3.00% (Quarterly Basis)"
                  },
                  {
                    "title": "Documents Required for Muktinath Sajilo Bachat Khata",
                    "listitem": [
                      { "text": "Passport size photograph" },
                      { "text": "Copy of Citizenship Certificate" }
                    ]
                  },
                  {
                    "title": "How to Apply for Muktinath Sajilo Bachat Khata",
                    "subtitle": "Application form for opening an account. Click the button below to download the form online, print it, fill out all the details with the required attachments, and submit it to your nearest branch. Alternatively, you can collect the application form from the nearest branch and submit it personally."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/general-banking/deposit/saving/muktinath-sajilo-bachat-khata"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "Normal Saving Account",
        "subtitle": "Money looks better in bank than in your wallet…!!! If you are willing to save money, save it in Muktinath Bikash Bank Limited. Muktinath Bikash Bank limited offers a Normal saving account assures that your money is tucked away for your needy times.",
        "img": "images/Mukti/normal_saving_account.jpg",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Normal Saving",
                "subtitle": "Normal Saving",
                "paragraph": "Money looks better in bank than in your wallet…!!! If you are willing to save money, save it in Muktinath Bikas Bank. Muktinath Bikas Bank limited offers a Normal savings account assures that your money is tucked away for your needy times.",
                "subtitle1": [
                  {
                    "title": "Minimum Balance For Normal Saving",
                    "subtitle": "Only NPR.500 is required to open a normal saving"
                  },
                  {
                    "title": "Features And Benefits Of Normal Saving",
                    "listitem": [
                      { "text": "Interest Rate 3.00% per annum" },
                      { "text": "Interest Payment Quarterly basis" },
                      { "text": "Visa ATM" },
                      { "text": "Telecom" },
                      { "text": "Free bill payment system Nepal" },
                      { "text": "Get access to mobile banking" }
                    ]
                  },
                  {
                    "title": "Documents Required for Normal Saving",
                    "listitem": [
                      { "text": "Passport size photograph" },
                      { "text": "Citizenship/Passport" }
                    ]
                  },
                  {
                    "title": "How to apply for Normal Savings?",
                    "subtitle": "Application form for opening Account, Click button below. You can download the form online and can print it. Fill out all the details with the required attachments and submit it to your nearest branch. You can collect the application form from the nearest branch and hand it out personally."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/online/preliminary-form/normal-saving-account"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "Mahila Pewa Bachat khata",
        "subtitle": "This account is offered for women. All the female citizens are eligible to open the account and enjoy the multiple facilities as an account holder.",
        "img": "images/Mukti/Mahila Pewa Bachat Khata.jpg",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Mahila Pewa Bachat Khata",
                "subtitle": "Mahila pewa Bachat Khata",
                "paragraph": "This account is offered for women of age 16 and above. All the female citizens are eligible to open the account and enjoy the multiple facilities as an account holder.",
                "subtitle1": [
                  {
                    "title": "Minimum Balance For Mahila Pewa Bachat Khata",
                    "subtitle": "Minimum balance of Rs 500 is required for account opening."
                  },
                  {
                    "title": "Mahila Pewa Bachat Khata",
                    "listitem": [
                      { "text": "Interest Rate 3.00% per annum" },
                      { "text": "Interest Payment on Quarterly Basis" },
                      { "text": "Free VISA ATM" },
                      {
                        "text": "Free Mobile and Internet Banking"
                      }
                    ]
                  },
                  {
                    "title": "Documents Required For Mahila Pewa Bachat Khata",
                    "listitem": [
                      { "text": "Passport size photograph" },
                      { "text": "Citizenship Certificate" }
                    ]
                  },
                  {
                    "title": "How to apply for Mahila Pewa Bachat Khata?",
                    "subtitle": "Application form for opening Account, Click the button below. You can download the form online and can print it. Fill out all the details with the required attachments and submit it to your nearest branch. You can collect the application form from the nearest branch and hand it out personally. Visit the nearest branch for assistance and clarity."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/online/preliminary-form/mahila-pewa-bachat-khata"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "Sunaulo Bal Shichha Bachat",
        "subtitle": "This saving account is for childern of age 16 and below. The saving account will help you to save from today for the upcoming future of your children",
        "img": "images/Mukti/suanulo_bal_siksha.jpg",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Sunaulo Bal Bachat",
                "subtitle": " Sunaulo Bal Bachat",
                "paragraph": "The account is for children of age 16 and below. Sunaulo Bal Bachat account is for here for you if you want to put the future of your child in safe hands.",
                "subtitle1": [
                  {
                    "title": "Minimum Balance For Sunaulo Bal Bachat",
                    "subtitle": "No minimum balance required for Sunaulo Bal Bachat"
                  },
                  {
                    "title": "Documents Required For Sunaulo Bal Bachat",
                    "listitem": [
                      { "text": "Interest Rate 3.00% per annum" },
                      { "text": "Interest Payment on Quarterly basis" },
                      { "text": "Passport size photograph" },
                      {
                        "text": "Copy of citizenship card of guardian"
                      },
                      { "text": "Birth certificate of children" }
                    ]
                  },
                  {
                    "title": "How to apply for Sunaulo Bal Bachat?",
                    "subtitle": "Application form for opening Account, Click button below. You can download form online and can print it. Fill out all the details with the required attachments and submit it to your nearest branch. You can collect the application form from the nearest branch and hand it out personally. Visit the nearest branch for assistance and clarity."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/online/preliminary-form/sunaulo-bal-bachat-khata"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
        "title": "Sharedhani Bachat Khata",
        "subtitle": "Sharedhani Bachat khata offers ample banking solution for saving. Saving must become a priority, Not just a thought…Pay yourself first.",
        "img": "images/Mukti/sharedhanibachatkhata4.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Shredhani Bachat Khata",
                "subtitle": "Sharedhani Bachat khata",
                "paragraph": "Sharedhani Bachat khata ample banking solution for saving. Saving must become a priority, Not just a thought…Pay yourself first.",
                "subtitle1": [
                  {
                    "title": "Minimum Balance For Sharedhani Bachat Khata",
                    "subtitle": "The minimum balance of NPR. 100 is required."
                  },
                  {
                    "title": "Interest Rate",
                    "subtitle": "Interest Rate 4.00% per annum"
                  },
                  {
                    "title": "Interest Payment",
                    "subtitle": "Quarterly Basis"
                  }
                  
                ]
                
              }
            }
          ],
          
        },
        
      },
      {
        "title": "Karmachari Bachat",
        "subtitle": "Karmachari Bachat offers ample banking solution for saving. Saving must become a priority, Not just a thought…Pay yourself first.",
        "img": "images/Mukti/karmacharibachatkhata4.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Karmachari Bachat",
                "subtitle": "Karmachari Bachat",
                "paragraph": "Karmachari Bachat ample banking solution for saving. Saving must become a priority, Not just a thought…Pay yourself first.",
                "subtitle1": [
                  {
                    "title": "Features and Benefits of Karmachari Bachat  ",
                    "listitem": [
                      { "text": "Interest payment on Quarterly Basis" },
                      { "text": "Interest Rate 3.00% per annum" },
                      { "text": "Free cheque books." },
                      { "text": "Free Visa ATM" },
                      {
                        "text": "Free bill payment system of Nepal Telecom"
                      },
                      { "text": "Get access to mobile banking." }
                    ]
                  },
                  {
                    "title": "Documents Required for Karmachari Bachat ",
                    "listitem": [
                      { "text": "Passport size photograph" },
                      {
                        "text": " Copy of Citizenship Certificate"
                      }
                    ]
                  },
                  
                ]
              }
            }
          ]
        }
      },
      {
        "title": "MUKTINATH SAMBRIDDHI BACHAT KHATA",
        "subtitle": "Let's start prosperity from Muktinath Sambriddhi Bachat Khata. Muktinath Sambriddhi Bachat Khata offers ample banking solutions for saving. Saving must become a priority, Not just a thought…Pay yourself first.",
        "img": "images/Mukti/samriddhabachatkhata.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About Muktinath Sambriddhi Bachat Khata",
                "subtitle": "Muktinath Sambriddhi Bachat Khata",
                "paragraph": "Let's start prosperity from Muktinath Sambriddhi Bachat Khata. Muktinath Sambriddhi Bachat Khata offers ample banking solution for saving. Saving must become a priority, Not just a thought…Pay yourself first.",
                "subtitle1": [
                  {
                    "title": "Features and Benefits of Muktinath Sambriddhi Bachat Khata ",
                    "listitem": [
                      { "text": "Minimum balance: Rs. 100.00" },
                      {
                        "text": "Interest Rate 3.00% per annum (payment on Quarterly basis)"
                      },
                      { "text": "Any branch banking service" },
                      { "text": "Free cheque book" },
                      { "text": "VISA ATM" },
                      {
                        "text": "Free Mobile banking (first year)                        "
                      },
                      {
                        "text": "Free Internet Banking (first year)"
                      }
                    ]
                  },
                  {
                    "title": "Documents Required for Muktinath Sambriddhi Bachat Khata ",
                    "listitem": [
                      { "text": "Passport size photograph" },
                      { "text": "Copy of Citizenship Certificate" }
                    ]
                  },
                  {
                    "title": "How to apply for Muktinath Sambriddhi Bachat Khata",
                    "subtitle": "To apply online please click button below. or You can download the form online and can print it, than Fill out all the details with the required attachments and submit it to your nearest branch. You can collect the application form from the nearest branch and hand it out personally. Visit the nearest branch for assistance and clarity."
                  }
                ],
                "button": {
                  "contents": [
                    {
                      "title": "Application form",
                      "link": "https://www.muktinathbank.com.np/online/online/preliminary-form/muktinath-sambriddhi-bachat-khata"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      {
  "title": "Muktinath Samriddhi Remit IPO Bachat Khata",
  "subtitle": "Muktinath Samriddhi Remit IPO Bachat Khata for saving. Saving must become a priority, Not just a thought…Pay yourself first.",
  "img": "images/Mukti/muktinathsamriddhiremitipo.png",
  "button": {
    "contents": [
      {
        "title": "View Details",
        "id": "btn1",
        "Details": {
          "title": "Details About Muktinath Samriddhi Remit IPO Bachat Khata",
          "subtitle": "Muktinath Samriddhi Remit IPO Bachat Khata",
          "paragraph": "Muktinath Samriddhi Remit IPO Bachat Khata offers ample banking solutions for saving. Saving must become a priority, not just a thought. Pay yourself first.",
          "subtitle1": [
            {
              "title": "Features of Muktinath Samriddhi Remit IPO Bachat Khata",
              "listitem": [
                { "text": "Minimum Balance – Rs. 100" },
                { "text": "Interest Posing - Monthly" }
              ]
            },
            {
              "title": "Facilities of Muktinath Samriddhi Remit IPO Bachat Khata",
              "listitem": [
                { "text": "Free DEMAT (for first year)" },
                { "text": "Free CRN Registration" },
                { "text": "Free MERO SHARE Registration (for first year)" },
                { "text": "Free C-ASBA Charge" },
                { "text": "Free Internet Banking (for first year)" }
              ]
            },
            {
              "title": "Interest Rate and Payment Details",
              "listitem": [
                { "text": "Interest Rate: 6.00%" },
                { "text": "Payment: Monthly Basis" },
                { "text": "Minimum Balance: Rs. 100" }
              ]
            }
          ],
          "button": {
            "contents": [
              {
                "title": "Application Form",
                "link": "https://www.muktinathbank.com.np/online/online/preliminary-form/muktinath-sambriddhi-remit-ipo-bachat-khata"
              }
            ]
          }
        }
      }
    ]
  }
},
      {
        "title": "Other Account",
        "subtitle": "Other Account for saving. Saving must become a priority, Not just a thought…Pay yourself first.",
        "img": "images/Mukti/othersaving.png",
        "button": {
          "contents": [
            {
              "title": "View Details",
              "id": "btn1",
              "Details": {
                "title": "Details About More saving accounts",
                "subtitle": "Other Account",
                "paragraph": "Other Account for saving. Saving must become a priority, Not just a thought…Pay yourself first.",
                "subtitle1": [
                  {
                    "title": "Samajik Surakshya Bachat Khata ",
                    "listitem": [
                      { "text": "Interest Rate 3.00% per annum" },
                      { "text": "Minimum Balance – Rs. 0" },
                      { "text": "Interest Posing - Quarterly Basis" },
                      
                    ]
                  },
                  {
                    "title": "PMS Bachat Khata ",
                    "listitem": [
                      { "text": "Interest Rate 3.00% per annum" },
                      { "text": "Minimum Balance – Rs. 0" },
                      { "text": "Interest Posing - Quarterly Basis" },
                      
                    ]
                  },
                  {
                    "title": "FCY Deposit Account",
                    "listitem": [
                      { "text": "Interest Rate up to 1.50% per annum" },
                      { "text": "Minimum Balance – Rs. 10" },
                      { "text": "Interest Posing - Quarterly Basis" },
                      
                    ]
                  },
                  
                ]
              }
            }
          ]
        }
      }
      
      
    ]
  },
  "/contact": {
    "type": "contact",
    "title": "Dear customer, you can contact us at:",
    "data": {
      "subtitle": "Central Office (General Banking) Lazimpat, Kathmandu",
      "button": {
        "title": "Branch Detail",
        "payload": "/bank"
      },
      "info": [
        { "key": "Email", "value": "info@muktinathbank.com.np" },
        { "key": "Phone", "value": "+977-01-5970887" },
        { "key": "Toll-Free Number", "value": "16600149999" }
      ]
    }
  },
  "/location": {
    "title": "For ATM location, please click the ATM location button, and for branch location, click the branch location button below.",
    "type": "quick_reply",
    "data": [
      {
        "title": "ATM Location",
        "payload": "/atm"
      },
      {
        "title": "Branch Location",
        "payload": "/bank"
      }
    ]
  },
  "/atm": {
    "type": "location",
    "for": "atm",
    "title": "",
    "header": "ATM Location",
    "img": "images/address.png",
    "subtitle": "Please type the place or send your current location to find ATM nearby.",
    "button": {
      "contents": [
        { "title": "Get ATM Near Me", "type": "send_location" },
        { "title": "Type Location", "type": "type_location" }
      ]
    }
  },
  "/bank": {
    "type": "location",
    "title": "",
    "header": "Branch Location",
    "img": "images/address.png",
    "subtitle": "Please type the place or send your current location to find bank branch nearby.",
    "button": {
      "contents": [
        { "title": "Get Branches Near Me", "type": "send_location" },
        { "title": "Type Location", "type": "type_location" }
      ]
    }
  },
  
  "/working_hours": {
    "title": "Please select the office working hours according to the season.",
    "type": "quick_reply",
    "data": [
      {
        "title": "Summer Season (16th Magh - 15th Kartik)",
        "payload": "/summer"
      },
      {
        "title": "Winter Season (16th Kartik - 15th Magh)",
        "payload": "/winter"
      }
    ]
  },
  "/summer": {
    "type": "table",
    "data": [
      {
        "Details": "Sunday to Thursday",
        "Office Hours": "9:30 A.M to 5:30 P.M",
        "Transaction Hours": "10:00 A.M to 4:00 P.M"
      },
      {
        "Details": "Friday",
        "Office Hours": "9:30 A.M to 3:00 P.M",
        "Transaction Hours": "10:00 A.M to 2:00 P.M"
      }
    ]
  },
  "/winter": {
    "type": "table",
    "data": [
      {
        "Details": "Sunday to Thursday",
        "Office Hours": "9:30 A.M to 4:30 P.M",
        "Transaction Hours": "10:00 A.M to 3:00 P.M"
      },
      {
        "Details": "Friday",
        "Office Hours": "9:30 A.M to 3:00 P.M",
        "Transaction Hours": "10:00 A.M to 2:00 P.M"
      }
    ]
  },
  "/forex": {
    "type": "forex",
    "title": "Dear Customer, You may select from the following to know the exchange rate!",
    "date": "true",
    "header": "Forex",
    "img": "images/icons/forex.png",
    "subtitle": "Please select your appropriate currency below to get today's exchange rate!",
    "country": [
      { "name": "India", "currency": "INR" },
      { "name": "United States", "currency": "USD" },
      { "name": "Europe", "currency": "EUR" },
      { "name": "Australia", "currency": "ASD" }
    ],
    "button": {
      "contents": [{ "title": "Get exchange rate", "type": "exchange_rate" }]
    }
  },
  
"/complaint": {
    "type": "form",
    "subtype": "Regarding",
    "action": "/rest/v1/problem/",
    "successResponse":{"title":"Your complaint has been successfully submitted. If your issue is urgent, you may visit nearest branch around you by clicking on the button below.",
                        "type":"quick_reply",
                        "data":[{"title":"Nearest Branch", "payload":"/bank"}]},
    "formCategory": {"type": "Others", "action": "Email_Postform"},
    "title": "Customer Problems",
    "data": [
        {
            "label": "Full name",
            "placeholder": "Enter full name",
            "id": "fullName",
            "type": "text",
            "validation": {"required": True, "name": True},
        },
        {
            "label": "Email Address",
            "placeholder": "Enter email address",
            "id": "emailAddress",
            "type": "email",
            "validation": {"required": True, "email": True},
        },
        {
            "label": "Mobile Number",
            "placeholder": "Enter mobile number",
            "id": "mobileNumber",
            "type": "number",
            "validation": {"required": True, "mobile": True},
        },
        {
            "label": "Account Number",
            "placeholder": "Enter Account number",
            "id": "accountnumber",
            "type": "number",
            "validation": {"required": True, "accountnumber": True},
            "data": [
                {"for": "ATM Card/ Visa Card"},
                {"for": "Mobile/Internet Banking"},
                {"for": "Loan"},
                {"for": "Others"},
            ],
        },
        {
            "label": "Problem",
            "placeholder": "Please briefly explain your problem.",
            "id": "textarea",
            "type": "textarea",
            "validation": {"required": True, "textfield": True},
        },
    ],
    "buttons": {
        "data": [
            {"text": "Cancel", "type": "cancel"},
            {"text": "Submit", "type": "submit"},
        ]
    },
},
"/feedback": {
    "type": "form",
    "subtype": "Regarding",
    "action": "/rest/v1/problem/",
    "successResponse":{"title":"Your feedback has been successfully submitted. We thank you for your suggestions. You may visit nearest branch around you by clicking on the button below.",
                        "type":"quick_reply",
                        "data":[{"title":"Nearest Branch", "payload":"/bank"}]},
    "formCategory": {"type": "Feedback", "action": "Email_Postform"},
    "title": "Suggestions",
    "data": [
        {
            "label": "Full name",
            "placeholder": "Enter full name",
            "id": "fullName",
            "type": "text",
            "validation": {"required": True, "name": True},
        },
        {
            "label": "Email Address",
            "placeholder": "Enter email address",
            "id": "emailAddress",
            "type": "email",
            "validation": {"required": True, "email": True},
        },
        {
            "label": "Mobile Number",
            "placeholder": "Enter mobile number",
            "id": "mobileNumber",
            "type": "number",
            "validation": {"required": True, "mobile": True},
        },
        {
            "label": "Account Number",
            "placeholder": "Enter Account number",
            "id": "accountnumber",
            "type": "number",
            "validation": {"accountnumber": True},
        },
        {
            "label": "Suggestions",
            "placeholder": "Please briefly explain your suggestions.",
            "id": "textarea",
            "type": "textarea",
            "validation": {"required": True, "textfield": True},
        },
    ],
    "buttons": {
        "data": [
            {"text": "Cancel", "type": "cancel"},
            {"text": "Submit", "type": "submit"},
        ]
    },
},
"/application_process": {
    "type": "form",
    "subtype": "Regarding",
    "action": "/rest/v1/problem/",
    "successResponse":{"title":"Your application request have been successfully submitted. For more assistance, you may visit nearest branch around you by clicking on the button below.",
                        "type":"quick_reply",
                        "data":[{"title":"Nearest Branch", "payload":"/bank"}]},
    "formCategory": {
        "type": "Application Request",
        "action": "Email_Postform",
    },
    "title": "Appointment for Application",
    "data": [
        {
            "label": "Full Name",
            "placeholder": "Enter full name",
            "id": "fullName",
            "type": "text",
            "validation": {"required": True,"name":True},
        },
        {
            "label": "Email Address",
            "placeholder": "Enter email address",
            "id": "emailAddress",
            "type": "email",
            "validation": {"required": True, "email": True},
        },
        {
            "label": "Mobile Number",
            "placeholder": "Enter mobile number",
            "id": "mobileNumber",
            "type": "number",
            "validation": {"required": True, "mobile": True},
        },
        {
            "id": "category",
            "label": "category",
            "type": "dropdown",
            "placeholder": "Select your desired application request",
            "data": [
                {"for": "Loans"},
                {"for": "Account Opening"},
                {"for": "Remittance"},
                {"for": "DEMAT"},
                {"for": "Others"},
            ],
            "validation": {"required": True, "account": True},
        },
    ],
    "buttons": {
        "data": [
            {"text": "Cancel", "type": "cancel"},
            {"text": "Submit", "type": "submit"},
        ]
    },
},
"/ecommerce": {
    "type": "form",
    "subtype": "Regarding",
    "action": "/rest/v1/problem/",
    "successResponse":{"title":"Your e-commerce activation application request have been successfully submitted. For more assistance, you may visit nearest branch around you by clicking on the button below.",
                        "type":"quick_reply",
                        "data":[{"title":"Nearest Branch", "payload":"/bank"}]},
    "formCategory": {
        "type": "Digital Services Request",
        "action": "Email_Postform",
    },
    "title": "E-commerce activation application",
    "data": [
        {
            "label": "Full name",
            "placeholder": "Enter full name",
            "id": "fullName",
            "type": "text",
            "validation": {"required": True,"name":True},
        },
        {
            "label": "Email Address",
            "placeholder": "Enter email address",
            "id": "emailAddress",
            "type": "email",
            "validation": {"required": True, "email": True},
        },
        {
            "label": "Mobile Number",
            "placeholder": "Enter mobile number",
            "id": "mobileNumber",
            "type": "number",
            "validation": {"required": True, "mobile": True},
        },
        {
            "label": "Account Number",
            "placeholder": "Enter Account number",
            "id": "accountnumber",
            "type": "number",
            "validation": {"required": True, "account": True},
        },
        {
            "label": "Card Number",
            "placeholder": "Enter Card Number",
            "id": "cardnumber",
            "type": "number",
            "validation": {"required": True, "account": True},
        },
        {
            "label": "Branch Name",
            "placeholder": "Enter Branch Name",
            "id": "branchName",
            "type": "text",
            "validation": {"required": True},
        },
    ],
    "buttons": {
        "data": [
            {"text": "Cancel", "type": "cancel"},
            {"text": "Submit", "type": "submit"},
        ]
    },
},
"/qr": {
    "type": "form",
    "subtype": "Regarding",
    "action": "/rest/v1/problem/",
    "successResponse":{"title":"Your QR registration request have been successfully submitted. For more assistance, you may visit nearest branch around you by clicking on the button below.",
                        "type":"quick_reply",
                        "data":[{"title":"Nearest Branch", "payload":"/bank"}]},
    "formCategory": {
        "type": "Digital Services Request",
        "action": "Email_Postform",
    },
    "title": "QR Registration",
    "data": [
        {
            "label": "Full name",
            "placeholder": "Enter full name",
            "id": "fullName",
            "type": "text",
            "validation": {"required": True,"name":True},
        },
        {
            "label": "Name of business",
            "placeholder": "Enter Name Of Business",
            "id": "NameOfBusiness",
            "type": "text",
            "validation": {
                "required": True,
                "business":True
            },
        },
        {
            "label": "Mobile Number",
            "placeholder": "Enter mobile number",
            "id": "mobileNumber",
            "type": "number",
            "validation": {"required": True, "mobile": True},
        },
        {
            "label": "Email Address",
            "placeholder": "Enter email address",
            "id": "emailAddress",
            "type": "email",
            "validation": {"required": True, "email": True},
        },
        {
            "label": "Account Number",
            "placeholder": "Enter Account number",
            "id": "accountnumber",
            "type": "number",
            "validation": {"required": True, "account": True},
        },
        {
            "label": "PAN Number",
            "placeholder": "Enter PAN Number",
            "id": "PANNumber",
            "type": "number",
            "validation": {"required": True,"pan":True},
        },
        {
            "label": "Branch Name",
            "placeholder": "Enter Branch Name",
            "id": "branchName",
            "type": "text",
            "validation": {"required": True,"branch":True},
        },
    ],
    "buttons": {
        "data": [
            {"text": "Cancel", "type": "cancel"},
            {"text": "Submit", "type": "submit"},
        ]
    },
},
"/debitcard": {
    "type": "form",
    "subtype": "Regarding",
    "action": "/rest/v1/problem/",
    "successResponse":{"title":"Your new debit card request have been successfully submitted. For more assistance, you may visit nearest branch around you by clicking on the button below.",
                        "type":"quick_reply",
                        "data":[{"title":"Nearest Branch", "payload":"/bank"}]},
    "formCategory": {
        "type": "New Debit Card Request",
        "action": "Email_Postform",
    },
    "title": "New Debit Card Request",
    "data": [
        {
            "label": "Full name",
            "placeholder": "Enter full name",
            "id": "fullName",
            "type": "text",
            "validation": {"required": True,"name":True},
        },
        {
            "label": "Email Address",
            "placeholder": "Enter email address",
            "id": "emailAddress",
            "type": "email",
            "validation": {"required": True, "email": True},
        },
        {
            "label": "Card Take Branch",
            "placeholder": "Enter Branch Where You Have Got Card",
            "id": "CardTakeBranch",
            "type": "text",
            "validation": {
                "required": True,
                "card":True
            },
        },
        {
            "label": "Mobile Number",
            "placeholder": "Enter mobile number",
            "id": "mobileNumber",
            "type": "number",
            "validation": {"required": True, "mobile": True},
        },
        {
            "label": "Account Number",
            "placeholder": "Enter Account number",
            "id": "accountnumber",
            "type": "number",
            "validation": {"required": True, "account": True},
        },
        {
            "label": "Branch Name",
            "placeholder": "Enter Branch Name",
            "id": "branchName",
            "type": "text",
            "validation": {"required": True,"branch":True},
        },
    ],
    "buttons": {
        "data": [
            {"text": "Cancel", "type": "cancel"},
            {"text": "Submit", "type": "submit"},
        ]
    },
},
"/mbanking": {
    "type": "form",
    "subtype": "Regarding",
    "action": "/rest/v1/problem/",
    "successResponse":{"title":"Your mobile banking application have been successfully submitted. For more assistance, you may visit nearest branch around you by clicking on the button below.",
                        "type":"quick_reply",
                        "data":[{"title":"Nearest Branch", "payload":"/bank"}]},
    "formCategory": {
        "type": "Digital Services Request",
        "action": "Email_Postform",
    },
    "title": "Mobile banking Registration application",
    "data": [
        {
            "label": "Full name",
            "placeholder": "Enter full name",
            "id": "fullName",
            "type": "text",
            "validation": {"required": True,"name":True},
        },
        {
            "label": "Email Address",
            "placeholder": "Enter email address",
            "id": "emailAddress",
            "type": "email",
            "validation": {"required": True, "email": True},
        },
        {
            "label": "Mobile Number",
            "placeholder": "Enter mobile number",
            "id": "mobileNumber",
            "type": "number",
            "validation": {"required": True, "mobile": True},
        },
        {
            "label": "Account Number",
            "placeholder": "Enter Account number",
            "id": "accountnumber",
            "type": "number",
            "validation": {"required": True, "account": True},
        },
        {
            "label": "Branch Name",
            "placeholder": "Enter Branch Name",
            "id": "branchName",
            "type": "text",
            "validation": {"required": True,"branch":True},
        },
    ],
    "buttons": {
        "data": [
            {"text": "Cancel", "type": "cancel"},
            {"text": "Submit", "type": "submit"},
        ]
    },
}
}