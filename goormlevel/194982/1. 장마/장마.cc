#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    vector<int> home(N);
    vector<bool> visited(N, false);

    for (int i = 0; i < N; i++) {
        cin >> home[i];
    }

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        for (int x = a - 1; x < b; x++) {
            home[x]++;
            visited[x] = true;
        }

        if ((i + 1) % 3 == 0) {
            for (int check = 0; check < N; check++) {
                if (visited[check]) {
                    home[check]--;
                }
            }
            fill(visited.begin(), visited.end(), false);
        }
    }

    for (int i = 0; i < N; i++) {
        cout << home[i] << " ";
    }
    cout << endl;

    return 0;
}
