package main

import (
	"log"
	"net/http"
	"ATC.com/packages/atcBankOps"
	"ATC.com/packages/handlers" 
	"github.com/gorilla/mux"
)

//export GO111MODULE="on"


func main() {
	r := mux.NewRouter()
	// r.HadleFunc is similar to HTTP.HandleFunc
	r.HandleFunc("/Account",handlers.GetAccounts).Methods("Get")
	r.HandleFunc("/Account", handlers.CreateAccount([]atcBankOps.Account_info{})).Methods("Post")
	r.HandleFunc("/Account/{account_number}", handlers.UpdateBalance).Methods("Put")
	r.HandleFunc("/Account/{account_number}", handlers.DeleteAccount).Methods("Delete")
	log.Fatal(http.ListenAndServe(":8081",r))
}


