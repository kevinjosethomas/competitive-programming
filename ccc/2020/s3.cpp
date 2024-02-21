#include <set>
#include <array>
#include <string>
#include <iostream>

using namespace std;

const int p = 31;
const int m = 1e9 + 9;
long long hasher(string s) {
    long long hash_value = 0;
    long long p_pow = 1;
    for (char c : s) {
        hash_value = (hash_value + (c - 'a' + 1) * p_pow) % m;
        p_pow = (p_pow * p) % m;
    }

    return hash_value;
}

int main() {
    string needle, haystack;
    cin >> needle >> haystack;

    set<long long> matches;
    array<int, 26> window_freq = {};
    array<int, 26> needle_freq = { 0 };

    for (char c : needle) {
        needle_freq[c - 'a']++;
    }

    for (int i = 0; i < haystack.size() - needle.size() + 1; i++) {
        string possible_needle = haystack.substr(i, needle.size());

        if (i == 0) {
            for (char c : possible_needle) {
                window_freq[c - 'a']++;
            }
        } else {
            window_freq[haystack[i - 1] - 'a']--;
            window_freq[haystack[i + needle.size() - 1] - 'a']++;
        }

        if (needle_freq == window_freq) {
            matches.insert(hasher(possible_needle));
        }   
    }

    cout << matches.size() << endl;
}