#include <iostream>
using namespace std;

int main() {
    //declaracion de variables
   double peso, altura, imc;
    //solicitamos la informacion de usuario
    cout<< "digite su peso (kg): ";
    cin>> peso;
    cout<<"digite su altura: ";
    cin>>altura;
    //hacemos la formula
    imc = peso / (altura*altura) ;
    cout<<"su imc es:"<<imc<< endl;
    
    }
