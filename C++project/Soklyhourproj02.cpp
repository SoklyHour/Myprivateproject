#include <iostream>
using namespace std;
int main(){
    char gender, try_again;
    bool new_calculation = true;
    double weight, height, bmr, chocolate_bar_calories;
    int age;

    cout<<"Welcome to my BMR caculator.\n";
    while(new_calculation){

        cout<<"Gender (M OR F): ";
        cin>>gender;

        while(gender != 'M' && gender != 'm' && gender != 'F' && gender != 'f'){

            cout<<"Wrong input. please enter again. Gender (M or F): ";
            cin>>gender;

        }
        cout<<"Weight in pounds: ";
        cin>>weight;

        cout<<"Height in inches: ";
        cin>>height;

        cout<<"Age in years: ";
        cin>> age;

        if((gender == 'M') || (gender== 'm')){
            bmr = 66 + ( 6.3* weight)+ (12.9*height)-(6.8*age);
            chocolate_bar_calories= bmr /230;

            cout<<"He needs "<< bmr << " calories to maintain his weighjt.\n";
            cout<<"That is about "<<chocolate_bar_calories<<" chocolate bar calories.\n";
    
        }
        else{
            bmr = 655+(4.3*weight)+(4.7 * height)-(4.7*age);
            chocolate_bar_calories=bmr /230;

            cout<<"She needs "<<bmr<<" calories to amintain her weight.\n";
            cout<<"That is about "<<chocolate_bar_calories<<" chocolate bar calories.\n";

        }
        cout<<"Do you want to do another calculation?(Y/N): ";
        cin>>try_again;

        if(try_again=='Y'||try_again=='y')
        new_calculation=true;
        else{
            new_calculation=false;
        }
        cout<<"Thank you for suing our BMR calculator,\n";
    }
    return 0;
}
