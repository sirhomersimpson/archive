#include <iostream>
using namespace std;

int gcd (int a, int b) {
    return (b==0 ? a: gcd(b, a%b));
}

int main() {
    int a = 100, b= 20;
    int result;
    result = gcd(a,b);
    cout << result;
}
