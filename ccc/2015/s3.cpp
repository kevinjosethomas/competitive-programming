#include <set>
#include <iostream>
#include <iterator>

using namespace std;

int main() {
    int g, p, count;
    count = 0;

    cin >> g;
    cin >> p;

    set<int> gates;
    for (int i = 1; i <= g; i++) {
        gates.insert(i);
    }

    for (int i = 0; i < p; i++) {
        int highest_gate; cin >> highest_gate;
        set<int>::iterator iter = gates.upper_bound(highest_gate);

        if (iter != gates.begin()) {
            iter--; count++;
            gates.erase(iter);
        } else {
            break;
        }
    }

    cout << count << endl;
}