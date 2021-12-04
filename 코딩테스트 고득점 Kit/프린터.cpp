#include <bits/stdc++.h>

using namespace std;
typedef pair<int, int> p;
int solution(vector<int> priorities, int location) {
    int answer = 0;
    priority_queue<int> pq;
    queue<p> q;
    for (int i = 0; i < priorities.size(); ++i) {
        pq.push(priorities[i]);
        q.push({ i, priorities[i] });
    }

    while (!q.empty()) {
        int idx = q.front().first;
        int val = q.front().second;
        q.pop();

        if (val == pq.top()) {
            pq.pop();
            answer++;
            if (idx == location)
                return answer;

        }
        else
            q.push({ idx, val });
    }
    return answer;
}
