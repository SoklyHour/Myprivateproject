package main

import (
	"log"
	"net/http"
	"ATC.com/packages/atcBankOps"
	"github.com/gorilla/mux"
)

//export GO111MODULE="on"

func GetAccounts(w http.ResponseWriter,r *http.Request) {
	w.Header().Set("Content-Type","application/json")

	Get := atcBankOps.GetAcc()

	err := Get.EncodeToJson(w)
	if err != nil {
		http.Error(w, "Unable to marshal json", http.StatusInternalServerError)
	}

}
func CreateAccount(input []atcBankOps.Account_info) http.HandlerFunc{
	return func (w http.ResponseWriter, r *http.Request){
		
		w.Header().Set("Content-Type","application/json")
		var CreateAcc atcBankOps.Account_info;
		
		err:= CreateAcc.DecodeJson(r.Body)
		if err != nil {
			log.Fatal(err)
		}
		
		err =atcBankOps.AddAccount(CreateAcc,w)
		if err != nil{
			log.Fatal(err)
		}


	}
}
//Slice is a variable-length sequence which stores elements of a similar type, you are not allowed to store different type of elements in the same slice
func UpdateBalance(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	params := mux.Vars(r)
	var account atcBankOps.Account_info
	err:= account.DecodeJson(r.Body)
	if err != nil{
		log.Fatal("Unable to Unmarshal the data",err)
	}

	err=atcBankOps.UpdateAcc(params["account_number"],&account,w)
	if err != nil{
		log.Fatal(err)
	}
}
func DeleteAccount(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application-json")
	params := mux.Vars(r)
	del:=atcBankOps.DeleteAcc(params["account_number"],w)
	if del != nil {
		log.Fatal(del)
	}
	
}
func main() {
	r := mux.NewRouter()
	// r.HadleFunc is similar to HTTP.HandleFunc
	r.HandleFunc("/Account",GetAccounts).Methods("Get")
	r.HandleFunc("/Account", CreateAccount([]atcBankOps.Account_info{})).Methods("Post")
	r.HandleFunc("/Account/{account_number}", UpdateBalance).Methods("Put")
	r.HandleFunc("/Account/{account_number}", DeleteAccount).Methods("Delete")
	log.Fatal(http.ListenAndServe(":8080",r))
}


