#include <queue>
#include <string>
#include <iostream>

using namespace std;

void merge(char marbles[]) {
    int size = sizeof(marbles) / sizeof(marbles[0]); 
    for (int i = 0; i < size - 1; i++) {
        if (marbles[i + 1] == '1') {
            marbles[i] = '0';
        }
    }
}

int main() {

    int spots, num_of_marbles;
    cin >> spots >> num_of_marbles;

    string mbles;
    char marbles[spots];
    for (int i = 0; i < mbles.size(); i++) {
        marbles[i] = mbles[i];
    }

    while (num_of_marbles > 0) {
        merge(marbles);

        typedef pair<int, int> pi;
        priority_queue<pi, vector<pi>, greater<pi> > queue;    

        pair<int, int> count = make_pair(0, 0);
        int size = sizeof(marbles) / sizeof(marbles[0]); 
        for (int i = 0; i < size; i++) {
            if (marbles[i] == '0') {
                if (count.first == 0) {
                    count = make_pair(1, i);
                } else {
                    count.first++;
                }
            } else {
                if (count.first != 0) {
                    queue.push(count);
                    count = make_pair(0, 0);
                } 
            }
        }

        pi optimal = queue.top();
        queue.pop();

        while (optimal.first > num_of_marbles) {
            optimal = queue.top();
            queue.pop();
        } 

        for (int i = optimal.second; i < optimal.second + optimal.first; i++) {
            marbles[i] = '1';
        }
        num_of_marbles -= optimal.first;
    }

    int count = 0;
    int size = sizeof(marbles) / sizeof(marbles[0]); 
    for (int i = 0; i < size; i++) {
        if (marbles[i] == '1') {
            count++;
        }
    }
    cout << count << endl;

}