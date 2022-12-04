package atcBankOps

import (
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func CreateFile(){
	_,err := os.Stat("Database.txt")
	if err==nil{
		fmt.Println("File is already Exist")
	}else if errors.Is(err,os.ErrNotExist){
		myFile,err := os.Create("Database.txt")
		if err != nil{
			log.Fatal(err)
		}
		log.Println(myFile)
		myFile.Close()
	}
	
}
func readFie(){
	CreateFile()
	if accounts !=nil{
		file, err := os.Open("Database.txt")
		if err != nil {
			fmt.Println(err)
		}
		defer file.Close()
		data ,err := ioutil.ReadAll(file)
		if err != nil{
			log.Fatal(err)
		}
		err= json.Unmarshal(data, &accounts)
		if err != nil{
			log.Fatal(err)
		}
		file.Close()

}

}
func writeFile(){
	CreateFile()
	content,err := json.MarshalIndent(accounts,"","\t")
	if err != nil{
		log.Fatal(err)
	}
	write:= ioutil.WriteFile("Database.txt",content,0644)
	if write != nil{
		log.Fatal(err)
	}
	
	

	// Acc, err := os.OpenFile("Database.txt",os.O_APPEND|os.O_WRONLY,0666)
	// if err != nil{
	// 	fmt.Println(err)
	// }
	// content,err := json.Marshal(accounts)
	// if err != nil{
	// 	fmt.Println(err)
	// } 
	// io.WriteString(Acc,string(content))
	// Acc.Close()
}


