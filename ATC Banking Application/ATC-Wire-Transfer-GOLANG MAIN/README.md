# Wire Transfer

1. Wire Transactions can be issued via a Browser or terminal command-line interface

2. User will get a status whether the funds were transferred or insufficient funds to transfer

3. NO business logic in the transfer server.

4. No Database is needed. You can hard code the accounts in a file

5. Record successful and unsuccessful transactions to a file

6. You can add account holders [Name, Acct #, Opening Balance] 

# Technologies to Use

#### JSON – Data Interchange between services
#### YAML – Configuration files
#### Golang
#### Gorilla/Mux  or Gin
#### Swagger
#### Rest/HTTP
#### gRPC
#### Error handling
#### Git software Development cycle

# I. Start With The Bank Account

### - Data & Structures
### - CRUD
### - Configuration

## a). Data Structure & Data
##### Account Holder Information:

In memory Map of struct

In file JSON array/list
##### Account# TTTTTTTTT(9 Digits) AAAAAAAAAAA(11 Digits) –Type String

T -> Routing Number A -> Account Number

Account Number must be Unique

	National ID#  9 DiGITS Type String
	
	SWIFT: 10 Characters Alphanumeric
	
	Balance: FLoat64
	
	First Name
	
	Last Name
	
	Address1
	
	Address2
	
	Address3
	
	Country

## b). Bank Account Operations  Server side API (Procedures)

Create a Package called atcBankOps.

    handle, error := atcBankOps.OpenDatabase(“ “) (SIMPLE FILE)

    error := atcBankOps.UpdateBalance(handle,accountNumber,Float64)

    error := atcBankOps.DebitAccount(handle,accountNumber,Float64)

    error := atcBankOps.CreditAccount(handle,accountNumber,Float64)

    list,error := atcBankOps.ListAccounts(handle)
  
    error := atcBankOps.DeleteAccount(handle,accountNumber)

    error := atcBankOps.SyncDatabase(handle)

    error := atcBankOps.CloseDatabase(handle)

## c). Bank Account Operations  Rest API (Procedures) (Client)

Create a Package called atcBankRst.

    restHandle, error := atcBankRst.FindBankServer(“ “)

    error := atcBankRst.UpdateBalance(restHandle,accountNumber,Float64)

    error := atcBankRst.DebitAccount(restHandle,accountNumber,Float64)

    error := atcBankRst.CreditAccount(restHandle,accountNumber,Float64)

    list,error := atcBankRst.ListAccounts(restHandle) –list  JSON

    error := atcBankRst.DeleteAccount(restHandle,accountNumber)
    
    error := atcBankRst.SyncDatabase(restHandle)

## d). Bank Account Data

Bank information is stored as JSON in a file called atcBankAccounts.txt. 

Accounts are read into a MAP of account Structures

Key is Account Number

variable := make(map[<key type>]<value type>)

Account File is updated every 3 minutes (Save for Last to implement)

## e). Bank Account Operations

      type DBStruct struct {

         NumberOfAccounts int //Public
         
         LastAccessed time.Time //Public
          
         accounts map[string]AccountStruct). //private
          
	    dbConnection *os.File //private

        }








