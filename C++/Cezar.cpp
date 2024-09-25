#include <iostream>
#include <string>

using namespace std;

string secret(int key, string open_sms){
    string closed_sms = "";
    for (char c : open_sms){
	
	if (islower(c)){
	    c += key;
	    if (c > 120){
	        c -= 26;
	    }
	}
	else if (isupper(c)){
	    c += key;
	    if (c > 90){
	        c -= 26;
	    }
	}
	closed_sms += char(c);
    }

    return closed_sms;
}

int main(){
    int key;
    string sms;
    cout << "Введите сообщение для шифрования: ";
    getline(cin, sms);
    cout << "Введите ключ: ";
    cin >> key;

    string res = secret(key, sms);
    cout <<"Зашифрованный текст: " << res << endl;

    return 0;
}
