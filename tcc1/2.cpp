#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int main() {
  // Your code here

  int n, k;
  cin >> n >> k;

  int testcase[n];
  for (int i = 0; i < n; i++) {
    cin >> testcase[i];
  }

  for (int d = 1; d <= k; d++) {
    int x_d;
    cin >> x_d;
    int purged_sum = 0;
    int ignore_queue = 0;

    for (int a = n - 1; a >= 0; a--) {
      if (testcase[a] == d) {
        ignore_queue += x_d;
      } else {
        if (ignore_queue > 0) {
          ignore_queue--;
        } else {
          purged_sum += testcase[a];
        }
      }
    }

    cout << purged_sum << endl;
  }

  return 0;
}
