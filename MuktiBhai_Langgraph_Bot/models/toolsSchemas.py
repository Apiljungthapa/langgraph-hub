from pydantic import BaseModel, Field

# appointment tool schema
class AppointmentInput(BaseModel):
    query: str = Field(description="A question regarding the appointment process, submitted by the user")
    
# bank details tool schema
class AboutUsInput(BaseModel):
    query: str = Field(description="""It is  queries about the bank’s details, leadership, departments, 
                                     contacts, committees, and banking info.""")
    
class DocumentsInput(BaseModel):
    query: str = Field(description="""A question regarding the required documents for bank accounts, loan applications, or transactions.
                                      This could include inquiries about specific account types, loan categories,
                                      or general banking requirements.""")
class chargesInput(BaseModel):
    query: str = Field(description="A question or inquiry related to the tariff of charges.")

class ContactInput(BaseModel):
    query: str = Field( description="""A question or inquiry related to the branches of the bank that may contain the contact details 
                    such as the bank's phone number, email, contact information, and address.""")

class InterestInput(BaseModel):
    query: str = Field(description="A string representing the user's query regarding financial products, such as interest rates, loan details, payment terms, or other banking service information. This query will be used to retrieve relevant details about financial products like saving deposits, loans, or fixed deposit terms.")


class GeneralInput(BaseModel):
    query: str = Field(description="A inquiry related to banking services, including cards, loans, digital banking savings accounts, common banking services.")