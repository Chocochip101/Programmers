#include <bits/stdc++.h>
#define INF 987654321
using namespace std;
typedef pair<int, int> p;

using namespace std;
vector<int> solution(vector<int> prices) {
	int len = prices.size();
	vector<int> answer(len);
	stack<int> s;
	for (int i = 0; i < len; ++i) {
		while (!s.empty() && prices[s.top()] > prices[i]) {
			answer[s.top()] = i - s.top();
			s.pop();
		}
		s.push(i);
	}

	while (!s.empty()) {
		answer[s.top()] = len - s.top() - 1;
		s.pop();

	}

	return answer;
}