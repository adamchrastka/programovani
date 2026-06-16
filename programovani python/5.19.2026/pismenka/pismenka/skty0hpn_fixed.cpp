#include <iostream>
#include <string>
#include <thread>
#include <chrono>
#include <cstdlib>

using namespace std;

int main() {
    string text;

    cout << "Zadejte slovo: ";
    cin >> text;

    for (char c : text) {
        system("cls");
                for (int i = 0; i < 10; i++) {
            cout << c;
			cout << "\n";
        }
        this_thread::sleep_for(chrono::milliseconds(500));
    }

    return 0;
}