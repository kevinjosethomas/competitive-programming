#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int mountains[5000];
vector<vector<int> > symmetry(5000, vector<int>(5000, -1));

int find_symmetry(int start, int end, int size) {
  int total = 0;
  for (int k = 0; k < size / 2; k++) {
    int i = start + k;
    int j = end - k;

    if (symmetry[i][j] != -1) {
      total += symmetry[i][j];
      break;
    }

    total += abs(mountains[start + k] - mountains[end - k]);
  }

  symmetry[start][end] = total;

  return total;
};

int main() {
  int n;
  cin >> n;

  for (int i = 0; i < n; i++) cin >> mountains[i];

  for (int window_size = 1; window_size <= n; window_size++) {
    int smallest = -1;
    for (int i = 0; i < n - window_size + 1; i++) {
      int j = i + window_size - 1;
      int symm = find_symmetry(i, j, window_size);

      if (smallest == -1 || symm < smallest) {
        smallest = symm;
      }
    }

    cout << smallest << " ";
  }

  return 0;
}
