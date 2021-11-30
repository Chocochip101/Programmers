#include<bits/stdc++.h>

using namespace std;

int answer = 0;


void dfs(vector<int> numbers, int target, int sum, int idx) {
    if (idx == numbers.size() && sum == target) {
         answer++;
        return;
    }
    if (idx >= numbers.size()) return;
    dfs(numbers, target, sum + numbers[idx], idx + 1);
    dfs(numbers, target, sum - numbers[idx], idx + 1);
}

int solution(vector<int> numbers, int target) {
    dfs(numbers, target, 0, 0);
    return answer;
}
int main() {
    cout << solution({ 1,1,1,1,1 }, 3);
}