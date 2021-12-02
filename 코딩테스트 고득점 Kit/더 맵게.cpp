#include <bits/stdc++.h>

using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int>> pq;
    
    for (int a : scoville)
        pq.push(a);

    int answer = 0;
    while (true) {
        if (pq.top() >= K) break;
        if (pq.size() == 1) return -1;

        int a = pq.top(); pq.pop();
        int b = pq.top(); pq.pop();
        pq.push(a + 2 * b);
        answer++;
    }
    return answer;
}
int main() {
    cout << solution({ 1,2,3,9,10,12 }, 7);
}