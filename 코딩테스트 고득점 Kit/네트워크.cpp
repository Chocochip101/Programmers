#include <bits/stdc++.h>
#define INF 987654321
#define MAX 1000001
using namespace std;
typedef pair<int, int> p;

using namespace std;

bool visited[201];
void dfs(int n, vector<vector<int>>& computers, int now) {
	visited[now] = true;
	for (int i = 0; i < n; ++i)
		if (computers[now][i] && !visited[i] && i != now) {
			dfs(n, computers, i);
		}
}
int solution(int n, vector<vector<int>> computers) {
	int answer = 0;
	memset(visited, false, sizeof(visited));
	for (int i = 0; i < n; ++i)
		if (!visited[i])
		{
			answer++;
			dfs(n, computers, i);
		}return answer;
}
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cout << solution(3,{ {1,1,0},{1,1,0},{0,0,1} });
	return 0;
}