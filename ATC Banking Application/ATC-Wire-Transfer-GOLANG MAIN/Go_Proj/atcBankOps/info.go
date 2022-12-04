package atcBankOps

import (
	"encoding/json"
	"fmt"
	"io"
)
type Account_info struct{

	National_ID string `json:"national_id"` 
	Card_Number string `json:"card_number"`
	SWIFT string `json:"swift"`
	Balance float64 `json:"balance"`
	First_Name string  `json:"first_name"`
	Last_Name string `json:"last_name"`
	Address1 string `json:"address1"`
	Address2 string `json:"address2"`
	Address3 string `json:"address3"`
	Country string `json:"country"`
	Routing_Number string `json:"routing_number"`
	Account_Number map[string]string `json:"account_number"`
}
var accounts []*Account_info

type account []*Account_info

func (Acc *account) EncodeToJson(w io.Writer) error{
	encode:= json.NewEncoder(w)
	return encode.Encode(Acc)
}
func (Acc *Account_info) DecodeJson(r io.Reader) error {
	e := json.NewDecoder(r)
	return e.Decode(Acc)
}

func GetAcc() account{
	if !(ReadAcc("Database.txt")){
		fmt.Println("cannot read file")
	}
	return accounts
}

func cheackAccountNum(Account_Number string) bool{
	if !(ReadAcc("Database.txt")){
		fmt.Println("cannot read file")
		return false
	}else {
	for _, p := range accounts {
		if p.Account_Number["Account_Number"] == Account_Number{
			return false
		}
	}
}
	return true
}

func AddAccount(accNum Account_info,w io.Writer) error{
 	if !(cheackAccountNum(accNum.Account_Number["Account_Number"])){
		fmt.Fprintln(w,"Account Number Aleready Exist. ")
	
	}else{
		accounts=append(accounts, &accNum)
		WriteAcc("Database.txt")
		fmt.Fprintln(w,"Account has Created.")
	}
	return nil
}


func UpdateAcc(Account_Number string,account *Account_info,w io.Writer)error{
	for index, id := range accounts {
		if id.Account_Number["Account_Number"]== Account_Number{
			accounts = append(accounts[:index], accounts[index+1:]...)
			accounts = append(accounts, account)
			WriteAcc("Database.txt")
			fmt.Fprint(w,"Account was updated")
			break
		}
	}
	return nil
}

func DeleteAcc(Account_Number string,w io.Writer) error{
		for index, id := range accounts {
			if id.Account_Number["Account_Number"] == Account_Number {
				accounts = append(accounts[:index], accounts[index+1:]...)
				WriteAcc("Database.txt")
				fmt.Fprint(w,"Account was delete")
				break
			}
	}
	return nil
}

